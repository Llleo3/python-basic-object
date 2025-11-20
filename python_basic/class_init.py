class Calculator:
    def __init__ (self,name,price):
        self.name=name
        self.price=price
    def add(self,x,y):
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)