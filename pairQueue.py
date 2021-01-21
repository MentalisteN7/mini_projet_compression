import heapq

class PairQueue():
    
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
        done = not self.isEmpty()
        pair = (0,0)
        while not done:
            popped = heapq.heappop(self.heap)
            pairCand = popped[2]
            if not ((pairCand[0] in deletedVertices) or (pairCand[1] in deletedVertices)):
                pair = pairCand
                done = True
            else:
                done = self.isEmpty()
        return pair
            
    def isEmpty(self):
        return self.heap == [] 