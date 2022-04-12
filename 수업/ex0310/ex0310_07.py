# a = input('숫자를 입력하세요')
# b = input('숫자를 입력하세요')

# #더하기 뺴기, 곱하기, 나누기를 출력하시오.

# print(a,'+',b, '=',int(a)+int(b))
# print(a,'-',b, '=',int(a)-int(b))
# print(a,'X',b, '=',int(a)*int(b))
# print(a,'/',b, '=',int(a)/int(b))

# print('{}-{}={}'.format (int(a),int(b),int(a)-int(b)))

kor = int(input('국어성적을 입력하세요'))
eng = int(input('영어성적을 입력하세요'))
math = int(input('수학성적을 입력하세요'))
print ('{}+{}+{}={}' .format (kor,eng,math,kor+eng+math))
print ('{}' .format ((kor+eng+math)/3))

num1 = float(input ("숫자를 입력하세요"))

num2 = float(input ("두번째 숫자를 입력하세요"))

print(num1/num2)
print(num1//num2)
print(num1%num2)