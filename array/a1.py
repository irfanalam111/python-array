def main():
    n=int(input("enter your number..."))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "*"*i

if __name__=="__main__":
    main()
    