import asyncio
from sensor_agent import SensorAgent
import logging


logging.basicConfig(level=logging.DEBUG)

async def main():

    xmpp_jid = "agent125@xmpp.jp"
    xmpp_password = "pass1234"

    agent = SensorAgent(xmpp_jid, xmpp_password)

 
    await agent.start(auto_register=False)
    print("SensorAgent is running...")

    await asyncio.sleep(40)


    await agent.stop()
    print("SensorAgent stopped")

asyncio.run(main())
