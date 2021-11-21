#Menu Driven Program
print('Welcome to menu\'s'.center(50))
print('''1. Adition
2. odd even
3. pallindrome
4. Greater Among 3 number
5. Leap year
6. Reverse Number
7. Emrip Number
8. Amstrong Number
9. Disrum Number
10. Automophic Number
11. Prime number
12. Calculator
13. Diamond Program
14. Convert Uppercase
15. Convert Lowercase
16. Convert Swapcase
''')
choice=int(input('Enter your Choice? '))
if choice==1:
    num1=int(input("Num1: "))
    num2=int(input("Num2: "))
    Add=num1+num2
    print(f"Addition of number {Add}")
elif choice==2:
    num1=int(input("Enter a number: "))
    if num1%2==0:
        print("Even")
    else:
        print("Odd")
elif choice==3:
    String=input("Enter a String: ")
    Reverse=String[::-1]
    if String==Reverse:
        print("Pallindrome")
    else:
        print("Not Pallindrome")
elif choice==4:
    Num1=int(input("Num1: "))
    Num2=int(input("Num2: "))
    Num3=int(input("Num3: "))
    if(Num1>Num2 and Num1>Num3):
        print("Num1 is Greater")
    elif(Num2>Num3):
        print("Num2 is Greater")
    else:
        print("Num3 is Greater")
elif choice==5:
    Year=int(input("Enter a Year: "))
    if(Year%4==0 and Year%100!=0 or Year%400==0):
        print("Leap Year")
    else:
        print("Not Leap Year")
elif choice==6:
    Num=int(input("Enter a number: "))
    Rev=0
    while(Num>0):
        Rem=Num%10
        Rev=Rev*10+Rem
        Num=Num//10
    print(f"Reverse: {Rev}")
elif choice==7:
    n=int(input("Enter a number: "))
    for i in range(2,n//2+1):
        if(n%i==0):
            print("Not Emrip")
            break
        else:
            rev=int(str(n)[::--1])
            for j in range(2,rev//2+1):
                if(rev%j==0):
                    print("Not Emrip")
    else:
        print("Emrip")
    
elif choice==8:
    n=int(input("Enter a number: "))
    sum=0
    p=len(str(n))
    while(n>0):
        rem=n%10
        sum=sum+rem**p
        n=n//10
    if(n==sum):
        print(f"{n}  is a Armstrong Number")
    else:
        print(f"{n}  is not a armstrong number")
elif choice==9:
    n=int(input("Enter a number: "))
    sum=0
    p=len(str(n))
    while(n>0):
        rem=n%10
        sum=sum+rem**p
        n=n//10
        p-=1
    if(n==sum):
        print(f"{n}  is a Disrum Number")
    else:
        print(f"{n}  is not a Disrum number")
elif choice==10:
    num=int(input("Enter a number: "))
    sqrNum=pow(num,2)

    length= len(str(num))

    result=sqrNum%pow(10,length)

    if num==result:
        print('Automorphic')
    else:
        print('Not Automorphic')
elif choice==11:
    Num=int(input("Enter a Number: "))
    for i in range(2,Num//2+1):
            if(Num%i==0):
                print("Not Prime Number")
                break
    else:
        print("Prime Number")
elif choice==12:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    operator=input('Operator: ')
    if num2==0:
        print("Denominator should not be zero")
    if num2!=0:
        
        calc={"+":num1+num2, "-":num1-num2, "*":num1*num2, "/":num1/num2, "%":num1%num2}
        print(num1,operator,num2, '=', calc[operator])
                   
    else:
        print("Invaild Operator")
elif choice==13:
    n=7
    star=1
    space=n//2
    for i in range(n):
        for j in range(space):
            print(" ",end=" ")
        for k in range(star):
            if(k==0 or k==star-1 or i==n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        if(i<n//2):
            star+=2
            space-=1
        else:
            star-=2
            space+=1
elif choice==14:
    s=input("Enter a String: ")
    s1=" "
    for i in s:
        if(i>='a' and i<='z'):
            k=ord(i)-32
            s=chr(k)
            s1+=s
        else:
            s1+=i
    print(s1)

elif choice==15:
    s=input("Enter a string: ")
    s1=""
    for i in s:
        if(i>='A' and i<='Z'):
            k=ord(i)+32
            s=chr(k)
            s1+=s
        else:
            s1+=i
    print(s1)

elif choice==16:
    s=input("Enter a string: ")
    s1=""
    for i in s:
        if(i>="A" and i<="Z"):
            k=ord(i)+32
            s=chr(k)
            s1+=s
        elif(i>="a" and i<="z"):
            k=ord(i)-32
            s=chr(k)
            s1+=s
        else:
            s1+=i
    print(s1)        
else:
    print("Not Vaild Input")
