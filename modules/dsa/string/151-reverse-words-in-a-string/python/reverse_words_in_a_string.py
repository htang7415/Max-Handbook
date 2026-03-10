class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        length = self._compact_spaces(chars)
        chars = chars[:length]
        self._reverse(chars, 0, len(chars) - 1)

        word_start = 0
        for index in range(len(chars) + 1):
            if index == len(chars) or chars[index] == " ":
                self._reverse(chars, word_start, index - 1)
                word_start = index + 1

        return "".join(chars)

    def _compact_spaces(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            while read < n and chars[read] == " ":
                read += 1

            while read < n and chars[read] != " ":
                chars[write] = chars[read]
                write += 1
                read += 1

            while read < n and chars[read] == " ":
                read += 1

            if read < n:
                chars[write] = " "
                write += 1

        return write

    def _reverse(self, chars: list[str], left: int, right: int) -> None:
        # Reverse the whole string first, then reverse each word in place.
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
