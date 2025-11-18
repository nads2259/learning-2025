class Iterator:
    
    def __init__(self,data):
        self.data = data
        
    def __iter__(self):
        self.index = 0
        return self
        
    def __next__(self):
        
        if (self.index >= len(self.data)):
            raise StopIteration
        else:
            num = self.data[self.index]
            self.index += 1
            return num
        
        
my_list = Iterator([1,2,3,4,5])

for i in my_list:
    print(i)