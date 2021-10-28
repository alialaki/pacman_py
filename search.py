# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #get starting state 
    startState = problem.getStartState()
    #fringe (Stack) to store the nodes along with their paths
    fringe = util.Stack()
    visited = []
    fringe.push((startState, []))
    while not fringe.isEmpty():
        #remove first node from list of checkable states
        currentNode = fringe.pop()
        #check whether current node is in visited list or not
        if currentNode[0] not in visited:
            #add most recent node to visited list
            visited.append(currentNode[0])
            #check whether current node goal state or not
            if problem.isGoalState(currentNode[0]):
                return currentNode[1]
            #get child states 
            for nodes in problem.getSuccessors(currentNode[0]):
                fringe.push((nodes[0], currentNode[1] + [nodes[1]]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #get starting state 
    startState = problem.getStartState()
    #Fringe (Queue) to store the nodes along with their paths
    fringe = util.Queue()
    visited = []
    fringe.push((startState, []))
    while not fringe.isEmpty():
        #remove first node from list of checkable states
        currentNode = fringe.pop()
        #check whether current node is in visited list or not
        if currentNode[0] not in visited:
            #add most recent node to visited list
            visited.append(currentNode[0])
            #check whether current node goal state or not
            if problem.isGoalState(currentNode[0]):
                return currentNode[1]
            #get child states
            for nodes in problem.getSuccessors(currentNode[0]):
                fringe.push((nodes[0], currentNode[1] + [nodes[1]]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #fringe (Priority Queue) to store the nodes along with their paths
    fringe = util.PriorityQueue()    
    startState = problem.getStartState()
    Visited = []
    #push (Node, [Path from start-node till 'Node'], culmulative backward cost till 'Node') to the fringe. 
    fringe.push((startState, [], 0), heuristic(startState, problem) + 0)    
    while not fringe.isEmpty():
        currentNode = fringe.pop()
        #check whether current node goal state or not, if current node is goal state, then exit the loop 
        if problem.isGoalState(currentNode[0]):    
            break
        else:
            #distinguish already visited nodes
            if currentNode[0] not in Visited:
                #append novelty encountered nodes to the set of visited nodes    
                Visited.append(currentNode[0])     
                successors = problem.getSuccessors(currentNode[0])
                for child_node, child_path, child_cost in successors:
                    #compute path of child node from start node
                    totalPath = currentNode[1] + [child_path]    
                    #compute total(cumulative) backward cost of child node from start node
                    totalCost = currentNode[2] + child_cost
                    #push (Node, [Path], Culmulative backward cost) to the fringe.    
                    fringe.push((child_node, totalPath, totalCost), totalCost + heuristic(child_node, problem))    

    return currentNode[1]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
