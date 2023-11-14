def f(palindrome):
    result = False
    word = palindrome
    for i in palindrome:
        if i == palindrome[-1]:
            palindrome = palindrome[:-1]
        else:
            break
        if len(palindrome) < len(word)/2:
            result = True
            break
        else:
            continue
    return result
        
    
if __name__ == '__main__':
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))