class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        oncedigitDict = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }
        
        tensdigitDict ={
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }
        
        def getEngWord(x):
            word = []
            hundDig = x // 100
            if hundDig:
                word.append(oncedigitDict[hundDig] + ' Hundred')
            tenDig = x % 100
            if tenDig >= 20:
                tens, once = tenDig//10, tenDig%10
                word.append(tensdigitDict[tens*10])
                if once:
                    word.append(oncedigitDict[once])
            elif tenDig:
                word.append(oncedigitDict[tenDig])
            return " ".join(word)
                    
            
        digitDict =['', ' Thousand', ' Million', ' Billion']
        i = 0
        out = []
        while num:
            digits = num % 1000
            w = getEngWord(digits)
            if w:
                out.append(w + digitDict[i])
            num = num // 1000
            i+=1
        out.reverse()
        return " ".join(out)
            