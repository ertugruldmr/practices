ef operateActions(N):
    l=[]
    for _ in range(N):
        commands = input().split()
        
        if(commands[0]=="insert"):
            l.insert(int(commands[1]),int(commands[2]))
        elif(commands[0]=="print"): 
            print(l)
        elif(commands[0]=="remove"):
            l.remove(int(commands[1]))
        elif(commands[0]=="append"):
            l.append(int(commands[1]))
        elif(commands[0]=="sort"):
            l.sort()
        elif(commands[0]=="pop"):
            l.pop()
        elif(commands[0]=="reverse"):
            l.reverse()
            
if __name__ == '__main__':
    N = int(input())
operateActions(N)   