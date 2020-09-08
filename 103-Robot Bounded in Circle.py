# Tag: sepcial thinking
# 1041. Robot Bounded In Circle
# -----------------------------------------------------------------------------------
# Description: 

# On an infinite plane, a robot initially stands at (0, 0) and faces north.  
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot 
# never leaves the circle.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.
# Example 3:

# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
# -----------------------------------------------------------------------------------
# Note:

# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 独特思路，如果一个circle后机器人在原位（0，0） 或者没有face north-> will circle
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 设置方向函数：d = [0 N,1 W,2 S,3 E]
        # use (d+1) % 4 to know next direction 
        # if l -> d +=1
        # if r -> d -=1
        # always reset to 4 when d is 0
        # init facing north 
        d = 4
        moves = [1,-1,-1,1]
        # if d = 0: y+1
        # if d = 1: x -1
        # if d = 2: y-1
        # if d = 3 : x+1
        x = 0
        y = 0
        for char in instructions:
            if d <= 0:
                d +=4
            if char == "G":
                curr_move = d % 4
                if curr_move % 2 == 0:
                    y +=moves[curr_move]
                else:
                    x +=moves[curr_move]
            if char == "L":
                d +=1
            if char == "R":
                d -=1
        if (x ==0 and y == 0 )or d % 4 !=0:
            return True
        else:
            return False
                