money,c500,c100,c50,c10 =0,0,0,0,0

money= int(input('교환할 돈을 입력하세요'))
#500원 동전 개수 1270 ->2개*500=1000 나머지 270
c500 = money//500
#100원 동전 개수 270 -> 2개
c100 = (money%500)//100
#50원 동전 개수 70 ->1개*50=50 나머지 20
c50 = ((money%500)%100)//50
#10원 동전 개수 20 ->2개
c10 = (((money%500)%100)%50)//10

print('입력한 금액 :',money)
print('500원 동전 :',c500)
print('100원 동전:', c100)
print('50원 동전:', c50)
print('10원 동전:', c10)