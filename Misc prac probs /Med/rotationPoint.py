"""
 I opened up a dictionary to a page in the middle and started flipping through, 
 looking for words I didn't know. I put each word I didn't know at increasing 
 indices in a huge list I created in memory. When I reached the end of the 
 dictionary, I started from the beginning and did the same thing until I reached 
 the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere 
in the middle of the alphabet, reach the end, and then start from the beginning 
of the alphabet. In other words, this is an alphabetically ordered list that has 
been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is 
where I started working from the beginning of the dictionary. This list 
is huge (there are lots of words I don't know) so we want to be efficient here. 
"""

"""
consider list: d,e,f,g,a,b,c
steps: 
   e,f,g,a,b,c,d
alternate:
    g,a,b,c,d,e,f

notes:
- wanna use binary search

"""
def rotationBSearchRec(arr, left, right):
    mid = left+((right-left)//2)
    print (left, right, arr[right])
    if right-left<=1:
        return arr[right]
    if arr[mid]>=arr[left]:
        left = mid
        return rotationBSearchRec(arr,left,right)
    else:
        right = mid
        return rotationBSearchRec(arr,left,mid)

    

def rotationBSearch(arr):
    print("")
    return rotationBSearchRec(arr, 0, len(arr)-1)

print(rotationBSearch(['c','d','e','f','g','a','b']))
print(rotationBSearch(['e','f','g','a','b','c','d']))
print(rotationBSearch(['f','g','a','b','c','d','e']))
['f','g','a','b','c','d','e']
['e','f','g','a','b','c','d']
