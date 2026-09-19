class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sd = {}
        

        for ch in s:
            sd[ch] = sd.get(ch, 0) +1
        for ch in t:
            if ch not in sd or sd[ch] == 0:
                return False
            sd[ch] -= 1
            
        return True