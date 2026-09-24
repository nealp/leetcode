class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        d = k
        stack = []
        for dig in num:
            while stack and dig < stack[-1] and d != 0:
                smaller = stack.pop()
                d -= 1
   
        # x is the next greater element for smaller
            stack.append(dig)

        while d != 0 and stack:
            stack.pop()
            d -= 1
        
        while stack and stack[0] == "0":
            stack.pop(0)
    

        if not stack:
            stack.append("0")
        result = "".join(stack)

        return result

    



 
  





