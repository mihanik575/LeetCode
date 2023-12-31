# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


import collections
import string

class Solution(object):
    def minDeletions(self, s):
        count = collections.Counter(s)
        result = 0
        lookup = set()
        for c in string.ascii_lowercase:
            for i in reversed(range(1, count[c]+1)):
                if i not in lookup:
                    lookup.add(i)
                    break
                result += 1
        return result