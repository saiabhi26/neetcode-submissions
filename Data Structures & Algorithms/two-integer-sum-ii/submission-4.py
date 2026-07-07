class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num in hmap and hmap[target - num] != i:
                return [hmap[target - num] + 1, i + 1]
            hmap[num] = i
            
        