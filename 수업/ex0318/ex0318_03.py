str1 = 'Python Is easy'

# print(str1.startswith('P')) #시작문자 확인 bool값으로 반환
# print(str1.endswith('k')) #끝나는 문자 확인. bool값으로 반환




# while True:
#     in_str = input('문자를 입력하세요')
#     count= 0
#     if in_str.lower() in str1.lower():
#         print('{}는 존재합니다.'.format(in_str))
        
#     else:
#         print('{}는 존재하지 않습니다.'.format(in_str))
#         count =+1
#         break
# print(str1.count('python'))

# print(str1.index('t'))
# if 'th' in str1:
#     print(str1.index('th'))
# else:
#     print('없습니다')
# print(str1.index('b')) #에러남.

# print(str1.find('b'))
# print(str1.find('t'))
# print(str1.upper()) #대문자로
# print(str1.lower()) #소문자로
# print(str1.swapcase()) #대문자-> 소문자, 소문자-> 대문자.
# print(str1.title()) #첫글자를 대문자로
# print(str1.isupper()) #첫글자가 대문자인지 확인문


# list1 =[10,4,3,9,20,21] 
# list2 =[21,20,9,3,4,10] #역순출력
# list3 =[3,4,9,10,20,21] #순차정렬
# list4 =[21,20,10,9,4,3] #역순정렬

# list1.reverse()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# instr ='서울인재개발원'


#문자열 역순
# instr,outstr ='',''
# count, i = 0,0

# instr = input('문자를 입력하세요>>')
# count = len(instr)

# for i in range(0,count):
#     outstr += instr[(count-1)-i] #역순 

# print(outstr)
    
    
    
    

# str1 ='서울인재개발원 파이썬 수업'
# for i in range(len(str1)):
#     if i==0:
#         print(str1[i],end='')
#     else:
#         print(','+str1[i],end='')

