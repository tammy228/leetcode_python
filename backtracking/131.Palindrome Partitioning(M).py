from typing import List
"""
My Solution

in order to get [a,a,b], [aa, b], we need to think every iteration how to split the word ex:"abcdefg", it could split in "a,bcedfg", "ab,cedfg", "abc,edfg"...
for the left side we need to check if it's palindrome, and for the right side we use same logic to do split the word
for complete answer, it should be all left word match palindrome and the index reach to the end

check
is there gonna be non-char ex: ,:{}

ex: "aab"
"a"             "aa"   "aab"(X)
"a", "ab"(X)    "b"
"b"

Time:
O(N * 2^N): length N word has N-1 partitiong space, each space we can choose or not choose-> 2^N, for eaceh node st ==st[::-1](O(N)), path[:] O(N)

Space:
auxiliary: path , st[::-1](the length could various therfore don't count) , stack = O(N)+ worst O(N) = O(N)

"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def backtracking(start, path):
            if start == len(s):
                ans.append(path[:])
                return
            for end in range(start, len(s)):
                st = s[start:end+1]
                if st == st[::-1]:
                    path.append(st)
                    backtracking(end+1, path)
                    path.pop()
        backtracking(0, path)
        return ans
            