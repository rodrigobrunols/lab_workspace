

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
