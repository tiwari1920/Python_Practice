class Test:
    def add(self,*nums):
        print(sum(nums))
t1 = Test()
t1.add(10,20)
t1.add(100,200,300)
