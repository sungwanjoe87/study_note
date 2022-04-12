#0부터 100까지 7의 배수의 합을 구하시오.

#0~100까지 홀수의 합을 구하시오.

#1, 10 -> 홀수의 합을 구하시오.




num1 = int(input("첫번째 숫자를 입력하시오"))
num2 = int(input("두번째 숫자를 입력하시오"))
sum=0
for i in range(num1,num2+1):
    if i%2 !=0:
        sum = sum + i
print(sum)
    
    
    
    

# num7 = ()
# sum= 0
# sum1= 0
# for i in range(0,101,7):
#     if i%7==0:
#         sum = sum+i

# print('7의 배수의 합:', sum)

# for i in range(0,100):
#     if i%2 !=0:
#         sum1 = sum1+i

# print('홀수의 합:', sum1)