
# Imports
import random
import csv 
import AgentFramework
import matplotlib.pyplot
import matplotlib.animation


# SETTING UP THE AGENTS

# We define 10 agents
num_of_agents = 10
# The agents will move 10 times in each loop
num_of_iterations = 2
neighbourhood = 20
agents = []



# Setting the frame for the animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])




# ENVIRONMENT- this is created from a list of values.

environment = []

# open file containing environment values
f = open('in.txt', newline='')
# read the file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# append the values from the environment
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)  
    environment.append(rowlist)
    
f.close()

# Add agents onto environment
for i in range(num_of_agents):
        agents.append(AgentFramework.Agent(environment, agents))





# CREATE THE AGENTS

fig.clear()

# Plot the agents in their environment 
def update(frame_number):  
    
    fig.clear() 
    
    #this is plotting the environment
    matplotlib.pyplot.imshow(environment)
    # creating a for loop to move the agents by the number of iterations
    for i in range(num_of_iterations):
           # Agents move randomly
           random.shuffle(agents)
           # Allow the agents to perform actions which were defined in the
           # agent framework
           for i in range(num_of_agents):
               agents[i].move()
               agents[i].eat()
               agents[i].share_with_neighbours(neighbourhood)

    # This plots the agents onto the graph
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        # This is plotting the axis
    matplotlib.pyplot.xlim(0, 120)
    matplotlib.pyplot.ylim(0, 120)
 


# Animate the agent's movements in the environment
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
# Show the model
matplotlib.pyplot.show()
