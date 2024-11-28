class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for x in range(len(operations)):
            if operations[x] == '+':
                l.append(l[-1]+l[-2])
            elif operations[x] == 'D':
                l.append(2*l[-1])
            elif operations[x] == 'C':
                l.pop()
            else:
                l.append(int(operations[x]))
        return sum(l)
            
            
