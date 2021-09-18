# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is 
# "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

def wordLadder(b,e,list):
    if e not in list:
        return 0 
    min_len = len(list) +1 

def bfs(root,t,queue):
    if not root:
        return null
    
    while root:
        if root.val == t:
            return root
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        root = queue.pop()
