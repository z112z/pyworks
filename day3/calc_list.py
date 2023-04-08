# 리스트 생성 및 연산
score = [70, 80, 50, 90, 60]
print(len(score))
sum_v = 0

#반복문 유형1
# i = score[0]
for i in score:
    sum_v = sum_v + i #sum_v+= i
    print("i=", i)
print("총점:", sum_v)

#평균 = 총점 / 개
avg_v = sum_v / len(score)
print("평균:", avg_v)

#반복문 유형2
sum_v = 0
for i in range(0, len(score)):
    sum_v += score[i]
print("총점:", sum_v)
    
# 내장 함수 - sum()
print("총점:", sum(score))



# 인덱싱
print(score[0])
print(score[4]) #60
print(score[-1]) #60

#슬라이싱
print(score[0:]) # 전체
print(score[1:3]) #80, 50
print(score[:-1]) #맨끝에거 뺴고 전부다
print(score[:]) #전체


