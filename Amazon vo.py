# Oct 21 
# ------------------------------------ 1 ---------------------------------------------------------
# Leetcode 451. Sort Characters By Frequency
# Given a string, sort it in decreasing order based on the frequency of characters.
# ** Hash Map / Bucket Sort
# Example 1:
# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
class Solution:
    # METHOD 1: HashMap -> Orderby Value -> Map nlogn
    def frequencySort(self, s: str) -> str:
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char,0) + 1
        charMap = sorted(charMap.items(), key = lambda x : x[1], reverse = True)
        res = ""
        for key, value in charMap:
            while value > 0:
                res += key
                value -=1
        return res
    # METHOD 2: BUCKET SORT -> n
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        counts = collections.Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for i in range(max_freq+1)]
        for key,value in counts.items():
            buckets[value].append(key)
        res = ""
        for i in range(len(buckets)-1,0,-1):
            for c in buckets[i]:
                res += c * i
        return res
# ------------------------------------ 2 ---------------------------------------------------------
# Leetcode 139. Word Break
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine 
# if s can be segmented into a space-separated sequence of one or more dictionary words.
# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
class Solution:
    # METHOD 1: BFS with Queue + check max len 
    # Run Time:  n*lem(max_len in wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = []
        queue.append(0)
        n = len(s)
        seen = set()
        max_len = 0
        for word in wordDict:
            if len(word)> max_len:
                max_len = len(word)   
        while queue:
            if queue[0] == n:
                return True
            start = queue[0]
            queue = queue[1:]
            if start not in seen:
                seen.add(start)
                end = start
                while end < n and (end-start + 1) <= max_len:
                    word = s[start:end+1]
                    if word in wordDict:
                        queue.append(end+1)
                    end +=1
        return False
    # METHOD 2: RECURSION + MEMO
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        def recursion_w_memo(start,s,memo):
            # base case start == n: return True
            if start == len(s):
                return True
            if memo[start]!= None:
                return memo[start]
            # recursive step: 
            # if we know the chars before start is in dict, we just need to check 
            # from start to end if those are in dict
            end = start + 1
            while end < len(s)+1:
                word = s[start:end]
                if word in wordDict :
                    can_word_break = recursion_w_memo(end,s,memo)
                    if can_word_break:
                        memo[start] = True
                        return True
                end +=1
            memo[start] = False
            return False
               
        memo = [None for x in range(len(s))]
        return recursion_w_memo(0,s,memo)
# ------------------------------------ 3 ---------------------------------------------------------
# Leetcode 240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false
class Solution:
    # METHOD 1: 缩小范围法，因为r最多可以缩小row次，c最大可以扩大col次，每个循环只调一个参数
    # 所以time complexcity : row + col
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        r = row - 1
        c = 0
        
        while r < row and c < col and r >= 0 and col >=0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -=1
            if matrix[r][c] < target:
                c+=1
        return False
    # METHOD 2: RECURSION
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False 
        row = len(matrix)
        col = len(matrix[0])
        
        def recursion(lr,rr,lc,rc,target):
            # Base Case:
            # If the area is empty, return False 
            # if lr < target: return False
            # if rc > target : return 
            if lr > rr or lc > rc:
                return False
            if matrix[lr][lc] > target:
                return False
            if matrix[rr][rc] < target:
                return False 
            # RECURSIVE STEP: 每次先缩小范围
            while lr <=rr:
                if matrix[rr][lc] > target:
                    rr -=1
                else:
                    break
            while lc <= rc:
                if matrix[lr][rc] > target:
                    rc -=1
                else:
                    break
            # 利用col分成上半和下班
            mid_r = lr + (rr-lr)//2
            i = lc
            # search mid 这一行
            while  i<= rc:
                if matrix[mid_r][i] == target:
                    return True
                i +=1
            # recursively search 上半行和下半行
            return recursion(lr,mid_r-1,lc,rc,target) or recursion(mid_r+1,rr,lc,rc,target)
        return recursion(0,row-1,0,col-1,target)      
# ------------------------------------ 4 ---------------------------------------------------------
# Leetcode 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest
#  transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 思路： dfs，adj neigborhood list for median word 
# eg  hit -> *it, h*t, hi*
# {*it:hit, h*t: hit,hot....}
# import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = [beginWord]
        queue = []
        L = len(beginWord)
        queue = collections.deque([(beginWord, 1)])
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        while queue:
            curr, curr_level = queue.popleft()
            for i in range(L):
                poss_word = curr[:i] + "*" + curr[1+i:]
                for word in all_combo_dict[poss_word]:
                    if word == endWord:
                        return curr_level+1
                    if word not in visited:
                        visited.append(word)
                        queue.append((word,curr_level+1))
                all_combo_dict[poss_word] = []
        return 0
