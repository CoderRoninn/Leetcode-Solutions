class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)

        return sum(stone in set_jewels for stone in stones)

        