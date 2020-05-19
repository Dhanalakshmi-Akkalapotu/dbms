# radius=4
# pi=3.14
# perimeter=2*pi*radius
# print(perimeter)
# area=pi*(radius**2)
# print(area)
# a='hello'
# print(type(a),a,len(a))
# print("hello","hai", end="-")
# print('world')
# print('red','pony',8,sep="*")
# a= float(input())
# print(a)
# print(type(a))
# if 2<a<90:
#     b=8
#     print("b:",b)
# else:    
#     if 78<a<200:
#         b=200
#     else:
#         b=500
#         print("b:",b)
# print(str(a)+ ' dhana') 
n=int(input())
i=1
while n>=i:
        print(i,end=" ") 
        i=i+1
a=[1,2,'life',[1,0.5,3,4]]
b=['dhana','dad',8,7]
print(a+b)
print(len(a))
print(a[-1][0:2])
print(a[::-1])
print(b[0][1:])
c=['dhana','daddy',3.56,'good','lover',234]
c=c+b
print(c+b)
print(c[-4][3:8])
print(type(c))
d=[1,8,7,6,5,4]
d[2:5]=[3 ,4,5]
print(d)
d[::3]=[10,9]
print(d)
x=['apple','banan','orange']
for i in x:
    print(i)
    break
print(range(8))

for i in range(6):
    print(i)
o="hello world"
print(list(o))
print(list(range(10)))
print(list(range(10,48,6)))   
print('green' in ['red','orange'])
print( 10 not in range(5,12))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def abs(a,b,square=add):
    return square(a,b)
print(abs(2,4))    

def naming(name="dhana",nickname="sweety"):
    print(nickname + " " +name)
naming()
naming('daddy')
a=naming
add= lambda x,y: x*y
print(add(5,7))
double= lambda x: 2*x
print(double(8))
print((lambda x,y,z=7:x+y*z)(1,y=20))
# print(sorted['a1','j9','p8','u6','o4'],key= lambda x: int(x[-1]))
print("helloworld".upper())
a,b="dhana","sweety"
print("{} is a good girl".format(a))
print("{1} is the nickname of {0} and everyone call her {1} ".format(a,b))
print("dhana is the nickname of {:>10} and everyone call her {:<15} ".format(a,b))
print(a.replace('dhana','sweety'))