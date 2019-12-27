"""
Write a function that takes:

    a list of unsorted_scores
    the highest_possible_score in the game

and returns a sorted list of scores in less than O(nlg⁡n) time.

For example:

    unsorted_scores = [37, 89, 41, 65, 91, 53]
    HIGHEST_POSSIBLE_SCORE = 100

    # Returns [91, 89, 65, 53, 41, 37]
    sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

We’re defining n as the number of unsorted_scores because we’re expecting the number of players to keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring it into our big O time and space costs because the highest possible score isn’t going to change. Even if we do redesign the game a little, the scores will stay around the same order of magnitude. 
"""
def unsorted_scores(scores, highestScore):
    scoreCount = []
    retArr = []
    for i in range(0,highestScore):
        scoreCount.append(0)
    for score in scores:
        scoreCount[score] =  scoreCount[score]+1
    for i in range(highestScore-1,0,-1):
        for j in range(0,scoreCount[i]):
            retArr.append(i)
    print(retArr)
    return retArr
assert(unsorted_scores([37, 89, 41, 65, 91, 53], 100) == [91, 89, 65, 53, 41, 37])

