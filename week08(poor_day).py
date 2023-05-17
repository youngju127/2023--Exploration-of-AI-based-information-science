humans = int(input("몇분이세요? "))
adult, teenager, kid = 0, 0, 0
ages = [None for _ in range(humans)]
for i in range(humans):
    ages.append(int(input("나이는?")))

print(ages)
try:
    for age in ages:
        # 어른 : 20000 (>19), 청소년 : 10000(19-8), 어린이 : 5000(<8)
        if age > 19:
            total += 20000
            adult +=1
        elif 19 >= age >= 8:
            total += 10000
            teenager +=1
        else:
            total += 5000
            kid +=1
except IndexError as err:
    print(err)
else :
    print(f'어른 {adult}명, 청소년 {teenager}명, 어린이 {kid}명의 총 요금은 {total}원 입니다')