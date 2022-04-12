#3의 배수를 제외하고
#넘을때의 총합과 숫자를 출력하시오.


total,i = 0,0

for i in range(1, 101):
    if i % 3 ==0:
        continue
    total +=i
    print('{},{}'.format(i,total))

print("1~100의 합계중 3의 배수를 제외한 합", total)