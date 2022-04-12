#4개의 값을 입력 받아서, 합을 구하고, 입력한 값을 출력하시오.

aas = []
total = 0
for i in range(4):
    aas.append(int(input('{}숫자를 입력하세요:'.format(i+1))))

for aa in aas:
    total += aa
    
print('입력한 숫자:', aas)
print('입력한 숫자의 합계는', total)

