class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        groups = []
        visited=set()
        cache={}
        def helper(n, g):
            if n not in g:
                return 1
            if n in cache:
                return cache[n]
            skip = helper(n+k, g)
            include = (2**g[n]-1) * helper(n+2*k, g)
            cache[n] = skip + include
            return skip + include
            
        for n in counter.keys():
            if n in visited:
                continue
            grp={}
            while n-k in counter:
                n-=k
            while n in counter:
                grp[n] = counter[n]
                visited.add(n)
                n += k
            groups.append(grp)
        
        out = 1
        for grp in groups:
            n = min(grp.keys())
            out *= helper(n, grp)
        return out -1
            
            
        
#         def helper(i, count):
#             if i == len(nums):
#                 return 1
            
#             out = helper(i+1, count)
            
#             if not count[nums[i] + k] and not count[nums[i] -k]:
#                 count[nums[i]] += 1
#                 out += helper(i+1, count)
#                 count[nums[i]] -= 1
#             return out
        
#         return helper(0, defaultdict(int)) - 1
        