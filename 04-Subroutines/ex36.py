def f(detector):
    detection = False
    k = 0
    for i in detector:
        if k == 3:
            detection = True
            break
        if i == "+":
            k += 1
        else:
            k -=1
    return detection
            
if __name__ == '__main__':
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))
