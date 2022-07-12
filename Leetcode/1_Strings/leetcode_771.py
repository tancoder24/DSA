class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([x for x in stones if x in jewels] )

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(i in J for i in S)

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(S.count(i) for i in J)

from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(Counter(S)[i] for i in J)