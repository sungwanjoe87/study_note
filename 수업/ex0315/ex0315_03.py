# aa = [10,20,30]
# #list에 데이터 추가
# aa.append(40)

# print(aa)



#aa[4]=50 없는 주소는 에러남.
#0자리에 100으로 변경.
# aa[0]=100
# print(aa)

# #1에 자리에 데이터를 밀어넣어라
# aa[1:2]=(200,300)
# print(aa)

# aa[1:2]=[200,300]
# print(aa)

# aa[1]= [1,2]
# print(aa)


# del(aa[1:2])
# print(aa)

students=[ 
          [1,'홍길동',100,100,200,100,100.0,0],
          [2,'이순신',100,100,200,100,100.0,0],
          [3,'유관순',100,100,200,100,100.0,0],
          [4,'김유신',100,100,200,100,100.0,0],
          [5,'김구',100,100,200,100,100.0,0]]

#0 주소의 학생 삭제
# del(students[0])
# print(students)
# #전체 학생성적을 출력
# for stu in students:
#     for s in stu:
#         print(s,end=' ')
#     print()

chkname = input('찾는 학생의 이름을 입력하세요.>>')
chk=0
#5명의 학생을 검색하는 중
for stu in students:
    #찾는 학생이 있는지 확인.
    if stu[1]==chkname:
        print('[찾는 학생 검색]')
        for s in stu:
            print(s,end=' ')
        print()
        chk=1
        break
    else:
        continue

            #print((stu'{},{},{},{},{},{},{}' .format(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6]))
if chk==0:
    print('찾는 학생이 없습니다.')
        
        