foods = {
    '떡볶이':'오뎅',
    '짜장면':'단무지',
    '라면':'김치',
    '피자':'피클',
    '맥주': '땅콩',
    '치킨': '치킨무',
    '삼겹살':'상추'}
while True:
    
    print (foods.keys())
    input1 = input('원하는 음식을 입력하세요.>>(프로그램 종료는 0번을 입력하세요')

    if input1.isdigit():
        if int(input1)==0:
            print('다시 입력하세요')
            break
    else:
        print('찾고자 하는 음식이 없습니다. 다시 입력하세요')