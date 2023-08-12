class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Quickly deduce anything that is not an anagram
        if len(s) != len(t):
            return False
        
        # I think we should use a dictionary and not a set, since you need to know the frequency of each letter in the words
        # Question: Can you use a boolean operator on two dictionaries to compare if they are the same? I'll try this
        s_dict, t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        
        if s_dict == t_dict:
            return True
        return False

        # Answer: Yes, you can compare two dictionaries in a boolean operator to check if they are the exact same. 


        # NeetCode Solution:
        f len(s) != len(t):
            return False

        countS, countT = {} # Initialize multiple variables at once

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #countS is a dict, the get function gets the value or defaults it to 0
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT
