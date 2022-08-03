
def takeInputs():
    Values = input().split()
    x=int(Values[0])
    k=int(Values[1])
    Pol = input().split()#Given Format
    
    Pol=castFromStringToExpression(x,Pol)
    
    return (x,k,Pol)

def castFromStringToExpression(x,pol):
    newPol=[]
    for statement in pol:
        if("**" in statement):
            newPol.append(x ** int(statement[len(statement)-1]))        
        elif(statement=="x" or statement == "X"):
            newPol.append(x)
        elif(statement == "+" or statement=="-"):
            newPol.append(statement)
        else:
            newPol.append(int(statement))
    return newPol

def calculatePolyOutput(pol):
    value=pol[0]
    for i in range(1,len(pol),2):
        if(pol[i]=="+"):
            value+=pol[i+1]
        elif(pol[i]=="-"):
            value-=pol[i+1]

    return value
        
def check(k,PolValue):
    if(k==PolValue):
        return True
    return False
 
def start():
    x,k,pol = takeInputs()
    polValue= calculatePolyOutput(pol)
    print(check(k,polValue))
"""
manuel handling    
start()
"""    
def startUsing_method():
    x,k = map ( int , input().split())
    s= input()
    print (eval(s) == k)
    
startUsing_method()