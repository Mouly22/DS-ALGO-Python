class HashTable:
    def __init__(self, inp):
        scount = 0
        wcount = 0
        for p in inp:
            inp1 = ord(p)
            if inp1 >= 65 and inp1 <= 90:
                if inp1 != 65 and inp1 != 69 and inp1 != 73 and inp1 != 79 and inp1 != 89:
                    scount += 1
                    #print(p)
            else:
                if inp1 >= 48 and inp1 <= 57:
                    wcount += inp1
        self.idx = (scount * 24 + wcount) % 9
        
    def hashing(self):
        hash_tbl = [None] * 9
        for i in range(len(hash_tbl)):
            if self.idx == i:
                if hash_tbl[i] != None:
                    i = (i+1)%9
                else:
                    hash_tbl[i] = inp
                    return hash_tbl
                    
    
        
inp = 'ST1E89B8A32'
a1 = HashTable(inp)
print(a1.hashing())