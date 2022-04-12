#주민번호
#신규주민번호가 생겼음.
#구 주민번호를 사용하는 사람들이 있음.
#신규로 전환
#주민번호가 990101-1105555 / 990101-2105555 / 8번째 자리가 1,2로 시작되면, 앞에 19를 붙이고, 
#010101-3105555 / 010101-4105555 8번째 자리가 3,4면 20붙여서 출력하라.

socal_number = input('주민번호를 입력하세요')
temp = socal_number[7]

if temp =='1' or temp =='2'or temp =='5' or temp=='6':
    socal_number = '19'+socal_number
elif temp =='3' or temp =='4'or temp =='7' or temp=='8':
    socal_number = '20'+socal_number
else:
    print('숫자가 틀렸습니다.')

print()


#1001->s1001, a1002->t1002
#startswith
#s를 강제로 붙여서 학번을 출력하도록 하시오 예) s1001
#s가 붙어 있으면, t로 변경해서 출력하도록 하시오 예)t1001

# in_str = input('학번을 적으세요')
# com_str =''

# if not in_str.isdigit():
#     com_str = 't'+in_str.str[1:]
# else:
#     com_str = 's'+in_str

# print(com_str)
