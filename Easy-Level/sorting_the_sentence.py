class Solution(object):
    
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        
        l1 = sorted(l,key=lambda count:int(count[-1]))
        l1 = [x[:-1] for x in l1]
        
        return " ".join(l1)
