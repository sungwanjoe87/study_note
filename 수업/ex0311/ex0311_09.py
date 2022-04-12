#숫자입력이 1,10이면 1~10이 모두 더해지게 하자.
num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요")) 

sum = 0
if num1 > num2:
    num1,num2 = num2,num1
for i in range(num1,(num2)+1): #eval은 문자를 숫자로 변경해주는 함수
    sum = sum + i

print('총합',sum)