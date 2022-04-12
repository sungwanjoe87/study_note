from sys import api_version
words2={ '연필':'pencil',
         '자': 'ruler',
         '책': 'book',
         '양말': 'sock',
         '모자': 'hat',
         '개': 'dog',
         '잠': 'sleep',
         '먹다': 'eat',
         '읽다': 'read',
         '피아노':'poaino'
}

words = {
    '자동차':'car',
    '의자':'chair',
    '사랑':'love',
    '국수':'noodle',
    '돼지': 'pig',
    '호랑이': 'tiger',
    '사자':'lion',
    '직업':'job',
    '사과':'apple'
    }
print('[영어 단어 테스트]')
print('1. 초등학교 1~2년')
print('2. 초등학교 3~4년')


#난이도 선택
ch1 = int(input('난이도를 선택하세요>>'))
if ch1 ==1:
    level=words
elif ch1 ==2:
    level=words2


wordlist =[]

for word in level:
    inwrds= input('{}의 영어 단어를 입력하세요'.format([word]))
    if inwrds.isdigit():
        if inwrds == 0:
            print('프로그램 종료합니다.')
            break
    if level[word] ==inwrds:
        print('정답입니다.{}:{}'.format(word,level[word]))
        wlist=[inwrds,'O',word,level[word]]
        wordlist.append(wlist)
                        
    else:
        print('오답입니다.{} :{}'.format(word,level[word]))
        wlist=[inwrds,'X',word,level[word]]
        wordlist.append(wlist)
ocount,xcount = 0,0
print('[정답 확인]')
print('='*50)
for idx,w in enumerate(wordlist):
    if 'O' in wlist:
        #1.정답, 2번 오답
        ocount +=1
        print('{}.{}, {}:{}'.format(idx+1,'정답',wlist[2],wlist[0]))
        print('{}'.format(wordlist))
    else:
        xcount +=1
        print('{}.{}, {}:{} 입력값'.format(idx+1,'오답',wlist[2],wlist[3],wlist[0]))
        print('{}'.format(wordlist))

#최종갯수 출력
print('정답{}, 오답{}, 점수는:{}점' .format(ocount,xcount,(ocount*10)))

#정답 : 9 오답 1 90점.