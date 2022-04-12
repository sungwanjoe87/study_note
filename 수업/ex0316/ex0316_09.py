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


rantemp= []
count = 0
level1=list(words.keys())

while count < 5:
    rno = randint(0,9)
    if not level1[rno] in rantemp:
        rantemp.append(level1[rno])        
    else:
        continue
    count +=1

print(rantemp)