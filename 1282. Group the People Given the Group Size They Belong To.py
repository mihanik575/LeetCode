# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/


import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        groups, result = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result