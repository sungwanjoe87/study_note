#문자를 입력받게 됩니다. 문자형
input1 = int(input('점수를 입력하세요>>'))

# if input1>=60:
#     print('합격입니다.')
# else:
#     print('불합격입니다.') 

if input1>=90:
    print('A', end='') #엔터키 생략 A에 +를 바로 붙여라!
    if input1>=95:
         print('+')
    elif 94>=input1>=90:
        print('-')

elif input1>=80:
    print('B', end='')
    if input1>=85:
         print('+')
    elif 84>=input1>=80:
        print('-')
    
elif input1>=70:
    print('C', end='')
    if input1>=75:
         print('+')
    elif 74>=input1>=70:
        print('-')

elif input1>=60:
    print('D', end='')
    if input1>=65:
         print('+')
    elif 64>=input1>=60:
        print('-')
else:
    print('F')



#짝수입니다. 홀수 입니다.

# if input1%2==0:
#     print("짝수 입니다.")
# else:
#     print("홀수 입니다.")

# if input1%3==0:
#     print("3의 배수입니다.")
# else:
#     print("3의 배수가 아닙니다.")
    
# if 5<input1<10:
#     print('5보다 크고 10보다 작은 수입니다.')
# else:
#     print('5보다 작거나 10보다 큰 수 입니다.')


# if input1>10:
#     print('10보다 큽니다.')
# else:
#     print('10보다 작습니다.')