if __name__ == '__main__':
    s = input()
    

            
    #alphanumeric
    print(any([i.isalnum() for i in s]))
    #alphabetical characters
    print(any([i.isalpha() for i in s]))
    #digit
    print(any([i.isdigit() for i in s]))
    #lowercase
    print(any([i.islower() for i in s]))
    #uppercase
    print(any([i.isupper() for i in s]))
