# https://leetcode.com/problems/unique-number-of-occurrences/


class Solution(object):
    def uniqueOccurrences(self, arr):
        hashMap = {}

        # Count occurrences of each element in arr
        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        hashSet = set()
        flag = True

        # Check if there are unique occurrences
        for count in hashMap.values():
            if count in hashSet:
                flag = False
                break
            else:
                hashSet.add(count)

        return flag