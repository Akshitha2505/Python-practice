
1.Write a Python program to repeatedly subtract 3 from a number until the result becomes less than 0?
Input:14
Output:14 11 8 5 2

Explanation:
Stop the loop before printing a negative value.
-----------------------------
n=int(input('Enter a number:'))
i=n
while i>=0:
    print(i)
    i=i-3
    
----------------using for loop-----------
n=int(input('Enter a NUmber:'))
for i in range(n,0,-3):
    print(i)
    

2.Write a Python program to repeatedly double a number until it exceeds 100?

Input:3
Output:3 6 12 24 48 96

Explanation:
Terminate the loop when the next value becomes greater than 100.
---------------------------------
n=int(input('Enter a number:'))
i=n
while i<100:
    print(i)
    i=i+i
---------------using for loop--------------------
n=int(input('Enter a Number:'))===========================================not coming
for i in range(n,101):
    
        print(i+i)
        if i<=100: 
            break

3.Write a Python program to count how many times a number can be divided by 2 before it becomes odd?

Input:40
Output:3

Explanation:
40 → 20 → 10 → 5
The number was divided by 2 three times.
--------------------------------
n=int(input('Enter a number:'))
count=0
while n%2==0:
    n=n//2
    count=count+1
print(count)
    
4.Write a Python program to find the first even number greater than n that is divisible by 7 using a while loop and break.
Input:40
Output:42

Explanation:
Terminate the loop immediately after finding the required number.
-----------------------------------
n=int(input('enter a number:'))
i=n
while i>=n:
    if i%2==0 and i%7==0:
        print(i)
        break
    i=i+1
        
5.Write a Python program to find the first number greater than n that is divisible by 9 but not by 3 using a while loop and break.
Input:50

Output:No such number
Explanation:
Every number divisible by 9 is also divisible by 3
-----------------------------------
n=int(input('Enter a number:'))
i=n
while i>=n:
    if i%9==0:
        if i%3!=0:
            print(i)
            break