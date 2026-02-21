from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from environment import DisasterEnvironment

class SensorAgent(Agent):
    class SenseBehaviour(PeriodicBehaviour):
        async def run(self):
            event, severity = self.agent.environment.sense()
            if event != "None":
                print(f"[SENSOR] Detected {event} with severity {severity}")
            else:
                print("[SENSOR] No disaster detected")

    async def setup(self):
        print("SensorAgent started")
        self.environment = DisasterEnvironment()
  
        self.add_behaviour(self.SenseBehaviour(period=5))
