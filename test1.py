from abc import ABC, abstractmethod


class Node(ABC):

    @abstractmethod
    def __eq__(self, other):
        
        pass


    @abstractmethod
    def is_the_solution(self, state):
        
        pass


    @abstractmethod
    def extend_node(self):
        
        pass


    @abstractmethod
    def __str__(self):
        
        pass


    

class BFS:

    def __init__(self, start, final):

        self.start_state = start
        self.final_state = final
        self.frontier = [self.start_state]
        self.checked_nodes = []
        self.number_of_steps = 0
        self.path = []


    def inser_to_frontier(self, node):

        self.frnotier.append(node)


    def remove_from_frontier(self):

        firest_node = self.frontier.pop(0)
        self.checked_nodes.append(first_node)
        return first_node

        


    


    
