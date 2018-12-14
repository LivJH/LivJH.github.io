import random

# DEFINING THE AGENT 


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

