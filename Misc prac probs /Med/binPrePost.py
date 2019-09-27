"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]



Note:

    1 <= pre.length == post.length <= 30
    pre[] and post[] are both permutations of 1, 2, ..., pre.length.
    It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.


"""

def prePost(pre, post, curr):
    curr.value = pre[0]
    if not(len(pre) == len(post) == 1):
        #create preorder lists for left and right subtrees
        #we exploit the property of pre and postorder - preorder[1] is the root of the left
        #subtree while postorder[-2](the second to last element of postorder) is the root of
        #the right subtree
        preLeft = pre[1:pre.index(post[-2])+1]
        preRight = pre[pre.index(post[-2])+1:]

        postLeft = post[0:post.index(pre[1])]
        postRight = post[post.index(pre[1]):len(postRight)-2]

        curr.left = prePost(preLeft,postLeft)
        curr.right = prePost(preRight,postRight)
    return curr
