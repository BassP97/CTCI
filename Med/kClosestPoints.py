"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique 
(except for the order that it is in.)
"""
import math
import heapq

def calculateDistance(points,k):
    distances = []
    for point in points:
        distance = math.pow(point[0],2) + math.pow(point[1],2)
        distance = math.sqrt(distance)
        distances.append(distance)
    heap = heapq._heapify_max(distances)
    retArr = []
    for i in range(k):
        retArr.append(heapq._heappop_max(heap))
    return retArr

#intuition - use heapq as a repository, and insert items until we reach heap of size k
#then, insert remaining items and pop (remove the smallest item)
#runs in N*Log(k) time due to heapify taking log(k) time
def calculateDistanceMinHeap(points, k):
    heap = []
    for point in points:
        distance = math.pow(point[0],2) + math.pow(point[1],2)
        distance = math.sqrt(distance)
        heapq.heappush(heap, distance)
        if len(heap)>k:
            heapq.heappop(heap)
        