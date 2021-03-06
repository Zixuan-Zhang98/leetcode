'''
https://leetcode.com/problems/shuffle-an-array/discuss/85958/First-Accepted-Solution-Java
I saw some people asking why this algorithm is correct. Here is my understanding. Hope it helps.

Proof: Suppose this algorithm works, i.e. for each position j (starting from 0), the probability of any number in the range[0,j] to be at position j is 1/(1+j).

Let's look at int i = random.nextInt(j + 1):
(1) If i == j, nums[j] does not need to change its position, which has probability 1/(1+j).
(2) if i !=j, nums[j] needs to be swapped with nums[i]. The probability of any number x in the range [0,j-1] to be at position j = nums[j] changes its position * x is at position i
= (1-1/(1+j)) * (1/j) = 1/(1+j)

Each number has equal probability to be at any position.
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        rand, n = self.nums[:], len(self.nums)
        for i in range(n):
            j = random.randint(0, i)
            rand[i], rand[j] = rand[j], rand[i]
        return rand
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()