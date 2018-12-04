### **Agent-Based Models (ABM)** 

Throughout my learning so far, I have been able to produce an Agent-Based Model (ABM). This form of model is useful for understanding how individuals, or agents, interact with one another and with their environment. The agent will randomly move within their environment for a number of times, which is measured by the number of iterations the model has been set to. Eventually, a pattern will emerge from the agent's movements in the environment which can reveal the complex relationships the agents have with their environment. 

**Creating the Foundations for an ABM**

The code for the ABM can be found [here](ABM.py)

In order to function an ABM, there needs to be a *model code*, *agent code* and *environment code*. The *model code* is where we set up the ABM's iterations, for loops, stopping commands; the *agent code* is used to build the agents and their behaviours, the code also allows agents to understand their neighbours' (other agents) behaviours so they can interact with one another; and the *environment code* is the agent's territory which keeps the agents within a limited space. 

My ABM contained 10 agents whom had the ability to eat, move, and share their distance with their neighbours to prevent any collisions, in this case we can call the agents 'sheep'. The environment in the ABM was raster data, which is made up of cells where each one is appointed a value. The sheep's number of iterations were set to 100, meaning they could move and eat around 100 times until the model code told them to stop, this would produce patterns from where the sheep had been interacting with their environment. 

**Application of ABMs in the real world**

ABMs are really useful when looking into criminal offences as they help to explore the relationship burglars have with their environment, or neighbourhood. I hope to implement an ABM into my PhD research 
