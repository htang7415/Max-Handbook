class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False

        lps = [0] * len(s)
        prefix_length = 0

        # lps[i] tracks the longest proper prefix of s[: i + 1] that is also a suffix.
        for index in range(1, len(s)):
            while prefix_length > 0 and s[index] != s[prefix_length]:
                prefix_length = lps[prefix_length - 1]

            if s[index] == s[prefix_length]:
                prefix_length += 1
                lps[index] = prefix_length

        longest_prefix_suffix = lps[-1]
        return longest_prefix_suffix > 0 and len(s) % (len(s) - longest_prefix_suffix) == 0
