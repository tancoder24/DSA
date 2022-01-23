def main():
    S = input()
    
    if(any(i.isalnum() for i in S)):
        print("True")
    else:
        print("False")
    if(any(i.isalpha() for i in S)):
        print("True")
    else:
        print("False")
    if(any(i.isdigit() for i in S)):
        print("True")
    else:
        print("False")
    if(any(i.islower() for i in S)):
        print("True")
    else:
        print("False")
    if(any(i.isupper() for i in S)):
        print("True")
    else:
        print("False")
    #Your code goes here
    
    return 0

if __name__ == '__main__':
    main()