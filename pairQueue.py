import heapq
import numpy as np

class PairQueue():
    """
    File de priorité pour les paires de sommet
    Les paires de plus faible coût sont prioritaires
    Les paires sont adjointes du sommet qui sert à les contracter
    """
    
    def __init__(self, pairList, costList):
        self.heap = []
        self.counter = 0
        for i in range(len(pairList)):
            heapq.heappush(self.heap, (costList[i], self.counter, pairList[i]))
            self.counter += 1

    
    def push(self, pair, cost):
        heapq.heappush(self.heap, (cost, self.counter, pair))
        self.counter += 1
    
    def pop(self, deletedVertices):
        done = self.isEmpty()
        pair = (0,0,np.zeros(3))
        while not done:
            popped = heapq.heappop(self.heap)
            pairCand = popped[2]
            if not ((pairCand[0] in deletedVertices) or (pairCand[1] in deletedVertices)):
                pair = pairCand
                done = True
            else:
                print('Le haut de la file était pas clean')
                done = self.isEmpty()
        self.cleanTop(deletedVertices)
        return pair
            
    def isEmpty(self):
        return self.heap == []
    
    def cleanTop(self, deletedVertices):
        done = self.isEmpty()
        while not done:
            popped = heapq.heappop(self.heap)
            pair = popped[2]
            if not ((pair[0] in deletedVertices) or (pair[1] in deletedVertices)):
                done = True
                heapq.heappush(self.heap, popped)
            else:
                done = self.isEmpty()
            

def main():
    pair_one = [1,2]
    pair_two = [1,3]
    pair_three = [2,3]
    pair_list = [pair_one, pair_two, pair_three]
    cost_list = [4,2,3]
    pair_queue = PairQueue(pairList=pair_list, costList=cost_list)

    print('pair_queue.heap = ', pair_queue.heap)

    deletedVertices = []
    pop = pair_queue.pop(deletedVertices)
    print('pop = ', pop)

    print('coucou')

if __name__ == "__main__":
    # execute only if run as a script
    main()
