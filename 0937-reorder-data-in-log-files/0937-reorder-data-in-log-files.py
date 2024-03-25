class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log1, log2 = [], []
        
        for log in logs:
            if log.split(' ')[1].isdigit():
                log1.append(log)
            else: 
                log2.append(log.split(' '))
        log2.sort(key= lambda x : x[0])
        log2.sort(key= lambda x : x[1:])

        for i in range(len(log2)):
            log2[i] = " ".join(log2[i])
        log2.extend(log1)
        return log2
        