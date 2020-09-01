# Tag:  String Manipulation
# 819. Most Common Word
# -----------------------------------------------------------------------------------
# Description: 

# Given a paragraph and a list of banned words, return the most frequent word that is 
# not in the list of banned words.  It is guaranteed there is at least one word that 
# isn't banned, and that the answer is unique.

# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive.  The answer is in lowercase.
# -----------------------------------------------------------------------------------
# Example:

# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# isalnum()！！！！！判断是不是a to z
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap ={}
        n = len(paragraph)
        temp = ""
        for char in paragraph:
            if char == " " or char.lower()>'z' or char.lower()<'a':
                if temp != "":
                    if temp in hashmap:
                        hashmap[temp] +=1
                    else:
                        hashmap[temp] = 1
                    temp = ""
            else:
                temp += char.lower()
        if temp:
            if temp in hashmap:
                hashmap[temp] +=1
            else:
                hashmap[temp] = 1
            
        max = 0
        res = ""
        for key,value in hashmap.items():
            if key not in banned and value >max:
                max = value
                res = key
        if not res and paragraph:
            return paragraph.lower()
        return res
        