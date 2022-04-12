numbers = [273,103,5,32,65,9,72,800,99]
chk =['짝수', '홀수']
for number in numbers:
    if number>=100:
        print('100이상의 수',number)

     
for number in numbers:
        print('{:3d} : {}' .format(number,chk[number%2]))