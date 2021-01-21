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
    
    def pop(self):
        popped = heapq.heappop(self.heap)
        pair = popped[2]
        return pair
            
    def isEmpty(self):
        return self.heap == [] 