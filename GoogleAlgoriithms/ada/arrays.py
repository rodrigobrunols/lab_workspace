import bisect


array = [0,8,2,3,1,5,6,3,8,9]
array.sort()
# idx = bisect.bisect_left(array,12)
bisect.insort(array,3)
# print(idx)
print(array)

# class Test:
#
#     def __init__(self):
#         self.array = [1,2,3,4,5,6,7,8,9]
#
#     def insert_in_order(self, num):
#         bisect.insort(self.array, num)
#
#     def print_array(self):
#         print(self.array)
#
#
# dummy = Test()
#
# dummy.print_array()
# dummy.insert_in_order(3)
# dummy.print_array()


class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        max_ = 0
        start = 0

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start += 1

            max_ = max(max_ , end - start + 1)

        return max_
