"""
There are a total of numCourses prerequisites you have to take, labeled from 0 to numCourses-1.

Some prerequisites may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of prerequisites and a list of prerequisite pairs, is it
possible for you to finish all prerequisites?
"""

def findSchedule(numCourses,prerequisites):
    adjMatrix = {}
    for course in prerequisites:
        if course[0] in adjMatrix.keys():
            adjMatrix[course[0]].append(course[1])
        else:
            adjMatrix[course[0]] = [course[1]]
    queue = [prerequisites[0]]
    seenCourses = set(prerequisites[0][0])
    while queue:
        currLoc = queue.pop()
        if currLoc in seenCourses:
            return False
        seenCourses.add(currLoc)
        for neighbor in adjMatrix[currLoc]:
            queue.append(neighbor)
    return True
        