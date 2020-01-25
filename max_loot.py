
class Solution(object):
    
    def __init__(self):
        self.max_sum=[]
        
        
    def lootSum(self,nums):
        num_len=len(nums)
        self.max_sum=[None]*num_len

	if len(nums) >0:
		self.max_sum[0]=nums[0]
	if len(nums) >1:
		self.max_sum[1]=max(nums[0], nums[1])

	for k in range(2, len(nums)):
		self.max_sum[k]=max(self.max_sum[k-2]+nums[k], self.max_sum[k-1])

	print self.max_sum
    
	if len(self.max_sum) >0:
		    return self.max_sum[-1]
	else:
		return 0 


    def rob(self, nums):
        ans=self.lootSum(nums)
	return ans



s=Solution()

s.rob([2,7,9,3,1])


		
