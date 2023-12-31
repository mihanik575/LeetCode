# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current = arr[0]
        win_count = 0
        for i in range(1, len(arr)):
            if arr[i] > current:
                current = arr[i]
                win_count = 1
            else:
                win_count += 1
            if win_count == k:
                break
        return current