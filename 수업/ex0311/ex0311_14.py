# for i in range(1,10):
#     # print('[{} 단 ]'.format(i))
#     for j in range(2,10):
#         print('{} * {} = {}  '. format(j,i,j*i),end='\t')
#     print()


#입력한 단 부터 9단까지 출력

n1=int(input("원하는 단수 첫번째를 입력하세요>>"))
x1=int(input("원하는 단수 두번째 숫자를 입력하세요")

if x1 > n1:
    x1,n1 = n1,x1


    for n in range(n,x1+1):
        for x in range(1,10):
            print('{} * {} = {} ' .format(n,x,n*x), end='\t')