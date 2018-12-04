
# Imports

import csv 
import AgentFramework
import random
import matplotlib.pyplot
import matplotlib.animation


### DEFINING THE AGENT #####################################################

class Agent:
   
    def __init__(self, environment, agents):
         self.x = random.randint(0,120)
         self.y = random.randint(0,120)
         self.x = random.randint(0,len(environment[0]))
         self.y = random.randint(0,len(environment))
         self.environment = environment
         self.store = 0
         self.agents = agents
    
    def move(self):
        if random.random() < 0.5:
             self.x = (self.x + 1) % 120
        else:
             self.x = (self.x - 1) % 120
           
        if random.random() < 0.5:
             self.y = (self.y + 1) % 120
        else:
             self.y = (self.y - 1) % 120
            
            
# Allowing the agents to eat at 10 units a time: 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                
                
  
    def distance_between(self,agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5


# setting the frame for the animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Environment 

environment = []


f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)  
    environment.append(rowlist)

f.close()


# Setting up the number of agents, iterations and the neighbourhood

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []




# Create the agents

fig.clear()

# Plot the agents in their environment 
def update(frame_number):  
    
    fig.clear() 


    for i in range(num_of_agents):
        agents.append(AgentFramework.Agent(environment, agents))
    
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #this is plotting the axis
        matplotlib.pyplot.xlim(0, 120)
        matplotlib.pyplot.ylim(0, 120)
        #this is plotting the environment
        matplotlib.pyplot.imshow(environment)


    
# Move the agents
   
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
       
        
        # plotting agents
       
        matplotlib.pyplot.xlim(0, 120)
        matplotlib.pyplot.ylim(0, 120)
        

# Animate the agent's movements in the environment
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
matplotlib.pyplot.show()