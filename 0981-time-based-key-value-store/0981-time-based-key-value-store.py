class TimeMap:

    def __init__(self):
        self.dictVals = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictVals:
            self.dictVals[key] = [[value, timestamp]]
        else:
            self.dictVals[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        out = ""
        vals = self.dictVals.get(key, [])
        i, j = 0, len(vals) - 1
        while i <= j:
            m = (i+j) // 2
            if vals[m][1] <= timestamp:
                out = vals[m][0]
                i = m+1
            else:
                j = m-1
        return out
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)