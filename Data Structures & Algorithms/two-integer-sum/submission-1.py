class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic = {}
        for i,n in enumerate((nums)):
            complement = target - n
            if (complement in myDic):
                return [myDic[complement], i]
            else:
                myDic[n] = i
        print (myDic)