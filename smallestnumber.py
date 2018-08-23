def main():
    global lcm
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    if m > n:
        max = m
    else:
        max = n

    while (True):
        if ((max % m == 0) and (max % n == 0)):
            lcm = max
            break
        max += 1

    print(lcm)
if __name__ == '__main__':

   main()
