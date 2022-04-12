from random import*

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


#튜플 리스트로 만들어 5개 5개씩 10개를  넣어라 tdic

#5개 만 먼저 words에서

wlist =list(words.items()) 
count =0
listtemp = [] #임시 저장소
while count <5:
    rno = randint(0,9)
    #랜덤으로 리스트에 담기
    #[('자동차':'car'), (........)]
    if not wlist[rno] in listtemp:
        listtemp.append(wlist[rno])
        count +=1

#print(listtemp)


w2list =list(words2.items())
count1 = 0
listtemp2 = []

while count1 <5:
        rno = randint(0,9)
        if not w2list[rno] in listtemp2:
                listtemp2.append(w2list[rno])
                count1 +=1

#print(listtemp2)

tdic = listtemp+listtemp2

print(tdic)