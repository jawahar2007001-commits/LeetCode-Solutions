class Solution(object):
    def addStrings(self, num1, num2):
        res=[]
        carry=0
        p1=len(num1)-1
        p2=len(num2)-1
        while p1>=0 or p2>=0 or carry:
            if p1>=0:
                d1=ord(num1[p1])-ord('0')
            else:
                d1=0
            if p2>=0:
                d2=ord(num2[p2])-ord('0')
            else:
                d2=0
            colsum=d1+d2+carry
            carry=colsum//10
            res.append(str(colsum % 10))
            p1-=1
            p2-=1
        return ''.join(reversed(res))

        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        