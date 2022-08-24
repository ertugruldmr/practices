def is_vowel(c):
    return 'AEIOU'.count(c) 

def minion_game(string):
    vowel = 0
    cons = 0
    length = len(s)

    for i in range(length):
        c = is_vowel(s[length-(i+1)])
        vowel += (i+1)*c
        cons  += (i+1)*(1-c)
                
    if cons > vowel:
        print ("Stuart %d" %cons)
    elif vowel > cons:
        print("Kevin %d" %vowel)
    else: 
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)