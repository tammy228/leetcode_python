"""
My Solution

check
will there be no beginWord or endWord in the wordList
duplicate word?
UppperLetter or LowerLetter only?
beginWord == endWord?
word length?
len(beginWord) == len(endWord)?

word is related is there is one char different, if we need to transform from beginWord-> endWord, we need to see if there is possible combinations
we can connected the word is there is only one char different, after connectting all tthe word, if there is path between beginWord-> endWord means there is solutions
to get the minimum transformation we can use bfs to traverse the graph

for construct graph we can use wildcard bucket to do the search
# {
#   # wildcard_bucket
#   '*ot': ['hot', 'dot', 'lot'],
#   'h*t': ['hot'],
#   'ho*': ['hot'],
#   'd*t': ['dot'],
#   'do*': ['dot', 'dog'],  <-- dot 和 dog 都認領了 do*
#   ... 
# }

ex:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

Time:
bucket, 
"""
from typing import List
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or len(beginWord) != len(endWord) or endWord not in wordList: return 0
        wildcard_bucket = defaultdict(list)
        L = len(wordList[0])
        q = deque([beginWord])
        ans = 0
        visited = set()


        for word in wordList:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                wildcard_bucket[key].append(word)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans + 1
                if word not in visited:
                    visited.add(word)
                    for i in range(L):
                        key = word[:i] + "*" + word[i+1:]
                        for nei in wildcard_bucket[key]:
                            if nei != word:
                                q.append(nei)
            ans += 1
        return 0
"""
Optimize

move visited.add() right after append into queue, otherwise queue will have a lot of duplicate words
there will only be blocked when they pop out

change wordList to wordSet can use it for checking and avoid duplicate words and replace visited


Time:
init bucket = O(NL^2), L^2 for each word slice L times and each times use slicing takes another L
queue = O(NL^2) 
total = O(NL^2)

Space:
bucket = O(NL^2), NL for total key count, each key maximum L length
init wordset = O(NL)
queue = O(N)
total = O(NL^2)

"""

class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList) # change to set can make search to O(1), if there is a lot of search we need to change to set
        if beginWord == endWord or len(beginWord) != len(endWord) or endWord not in wordSet: return 0
        wildcard_bucket = defaultdict(list)
        L = len(wordList[0])
        q = deque([beginWord])
        ans = 1  # beginWord also count

        if beginWord in wordSet:
            wordSet.remove(beginWord)

        for word in wordSet:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                wildcard_bucket[key].append(word)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                
                for i in range(L):
                    key = word[:i] + "*" + word[i+1:]
                    for nei in wildcard_bucket[key]:
                        if nei in wordSet:
                            q.append(nei)
                            wordSet.remove(nei)
            ans += 1
        return 0
                
"""
Optimize 2

bidirection bfs

Time: O(N * L^2)                                                                             
- Preprocessing wildcard_bucket: O(N * L^2)                                                  
- Bidirectional search: O(N * L^2) in worst case, but much faster in practice.               

Space: O(N * L^2)                                                                            
- wildcard_bucket: O(N * L^2)                                                                
- begin/end sets and visited: O(N * L)

"""
class Solution3:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: 
            return 0
        
        wordSet.add(beginWord)
        
        # Build wildcard buckets (e.g., "hot" -> "*ot", "h*t", "ho*") to optimize graph building to O(NL)
        wildcard_bucket = defaultdict(list)
        L = len(beginWord)
        for word in wordSet:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                wildcard_bucket[key].append(word)
                
        begin_set = {beginWord}
        end_set = {endWord}
        visited = {beginWord, endWord}
        ans = 1  

        while begin_set and end_set:
            # Core optimization: Always expand the smaller frontier to minimize search space
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_level_set = set()
            
            for word in begin_set:
                for i in range(L):
                    key = word[:i] + "*" + word[i+1:]
                    for nei in wildcard_bucket[key]:
                        
                        # Early intercept: The paths from both ends have successfully met
                        if nei in end_set:
                            return ans + 1
                        
                        if nei not in visited:
                            visited.add(nei)
                            next_level_set.add(nei)
                            
            begin_set = next_level_set
            ans += 1  
            
        return 0