# ------------------------------------ 5 ---------------------------------------------------------
# Leetcode 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish 
# all courses?

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
class Solution:
    # METHOD 1: FOR EACH NODE, DETECT CYCLE -> keep visited stack and visit flag 
    # Exceed time limit 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {x:[] for x in range(numCourses)}
        in_list = {x:[] for x in range(numCourses)}
        for pre in prerequisites:
            key = pre[1]
            value = pre[0]
            adj_list[key].append(value)
            in_list[value].append(key)
        flag = [None for x in range(numCourses)]
        def has_cycle(curr,adj_list,visited):
            if curr in visited:
                flag[curr] = True
                return True
            if not adj_list[curr]:
                flag[curr] = False
                return False
            visited.append(curr)
            for nei in adj_list[curr]:
                if has_cycle(nei,adj_list,visited):
                    return True
            visited.remove(curr)
            flag[curr] = False
            return False
        count = 0
        for c in in_list:
            if flag[c]:
                return flag[c]
            else: 
                if has_cycle(c,adj_list,[]):
                    return False
        return True
    # METHOD 2:  结合flag和visited，三个状态的map
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {x:[] for x in range(numCourses)}
        for pre in prerequisites:
            key = pre[1]
            value = pre[0]
            adj_list[key].append(value)
        visited = [0 for i in range(numCourses)]
        # Color 3:
        # 0: not visited
        # 1 : being visted 
        # -1: done visited and no cycle 
        def dfs(curr,adj_list,visited):
            if visited[curr] == 1:
                return True
            if visited[curr] == -1:
                return False
            # Mark being visit
            visited[curr] = 1
            for nei in adj_list[curr]:
                if dfs(nei,adj_list,visited):
                    return True
            visited[curr] = -1
            return False
        for course in adj_list:
            if visited[course] != -1:
                if dfs(course,adj_list,visited):
                    return False
        return True
        # METHOD 3: TOPOLOFICAL SORT:
        # METHOD 3: TOPOLOGICAL SORT:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {x:[] for x in range(numCourses)}
        in_list = {x:[] for x in range(numCourses)}
        for pre in prerequisites:
            in_e = pre[0]
            out = pre[1]
            adj_list[out].append(in_e)
            in_list[in_e].append(out)
        res = []
        # put all node without incoming edges to the list
        queue = collections.deque([])
        for course in in_list:
            if len(in_list[course]) == 0:
                queue.append(course)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            # for nei in adj_list, remove curr from in_list
            for nei in adj_list[curr]:
                in_list[nei].remove(curr)
                if len(in_list[nei]) == 0:
                    queue.append(nei)
        # check if all node has no in_coming edges now, if so, no cycle
        for course in in_list:
            if len(in_list[course]) != 0:
                return False
        return True
# ------------------------------------ 6 ------------------------------------------------------- 
# Leetcode 92. Reverse Linked List II
# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.
# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL   
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        if m == n :
            return head
        # EDGE CASE, M == 1
        if m == 1:
            new_prev = dummy
            new_tail = head
        elif m >1:
            for i in range(m-2):
                if head.next:
                    head = head.next
                if not head.next:
                    return dummy.next
            new_prev = head
            new_tail = head.next
        curr = new_tail
        prev = ListNode(0)
        # 要记录三个点，prev curr next
        # 每次吧curr.next记录在next之后再断curr->next to prev <-curr  next 
        # prev = curr
        # curr = next 
        # 记录开始rev前的一个点，和最开始rev的一个点，用来最后链接
        for i in range(n-m+1):
             if curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next       
        new_prev.next = prev
        if new_tail.next:  
            new_tail.next = next
        return dummy.next               

# ------------------------------------ 7 ------------------------------------------------------- 
# Leetcode 27. Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
class Solution:
    # METHOD: 2 POINTERS
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n -1
        while left <= right:
            if nums[left]==val:
                nums[left],nums[right] = nums[right],nums[left]
                right -=1
            else:
                left +=1
        return left
# ------------------------------------ 8 ------------------------------------------------------- 
# Leetcode 382. Linked List Random Node
class Solution:
    # METHOD 1: 放到list，用python rand library
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.list = []
        while head:
            self.list.append(head.val)
            head = head.next
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = len(self.list)
        rand = random.randrange(n)
        return self.list[rand]
    # METHOD 2: Reservoir Sampling
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            # 1/k  select new, k-1/k select old, for old, each one is 1/k
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val
        
