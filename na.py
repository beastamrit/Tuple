a=("tuples",3,2.1)
print(a)
b=(1,3,5,7,7,7,11)
print(b)
b=b+(9,)
print (b)
print(b.count(7))
print(b[2])
print(b[2:5])
def pallen (r):
    e=len(r)-1
    s=0
    while s<e:
        if r[s]!=r[e]:
            return False
        s=s+1
        e=e-1
    return True
r=(1,2,3,3,2,1)
if pallen(r):
    print("flip flop")
else : 
    print("not flip flop")
    