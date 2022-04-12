aa = []
bb = []


# for i in range(100):
#     aa.append(i*2)

# for j in range(100): #0,1,2,3,4,5,6,...   , 99,98~ 
#     bb.append(aa[99-j])


# print(bb)


for i in range(200):
    aa.append(i*3)

for j in range(200):
    bb.append(aa[199-j])

print(aa[3:9]) #3~8까지 출력
print(aa[100:]) #100부터 끝까지
print(aa[190:210]) #인덱스가 없는 것을 출력하면 슬라이스에선 에러나지 않고 출력됨.
print(aa[-7:]) #-7번째 뒤에서 부터 출력.
