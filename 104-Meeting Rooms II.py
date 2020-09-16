# Tag: Heapq
# 253. Meeting Rooms II
# -----------------------------------------------------------------------------------
# Description: 

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],
# [s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# -----------------------------------------------------------------------------------
# Examples:

# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Condition to be overlapped: 
# interval[i]'s' start time smaller than the smallerst end time of all rooms from previous steps
# ** Pre-condition: sort intervals by start time 
# (1) For i in intercals: 
# **if start_time of intervals[i] > h[0] (samllerst end time, head of the heapq):
#  Can fit in same room 
# heapq -> pop h[0] -> heapqpush i[start_time]
# ** else:
# heapq -> heappush i[start_time]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Define heap as h = []
        heap =[]
        intervals.sort()
        for interval in intervals:
            # need a new meeting room
            if not heap or heap[0] >interval[0]:
                heapq.heappush(heap,interval[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,interval[1])
        return len(heap)
        