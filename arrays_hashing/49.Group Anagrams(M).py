from typing import List
from collections import defaultdict

"""
My Solution

while iterating the list, use a dict to store sorted str as key, a
nd if you can find the key add the origin str to the value
else create key and add the value

Time:
O(N* mlogm), where N is len(strs) m is the length of str

Space:
O(Nm)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_str = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in dict_str:
                dict_str[sorted_str] = dict_str.get(sorted_str, [string])
            else:
                dict_str[sorted_str].append(string)
        return [value for _, value in dict_str.items()]
            

"""
Optimize

More pythonic style
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())