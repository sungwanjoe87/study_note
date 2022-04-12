import operator

tdic,tlist = {},[]

tdic = {'love':'사랑', 'chair':'의자', 'game':'게임','car':'자동차'}

#key와 value를 튜플형태로 출력 -list형태로 출력
tlist2 = list(tdic.items())
tlist2.sort(reverse=True)
print(tlist2)
# tlist = sorted(tdic.items(), key=operator.itemgetter(0))
# print(tlist)
# print(tdic.keys())
# print(tdic.values())
# print(tdic.items())
# print(list(tdic.keys))


# tlist1 = [4,6,1,6,8,9,11,2]
# #새로운 리스트에 저장 sorted 기존의 리스트는 변경되지 않고 새로운 리스트에 담긴다.
# tlist2 = sorted(tlist1)
# # tlist1.sort(reverse=True)
# print(tlist1)

# tlist1.reverse()
# print(tlist1)

