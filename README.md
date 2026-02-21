# 403_lab1-2
# 403_lab3


**1**
**Agent Goals**
In the laboratoory, the Sensoragent was extended to include explicit goals that guide its reactive behavior within the disaster environment.

**Rescue and Response Goals**
The recue and response goals define how the agent reacts when a disater event is detected:
- Respond to detected disaster events.
- Prioritize high-severity disasters over-severity situations.
- Trigger an emergency response when the severity level is critical.
- Send alerts for meduim-severity disaster events.

These goals ensure that the agent takes appropiate action depending on the seriousness of the disaster

**Monitoring Goals**
The monitering goals ensure continuous environmental awareness:
- Continously monitor the stimulated disaster environment.
- Classify detected disasters based on severity levels.
- Return to the idle monitoring state after handling each event.

**2**
**Implementation of FSM Behaviour**
In Lab 2, the SensorAgent used a PeriodicBehaviour to continuously sense the environment at fixed time intervals. While this allowed the agent to detect disasters, it did not support structured decision-making or state-based reactions.

For Lab 3, the **PeriodicBehaviour** was replaced with **FSMBehaviour**(Finite State Machine Behaviour). This change allows the agent to transition between defined states based on detected events and severity levels.

The FSMBehaviour enables:
- State-based decision-making
- Event-triggered transitions
- Goal-driven reactive behavior
- Structured handling of disaster situations

By replacing **PeriodicBehaviour** with **FSMBehaviour**, the SensorAgent now reacts differently depending on the severity of detected disaster events.




**3**
**Finite State Machine (FSM) States**
To implement reactive behavior, the SensorAgent was redesigned using a Finite State Machine (FSM). The following states were defined:

1. **IDLE State**
The IDLE state represents the default monitoring conditions of the agent.
In this state, the agent continuously senses the environment for possible disaster events.
If no disaster is detected, the agent remains in the IDLE state.
If a disaster event is detected, the agent transitions to the ASSESS state.

2. **ASSESS State**
The ASSESS state is responsible for evaluating the severity of a detected disaster event.
The agent classifies the severity level into low, medium, or high categories.
Based on this classification, the agent transitions to one of the following states: MONITOR, ALERT, or EMERGENCY.

3. **MONITOR State**
The MONITOR state handles low-severity disaster events.
In this state, the agent continues observing the situation without escalating the response.
After monitoring, the agent returns to the IDLE state.

4. **ALERT State**
The ALERT state handles medium-severity disaster events.
In this state, the agent generates an alert to notify rescue teams or relevant authorities.
After sending the alert, the agent transitions back to the IDLE state.

5. **EMERGENCY State**
The EMERGENCY state handles high-severity disaster events.
In this state, the agent initiates an emergency response procedure.
After triggering the emergency response, the agent returns to the IDLE state.
