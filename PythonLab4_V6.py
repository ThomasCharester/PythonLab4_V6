class String:
    myString = list()
    def Concat(self,strToConcat):
        self.myString.extend(strToConcat)
    def Set(self, strToSet):
        self.myString = list(strToSet)
    def Clear(self):
        self.myString = list()
    def IndexOf(self, substring):
        startPos = 0
        flag = False
        for i in range(len(self.myString)):
            if flag and len(substring) <= i - startPos :
                return i
            if self.myString[i] == substring[0] and not flag:
                startPos = i
                flag = True
            elif flag and self.myString[i] != substring[i-startPos]:
                startPos = 0
                flag = False
        return -1
    def _eq_(self,strToSet):
        self.myString = list(strToSet)
    def Reverse(self):
        temp = ''
        for i in range(1,len(self.myString) + 1):
            temp += self.myString[-i]
        self.myString = list(temp)


s = String()

s.Set('WASDWASD')

s.Clear()

s.Concat('QWERTYUIOP')

s.IndexOf('YUI')

s.Reverse()

s.Clear()
            
