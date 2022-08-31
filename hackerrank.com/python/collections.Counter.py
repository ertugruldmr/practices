num_of_shoes = int(input())
shoes_sizes_avail = [int(x) for x in input().split()]
num_customers = int(input())
money_earned = 0
for i in range(num_customers):
    desired = [int(x) for x in input().split()]
    size = desired[0]
    price = desired[1]
    if size in shoes_sizes_avail:
        shoes_sizes_avail.remove(size)
        money_earned = money_earned + price
print(money_earned)