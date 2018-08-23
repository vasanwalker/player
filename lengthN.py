def main():
    str=input()
    list=[]
    for i in str:
        n=ord(i)+3
        y=chr(n)
        list.append(y)

    print(''.join(list))
if __name__ == '__main__':

    main()
