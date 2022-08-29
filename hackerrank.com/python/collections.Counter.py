num_of_shoes = int(input())
shoe_list = [int(i) for i in input().split(" ")]
num_cust = int(input())
total=0
for i in range(num_cust):
 temp=[]
 temp= [int(i) for i in input().split(" ")]
 size=temp[0]
 price=temp[1]
 if size in shoe_list:
     total+=price
     shoe_list.remove(size)   
print(total)