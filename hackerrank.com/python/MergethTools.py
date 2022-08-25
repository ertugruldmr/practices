import textwrap

def merge_the_tools(string, k):
    s_lst = textwrap.wrap(string, k)
    for s in s_lst:
        s = ''.join(list(dict.fromkeys([*s])))
        print(s)

if __name__ == '__main__':