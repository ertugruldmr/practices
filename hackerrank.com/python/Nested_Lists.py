all_list=[]
if __name__ == '__main__':
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_list.append([name,score])
       
all_list.sort(key = lambda x:x[1])

for i in all_list:
    if(i[1]!=all_list[0][1]):
        second_lowest_grade=i[1]
        break
    
output_list=[]
for i in all_list:
    if(i[1] == second_lowest_grade):
        output_list.append(i)
            
output_list.sort(key = lambda x:x[0])
    
for i in output_list:
    print(i[0]) 
