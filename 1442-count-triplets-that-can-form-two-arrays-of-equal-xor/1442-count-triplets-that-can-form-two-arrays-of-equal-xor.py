class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        prefix= 0
        prev_xor_cnt, prev_xor_idx_sum = defaultdict(int), defaultdict(int)
        prev_xor_cnt[0] = 1
        
        for i in range(n):
            prefix ^= arr[i]
            
            if prev_xor_cnt[prefix]:
                out += i * prev_xor_cnt[prefix] - prev_xor_idx_sum[prefix]
            prev_xor_cnt[prefix] += 1
            prev_xor_idx_sum[prefix] += i+1
        return out
            
        
        # for i in range(n):
        #     a = 0
        #     for j in range(i+1, n+1):
        #         a ^= arr[j-1]
        #         b = 0
        #         for k in range(j, n+1):
        #             b ^= arr[k]
        #             if a == b:
        #                 out+=1
        # return out
#         for i in range(n):
#             a = arr[i]
#             for j in range(i+1, n+1):
#                 a ^= arr[j]
#                 if a == 0:
#                     out+=j-1
#         return out
        
        