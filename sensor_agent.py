from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State
from environment import DisasterEnvironment

STATE_IDLE = "IDLE"
STATE_ASSESS = "ASSESS"
STATE_MONITOR = "MONITOR"
STATE_ALERT = "ALERT"
STATE_EMERGENCY = "EMERGENCY"


class SensorAgent(Agent):

    class DisasterFSM(FSMBehaviour):
        async def on_start(self):
            print("[FSM] Disaster Response FSM Started")

    # ---------------- STATES ----------------

    class IdleState(State):
        async def run(self):
            print("[STATE] IDLE - Monitoring environment...")
            event, severity = self.agent.environment.sense()

            if event != "None":
                print(f"[EVENT] {event} detected (Severity: {severity})")
                self.agent.current_event = (event, severity)
                self.set_next_state(STATE_ASSESS)
            else:
                self.set_next_state(STATE_IDLE)

    class AssessState(State):
        async def run(self):
            print("[STATE] ASSESSING disaster...")
            event, severity = self.agent.current_event

            if severity <= 4:
                self.set_next_state(STATE_MONITOR)
            elif 5 <= severity <= 7:
                self.set_next_state(STATE_ALERT)
            else:
                self.set_next_state(STATE_EMERGENCY)

    class MonitorState(State):
        async def run(self):
            print("[ACTION] Monitoring low-severity situation.")
            self.set_next_state(STATE_IDLE)

    class AlertState(State):
        async def run(self):
            print("[ACTION] Sending ALERT to rescue teams.")
            self.set_next_state(STATE_IDLE)

    class EmergencyState(State):
        async def run(self):
            print("[ACTION] Initiating EMERGENCY RESPONSE!")
            self.set_next_state(STATE_IDLE)

    async def setup(self):
        print("SensorAgent with FSM started")
        self.environment = DisasterEnvironment()

        fsm = self.DisasterFSM()

        fsm.add_state(name=STATE_IDLE, state=self.IdleState(), initial=True)
        fsm.add_state(name=STATE_ASSESS, state=self.AssessState())
        fsm.add_state(name=STATE_MONITOR, state=self.MonitorState())
        fsm.add_state(name=STATE_ALERT, state=self.AlertState())
        fsm.add_state(name=STATE_EMERGENCY, state=self.EmergencyState())

        fsm.add_transition(source=STATE_IDLE, dest=STATE_IDLE)
        fsm.add_transition(source=STATE_IDLE, dest=STATE_ASSESS)
        fsm.add_transition(source=STATE_ASSESS, dest=STATE_MONITOR)
        fsm.add_transition(source=STATE_ASSESS, dest=STATE_ALERT)
        fsm.add_transition(source=STATE_ASSESS, dest=STATE_EMERGENCY)
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_IDLE)
        fsm.add_transition(source=STATE_ALERT, dest=STATE_IDLE)
        fsm.add_transition(source=STATE_EMERGENCY, dest=STATE_IDLE)

        self.add_behaviour(fsm)