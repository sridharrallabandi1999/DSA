import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        
        pq = [(0, src, 0)]
        
       
        dist = {}

        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            
            if node == dst:
                return cost
            
            
            if stops > k:
                continue

            
            for neighbor, price in graph[node]:
                new_cost = cost + price
                
                
                if (neighbor, stops) not in dist or new_cost < dist[(neighbor, stops)]:
                    dist[(neighbor, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # If no path was found, return -1
        return -1
