words = {
        '자동차':'car',
        '의자':'chair',
        '사랑':'love',
        '국수':'noodle',
        '돼지': 'pig',
        '호랑이': 'tiger',
        '사자':'lion',
        '직업':'job',
        '사과':'apple',
        '여우':'fox'
        }

words2={ 
        '연필':'pencil',
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

from random import *

print ('        [영단어 테스트]         ')
print ('1.      초등 1~2학년        ')
print ('2.      초등 3~4학년        ')
print ('0.      프로그램 종료       ')

ch = input('원하는 번호를 입력하세요')

if ch ==1:
    level = words
elif ch ==2:
    level = words2
elif ch ==3:
    print('프로그램을 종료합니다.')
    exit()

wordlist = []
for word in level:
    answer = input('{}의 영단어를 입력하세요'.format(word))
    if level[word] == answer:
        print ('정답입니다. {}:{}' .format(word,level(word)))
        wlist= (answer,'O', word, level(word))
        wordlist.append(wlist)