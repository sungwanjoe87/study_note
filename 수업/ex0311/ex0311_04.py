from re import fullmatch


a=1
b=2
c=3
d=4
e=5 #'변수'5개가 선언됨.
#리스트
aa=[1,2,3,4,5,'문자', [1,2,3,4,5]]
bb=[i for i in range(0,25)]

# if 10 in aa:
#     print('1이 존재 합니다.')
# else:
#     print('1이 존재하지 않습니다')

frult = ['사과', '복숭아', '딸기', '배', '포도', '수박']

if '딸기' in frult:
    print ('여기에 딸기에 있습니다')

frult.append('한라봉')

print(frult)


#리스트 뒤에 추가문
aa.append(6)

print(aa)