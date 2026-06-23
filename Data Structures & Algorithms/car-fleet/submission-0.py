class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]
        position.sort(reverse = True)
        stack = []
        for i in position:
            rt = (target-i)/d[i]
            if len(stack) == 0 or rt > stack[-1]:
                stack.append(rt)
        return len(stack)
                