from typing import List
from collections import defaultdict
class Solution:
    def convertTime(self, st: str):
        hour_st = st[0:2]
        min_st = st[3:5]
        
        hour_int = int(hour_st) if hour_st[0] != "0" else int(hour_st[1])
        min_int = int(min_st) if min_st[0] != "0" else int(min_st[1])
        return hour_int * 100 + min_int
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_time = defaultdict(list)
        ans = []
        for name, time in zip(keyName, keyTime):
            name_time[name].append(self.convertTime(time))

        for key, value in name_time.items():
            value.sort()
            for i in range(len(value)-2):
                if value[i+2] - value[i] <= 100:
                    ans.append(key)
                    break
        ans.sort()
        return ans
                         
        