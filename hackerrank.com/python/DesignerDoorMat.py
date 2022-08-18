
def draw_pattern(n, m):
    # defining initial variables
    space, pattern, text = "-", ".|.", "WELCOME"

    
    # draw upper side rows
    for i in range(n//2):print(f"{pattern * (2*i + 1)}".center(m, space))
    
    # draw middle row 
    print(text.center(m, space))

    # draw lower side rows
    for i in reversed(range(n//2)): print(f"{pattern * (2*i + 1)}".center(m, space))
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    draw_pattern(n, m)