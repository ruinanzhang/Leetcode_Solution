// # Tag: BST
// # 220. Contains Duplicate III
// # -----------------------------------------------------------------------------------
// # Description:
// # Given an array of integers, find out whether there are two distinct indices i and j 
// # in the array such that the absolute difference between nums[i] and nums[j] is at most 
// # t and the absolute difference between i and j is at most k.
// # -----------------------------------------------------------------------------------
// # Example 1:
// # Input: nums = [1,2,3,1], k = 3, t = 0
// # Output: true
// # Example 2:

// # Input: nums = [1,0,1,1], k = 1, t = 2
// # Output: true
// # Example 3:

// # Input: nums = [1,5,9,1,5,9], k = 2, t = 3
// # Output: false
// # -----------------------------------------------------------------------------------
// # Constraints:
// # 0 <= nums.length <= 2 * 104
// # -231 <= nums[i] <= 231 - 1
// # 0 <= k <= 104
// # 0 <= t <= 231 - 1
// # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// # 思路: BST
// # for i in range(len(nums)):
// #   if len(BST) > k:
// #       BST.delete(oddest elment: nums[i-k+1])
// #   BST.insert(nums[i])
// #   BST.search if samllest in BST is greater than nums[i] - t or largest in BST is smaller than nums[i]+t
// #   if so, return T
// # *** Time Comp: nlogk
// # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    TreeSet<Integer> set = new TreeSet<>();
    for (int i = 0; i < nums.length; ++i) {
        // Find the successor of current element
        Integer s = set.ceiling(nums[i]);
        if (s != null && s <= nums[i] + t) return true;

        // Find the predecessor of current element
        Integer g = set.floor(nums[i]);
        if (g != null && nums[i] <= g + t) return true;

        set.add(nums[i]);
        if (set.size() > k) {
            set.remove(nums[i - k]);
        }
    }
    return false;
}
}
