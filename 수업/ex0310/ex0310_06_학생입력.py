# #입력
# a = input()
# #출력
# print(a)

id='admin'
pw='1111'
students=[]
count = 1
# u_id = input('아이디를 입력하세요>>')
# u_pw = input('패스워드를 입력하세요>>')
#무한 반복
while True:

    # if(id==u_id and pw==u_pw):

        stu_no = count
        print('학생번호:', stu_no)
        stu_name = input("이름을 입력하세요")
        kor = int(input("국어성적을 입력하세요"))
        eng = int(input("영어성적을 입력하세요"))
        math = int(input("수학성적을 입력하세요"))
        total = kor+eng+math
        avg = total/3
        rank = 0
        student = [stu_no,stu_name,kor,eng,math,total,avg,rank]
        students.append(student)
        print(students)
        count += 1
        # print('학생번호:'+ stu_no)
        # print('학생이름:'+ stu_name)
        # print('국어:',kor)
        # print('영어:',eng)
        # print('수학:',math)
        # print('합계:{}' .format(kor+eng+math))
        # print('평균:{:.2f}' .format((kor+eng+math)/3))        
    # else:
    #     print ("아이디, 패스워드가 일치하지 않습니다. 프로그램을 종료합니다.")