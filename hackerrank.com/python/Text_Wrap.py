def wrap(string, max_width):
    result=""
    for i in textwrap.wrap(string,max_width):
        result+=i+"\n"
    
    return result