# ------------------------------------ 9 -------------------------------------------------------
# Leetcdoe 285. Inorder Successor in BST
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# The successor of a node p is the node with the smallest key greater than p.val.
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # METHOD 1: Inorder Traverse, get list -> traverse list 
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        path = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            path.append(root)
            if root.right:
                traverse(root.right)
        traverse(root)
        for i in range(len(path)):
            if path[i] == p:
                if i+1 < len(path):
                    return path[i+1]
                else:
                    return None
        return None
    # METHOD 2: DFS WITH 2 Global Vars
    # CHECK == BEFORE UPDATE PREV
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.prev = None
        self.res = None
        def recursion(root):
            if root.left:
                recursion(root.left)
            if self.prev == p:
                self.res = root   
            self.prev = root
            if root.right:
                recursion(root.right)
        recursion(root)
        return self.res
    # METHOD 3: Binary Search the smallest number larget than target node 
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        candidate = None 
        curr = root
        while curr:
            if curr.val > p.val:
                candidate = curr
                curr = curr.left
            else:
                curr = curr.right
        return candidate
# ------------------------------------ 10 ------------------------------------------------------- 
# Leetcode 678. Valid Parenthesis String
# Given a string containing only three types of characters: '(', ')' and '*', write a function 
# to check whether this string is valid. We define the validity of a string by these rules:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.        
# class Solution:
# METHOD: keep 2 stacks for open and star, durting the scan, if close: pop star or open
# after scan, make sure every open can have a start that comese later than open 
    def checkValidString(self, s: str) -> bool:
        open_stack = collections.deque([])
        star_stack = collections.deque([])
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append((s[i],i))
            if s[i] == '*':
                star_stack.append((s[i],i))
            if s[i] == ')':
                if not open_stack and not star_stack:
                    return False
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
        if not open_stack:
            return True
        if open_stack and not star_stack:
            return False 
        else: 
            while open_stack:
                if not star_stack:
                    return False
                else:
                    curr_open = open_stack.pop()
                    curr_star = star_stack.pop()
                    if curr_open[1] > curr_star[1]:
                        return False
        return True       
# ------------------------------------ 10 -------------------------------------------------------                
# 260. Single Number III
# Given an integer array nums, in which exactly two elements appear only once and all the other
#  elements appear exactly twice. Find the two elements that appear only once. You can return 
#  the answer in any order.

# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it 
# using only constant space complexity?
class Solution:
    # METHOD 1 HASHMAP
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        for k,v in counter.items():
            if v == 1:
                res.append(k)
        return res
    # BITMASK: 这真的想不出来，背一下吧
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0 
        for num in nums:
            bitmask = bitmask ^ num 
            
        diff = bitmask & (-bitmask+1)
        
        x = 0
        for num in nums:
            if num & diff:
                x= x^num
        return [x, bitmask^x]
# ------------------------------------ 11 -------------------------------------------------------                 
# Leetcode 937. Reorder Data in Log Files
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  
# It is guaranteed that each log has at least one word after its identifier.
# Reorder the logs so that all of the letter-logs come before any digit-log.  
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
# Return the final order of the logs.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)  
        # firsts sort by identifier 
        letters.sort(key = lambda x: x.split()[0]) 
        # then sort by words 
        letters.sort(key = lambda x: x.split()[1:])        
        result = letters + digits                                     
        return result
