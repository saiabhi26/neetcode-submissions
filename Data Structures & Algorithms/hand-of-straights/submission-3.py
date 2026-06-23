class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        d = defaultdict(int)
        hand.sort()
        for i in range(len(hand)):
            num = hand[i]
            d[num]+=1
        

        for num in hand:
            if d[num] > 0:
                for i in range(num,num+groupSize):
                    if d[i] == 0:
                        return False
                    d[i]-=1
        return True
            
        
