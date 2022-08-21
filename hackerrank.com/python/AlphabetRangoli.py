def print_rangoli(size):
    width = (size-1) * 4 + 1

    for i in [abs(n) for n in range(-size+1, size)]:
        line = chr(ord("a") + i)
        for j in range(size-i-1):
            letter = chr(ord("a") + i + j + 1)
            line = letter + line + letter
            
        print("-".join(list(line)).center(width, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)