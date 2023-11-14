def f(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        largest = n1
    elif n2 > n1 and n2 > n3:
        largest = n2
    else:
        largest = n3
    if n1 < n2 and n1 < n3:
        smallest = n1
    elif n2 < n1 and n2 < n3:
        smallest = n2
    else:
        smallest = n3
    return largest - smallest

if __name__ == '__main__':
    print(f(7,4,9))
    print(f(2,12,8))