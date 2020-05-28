# Tag : Binary Search Tree
# 504. Closest Number In Binary Search Tree II
# -----------------------------------------------------------------------------------
# Description:
# In a binary search tree, find k nodes containing the closest numbers 
# to the given target number. return them in sorted array
# -----------------------------------------------------------------------------------
# Assumptions:
# The given root is not null.
# There are no duplicate keys in the binary search tree.
# -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# !!!!我的思路是先recursive in-order traverse and then return the sorted list
#  Then find the crossover point -> get 2 pointers (left and right), and then return the target
# list going thru the whole list and then binary search (这也太复杂了肯定有更简单的解法。。目前是 N + LogN)
class Solution(object):
  def closestKValues(self, root, target, k):
    """
    input: TreeNode root, double target, int k
    return: int[]
    """   
    list_res = []
    list_res = Solution. inorder(root,target,list_res)
    llength = len(list_res)
    if target >=  list_res[llength -1]:
      return list_res[llength - k : llength]
    if target <= list_res[0]:
      return list_res[0:k]
    # return list_res
    
    # after returnning the in-order traverse list of the tree node values
    # we need to find the crossover point which is the closest num to the target:
    # Use binary search: 
    low = 0
    high = llength - 1
    # Here Binary Search return the index of cross_over point
    ind_cross_over = binary_search(list_res,low,high,target)
    res = []

    # return ind_cross_over

    if not ind_cross_over:
      res.append(root.val)
      return res
    
    if list_res[ind_cross_over] >= target: 
      right = ind_cross_over
      left = ind_cross_over - 1
    if list_res[ind_cross_over] < target:
      left = ind_cross_over
      right = ind_cross_over - 1
    
    res = []
    while len(res) < k :
      if  get_diff(list_res[right],target) < get_diff(list_res[left],target):
        res.append(list_res[right])
        if list_res[right + 1]: 
          right = right + 1
        else: 
          res.append(list_res[(left + 1 - k + len(res)):left + 1])
      else : 
        res.append(list_res[left])
        if list_res[left - 1]: 
          left = left - 1
        else: 
          res.append(list_res[right:(right + k - len(res))])
    
    mergeSort(res)
    return res

    # write your solution here
  
  def inorder(root,target,list_res):
    if root.left:
      Solution.inorder(root.left,target,list_res)
    list_res.append(root.val)
    if root.right:
      Solution.inorder(root.right,target,list_res)
    return list_res
    

def get_diff(val,target):
  return abs(val-target)


def binary_search(res_list,low,high,target):
  mid = low + ((high - low)//2 )
  if res_list[mid] >=target:
    if res_list[mid -1] < target:
      return mid
    if res_list[mid -1] == target:
      return (mid - 1)
    else:
        return binary_search(res_list,low,mid,target)

  if res_list[mid] <= target:
    if res_list[mid +1] > target:
      return mid
    if res_list[mid +1] == target:
      return mid+1
  
    else: 
      binary_search(res_list,mid,high,target)
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1