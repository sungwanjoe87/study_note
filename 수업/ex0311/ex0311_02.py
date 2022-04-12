import datetime
#현재시간을 가져온다
now = datetime.datetime.now()



print(now)
test=int(input("달을 넣으세요"))
#12,1,2는 겨울
#3,4,5는 봄
#6,7,8은 여름
#9,10,11은 가을
if 2<(now.month)<=5:
    print("봄 입니다.")
elif 5<(now.month)<=8:
    print("여름입니다.")
elif 8<(now.month)<=11:
    print("가을입니다.")
else:
    print("겨울입니다.")
    
#if (now.month == 3 or 4 or 5): # now.month가 3,4,5인지가 아니라 숫자인지 아닌지 비교하게 된다. \
    # now.month ==3 or now.month ==4 ... 이런식으로 작성해야 한다.

# #현재 년도
# print(now.year)
# #현재 달
# print(now.month)
# #현재 일
# print(now.day)
# #현재 시간
# print(now.hour)
# #현재 분
# print(now.minute)
# #현재 초
# print(now.second)

