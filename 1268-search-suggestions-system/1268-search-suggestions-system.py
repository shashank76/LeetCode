class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        out =[]
        products.sort()
        l, r = 0, len(products)-1
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l<=r and (len(products[l]) <= i or (products[l][i] != c)):
                l+=1
            
            while l<=r and (len(products[r]) <= i or (products[r][i] != c)):
                r-=1
            n = r-l+1
            out.append([])
            for j in range(min(3, n)):
                out[-1].append(products[l+j])
        return out