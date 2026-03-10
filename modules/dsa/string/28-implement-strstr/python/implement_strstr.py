class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        lps = self._build_lps(needle)
        needle_index = 0

        for haystack_index, char in enumerate(haystack):
            while needle_index > 0 and char != needle[needle_index]:
                needle_index = lps[needle_index - 1]

            if char == needle[needle_index]:
                needle_index += 1
                if needle_index == len(needle):
                    return haystack_index - needle_index + 1

        return -1

    def _build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)
        prefix_length = 0

        # lps[i] stores the longest proper prefix that is also a suffix for pattern[: i + 1].
        for index in range(1, len(pattern)):
            while prefix_length > 0 and pattern[index] != pattern[prefix_length]:
                prefix_length = lps[prefix_length - 1]

            if pattern[index] == pattern[prefix_length]:
                prefix_length += 1
                lps[index] = prefix_length

        return lps