# ------------------------------------ 12 -------------------------------------------------------   
# Leetcode 692. Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, 
# then the word with the lower alphabetical order comes first.       
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.   
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        words = sorted(words,key = lambda x:x)
        for word in words:
            hashmap[word] = hashmap.get(word,0) + 1
        hashmap = sorted(hashmap.items(),key = lambda x:x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(hashmap[i][0])
        return res
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word       
# ------------------------------------ 13 -------------------------------------------------------                 
# Leetcode 1192. Critical Connections in a Network      
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections 
# forming a network where connections[i] = [a, b] represents a connection between servers a and b. 
# Any server can reach any other server directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# Return all critical connections in the network in any order.                
class Solution:
    # METHOD: GIVE EACH NODE A RANK,PASS THIS TO THE SUPER LOOP. 
    # IF WE SEE A NODE WITH A RANK SMALLER THAN MIN_PREV_RANK, WE KNOW THIS NODE HAS BEEN
    # SEEN, SO REMOVE (NODE,CURR) FROM THE COLLECTIONS
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # If has cycle -> not critical 
        # If no cycle -> critial
        adj_list = {x:[] for x in range(n)}
        for e in connections:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        # Three colors:
        # visited[i] = 0 : not seen i 
        # visited[i] = 1 : i in stack
        # visited[i] = -1: i done visit no cycle
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n
        def dfs(curr,depth):
            if rank[curr] >= 0:
                return rank[curr]
            rank = depth 
            min_back_depth = n
            for nei in adjlist[curr]:
                if rank[curr] == depth -1:
                    continue 
                prev_rank = dfs(nei,depth+1)
                if prev_rank <= min_back_depth:
                    connections.remove([curr,nei])
                    connections.remove([nei,curr])
                min_back_depth = min(min_back_depth, prev_rank)
            rank[curr] = n
            return min_back_depth
        dfs(0,0)
        return connections      
# ------------------------------------ 14 -------------------------------------------------------        
# Leetcode 57. Insert Interval
# Given a set of non-overlapping intervals, insert a new interval into the intervals 
# (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
class Solution:
    # METHOD: PUT INTO DEQUE AND POPLEFT, KEEP UPDATE OF CURR TO_MERGE 
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        res = []
        interval_deque = collections.deque(intervals)
        to_merge = newInterval #[2,5]
        while interval_deque:
            curr = interval_deque.popleft() #[1,3]
            if curr[0] > to_merge[1]:    # 1 > 5 no 
                res = res + [to_merge] + [curr] + list(interval_deque)
                return res
            else:   
                if curr[1] < to_merge[0]: # 3<2 not
                    res += [curr]
                else:
                    if curr[0] < to_merge[0]: # 1 < 2 yes 
                        to_merge[0] = curr[0]  
                    if curr[1] > to_merge[1]:
                        to_merge[1] = curr[1]
        if not res:
            return [newInterval]
        if res[-1][1] < to_merge[0]:
            return res + [to_merge]
# ------------------------------------ 15 -------------------------------------------------------
# Leetcode 3. Longest Substring Without Repeating Characters Sliding Window
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
class Solution:
    # MRTHOD1: Sliding window + hashmap // hashmap can be changed to stack
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = 0
        end = 1
        n = len(s)
        if not s:
            return 0
        if n == 1:
            return 1
        map[s[start]] = 0
        max_len = 0
        # map: [a:1], [b:1]
        # a b c c b c b b 
        # s     e
        # 0 1 2 3
        while end < n:
            # not seen in curr substring
            if s[end] not in map:
                map[s[end]] = end
                # move end to next 
                end +=1
                # update max length
                if len(map) > max_len:
                    max_len = len(map)
            # if seen in curr substring
            else:
                prev_ind = map[s[end]] 
                while start <= prev_ind:
                    del map[s[start]]
                    start +=1
        return max_len
# ------------------------------------ 16 -------------------------------------------------------              
# Leetcode 567. Permutation in String
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of 
# s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
class Solution:
    # METHOD: USE HASHMAP TO TRACK CURRENT LENGTH OF STRING EQUALS TO PERM OR NOT
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get perm -> have same char and each char should be same count
        perm_count = collections.Counter(s1)
        if len(s2) < len(s1):
            return False
        len_perm = len(s1)
        # have fixed length, since if we can find perm, the length must be len(s1)
        start = 0
        end = len_perm -1
        curr_map = collections.Counter(s2[start:end+1])
        
        while start < len(s2) - len_perm:
            if curr_map == perm_count:
                return True
            else:
                # remove the char start points to from curr dict
                curr_map[s2[start]] -= 1
                if curr_map[s2[start]] == 0:
                    del curr_map[s2[start]]
                start +=1
                end +=1
                curr_map[s2[end]] = curr_map.get(s2[end],0) + 1
        return curr_map == perm_count
# ------------------------------------ 17 -------------------------------------------------------         
# Leetcode 146. LRU Cache       
# ------------------------------------ 18 ------------------------------------------------------- 
# Leetcoce 33. Search in Rotated Sorted Array       
# You are given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] 
# might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.     
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1
        # 4 5 6 7 0 1 2
        # 0 1 2 3 4 5 6
        # s.    m.    e
        # mid = 3 -> 7
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]: # left not rotatetd
                # 2 situations: 
                # 1. target > start  and target < mid
                if target >= nums[start] and target <= nums[mid]:
                    # in left
                    end = mid -1
                else:
                    # check right
                    start = mid +1
            else:
                # right not rotated
                # if target > mid and target < end
                if target <= nums[end] and target >= nums[mid]:
                    # go right
                    start = mid+1
                    # check left
                else:
                    end = mid -1
        return -1
                   
                        
                    
            
        
        

            
        
                
                
            
        
        

            
    
        
