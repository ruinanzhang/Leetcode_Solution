# Tag:STRING
# 929. Unique Email Addresses
# -----------------------------------------------------------------------------------
# Description:
# Every email consists of a local name and a domain name, separated by the @ sign.
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# If you add periods ('.') between some characters in the local name part of an email address, 
# mail sent there will be forwarded to the same address without dots in the local name.  
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  
# (Note that this rule does not apply for domain names.)
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored.
# s allows certain emails to be filtered, for example m.y+name@email.com will be
# forwarded to my@email.com.  (Again, this rule does not apply for domain names.)
# It is possible to use both of these rules at the same time.
# Given a list of emails, we send one email to each address in the list. 
#  How many different addresses actually receive mails? 
# -----------------------------------------------------------------------------------
# Example:
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 基本思路很简单，就是要熟悉一下string在python里的operation：
# 1.if a char in string: -> if 'c' in string:
# 2.index of a char: -> str.index('c')
# 3.split string by a char: ->  a,b = str.split('c')
# 4.用set add item，只会add unique的，所以找unique第一时间想set
# 5.string貌似不能inline adjust，必须放到一个新的string里！！！！！
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # 想找unique elemnts -> put into set()!!!!
        unique = set()
        for email in emails:
            at_ind = email.index('@')
            local = email[:at_ind]
            domain = email[at_ind+1:]
            if '.' in local:
                local = local.replace('.','')
            if '+' in local:
                p_ind = local.index('+')
                local = local[:p_ind]
            unique.add(local+'@'+domain)
        return len(unique)
