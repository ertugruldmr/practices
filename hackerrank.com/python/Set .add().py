size=int(input())
countryList=[]
for _ in range(size):
    countryList.append(input())
print(len(set(countryList)))