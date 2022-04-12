url ='http://www.naver.com'
#naver+글자의총길이수+c가 들어간 갯수+!!
#힌트:http:// .

in_str =input('비번을 넣어주세요 암호화 할게요...')

temp_str1 =in_str.replace('http://www.','')
print(temp_str1)
temp_str2 = temp_str1[:temp_str1.index('.')]
print(temp_str2+str(len(url))+str(url.count('c')+'!!'))