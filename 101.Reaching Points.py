# Tag: Backtracking with special thinking
# 780. Reaching Points
# -----------------------------------------------------------------------------------
# Description: 
# A move consists of taking a point (x, y) and transforming it to 
# either (x, x+y) or (x+y, y).

# Given a starting point (sx, sy) and a target point (tx, ty), return True if and 
# only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). 
# Otherwise, return False.
# -----------------------------------------------------------------------------------
# Note:

# sx, sy, tx, ty will all be integers in the range [1, 10^9].
# -----------------------------------------------------------------------------------
# # Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)

# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False

# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 从下往上，backtrack
# since : sx, sy, tx, ty will all be integers in the range [1, 10^9]
# For the 2 pahts we might face from 
# (x',y') -> (x', x'+y') 
#            (tx, ty)
# (tx,ty-tx) <-  if ty>tx
# (x',y') -> (x'+y', y') 
#            (tx, ty)
# (tx-ty,ty) <-  if tx>ty
# Since this is a hard question, use:
# while tx>ty:
#   tx = tx -ty
# will exceed time limit: 
# so use:  tx %= ty
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while (tx >= sx and ty >= sy):
            if tx == ty:
                break 
            elif tx > ty:
                if ty>sy:
                    tx= tx %ty
                 # if ty == sy: early return, only change tx is fine 
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                 # if tx == sx: early return, only change ty is fine
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy