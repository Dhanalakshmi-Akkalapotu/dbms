'''class person:
    def __init__(self,fullname):
        #print("hello,i'm {}!".format(name))
        #print(self)
        self.name=fullname
    def say_hello(self):
       # print('hello')
        print'''
class car:
    def __init__(self,color,acceleration,cost):
        self.color=color
        self.acceleration=acceleration
        self.speed=0
        self.cost=10,000
    def accelerate(self):
        print('speeding up!')
        self.speed+=self.acceleration
    def apply_brakes(self):
        print('applying brakes!')
        self.speed-=10