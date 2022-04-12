while True:
    print("="*50)
    print('===딕셔너리확인프로그램===')
    print('1. 키값으로 검색')
    print('2. value값으로 검색')
    print('3. 딕셔너리 전체 출력')
    print('4. 프로그램 종료')
    
    #위에 것 중 원하는 값으로 입력 받기.
    ch1 = input('원하는 번호를 입력하세요>>>')
    #숫자 외에 입력 되었을때 다시 초기화면으로 돌아가는 체크포인트
    if not ch1.isdigit():
        print('숫자만 입력가능합니다!')
        continue
    ch1 = int(ch1)
    
    if ch1 == 1:
        #1번 내에서 무한 반복
        while True:
              #내부에서 키 값 받기
        key1=input('키를 입력하세요(0:상위메뉴 이동)>>')