# a= input('문자를 입력하세요')
# if a=='$':
#     print('$인 문자입니다.')
# else:
#     print('$인 문자가 아닙니다.')

total,i = 0,0

for i in range(1,100):
    total += 1
    print(i)
    if total>100:
        break

print('합은:{}'.format(total))
print('100을 넘었을 때의 숫자는', i-1) 