def down(a,i):
    temp=a[i]
    a[i]=a[i+3]
    a[i+3]=temp
    return a

def up(a,i):
    temp=a[i]
    a[i]=a[i-3]
    a[i-3]=temp
    return a

def right(a,i):
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
    return a

def left(a,i):
    temp=a[i]
    a[i]=a[i-1]
    a[i-1]=temp
    return a
def pop():
    minh=10
    minind=-1
    i=0
    while(i<len(openlist)):
        j=0
        count=0
        while(j<9):
            if(openlist[i][j]!=goal[j]):
                if(openlist[i][j]!=0):
                    count+=1
            j+=1
        if(minh>count):
            minh=count
            minind=i
        i+=1
    val=openlist[minind]
    openlist.pop(minind)
    return val
print("\nEnter the start state ")
start=[]
start.extend(list(map(int,input().split())))
start.extend(list(map(int,input().split())))
start.extend(list(map(int,input().split())))
print(start)

print("\nEnter the goal state ")
goal=[]
goal.extend(list(map(int,input().split())))
goal.extend(list(map(int,input().split())))
goal.extend(list(map(int,input().split())))
print(goal)

openlist=[]
closedlist=[]
dumy=start.copy()
openlist.append(dumy)

while(True):
    dumy=pop()
    closedlist.append(dumy)
    print("step"+str(dumy[0:3]))
    print("    "+str(dumy[3:6]))
    print("    "+str(dumy[6:9]))
    indzero=dumy.index(0)
    if(indzero<6):
        openlist.append(down(dumy.copy(),indzero))
    if(indzero>2):
        openlist.append(up(dumy.copy(),indzero))
    if((indzero%3)<2):
        openlist.append(right(dumy.copy(),indzero))
    if((indzero%3)>0):
        openlist.append(left(dumy.copy(),indzero))

    
    if(dumy==goal):
        print("Goal state reached"+str(dumy))
        break