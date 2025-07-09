#조건문
#조건이 하나일 때 : if문
'''
weather = "비"

if weather == "비":
    print("우산을 챙기세요.")

#조건이 여러 개일 때 : elif문
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")  #앞의 조건에 모두 해당하지 않을 때 실행

#값 입력받기 : input()
weather = input("오늘 날씨는 어때요? ")
#print(weather)

if weather == "비" or weather == "눈":  #조건 변경
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물이 필요 없어요.")

temp = int(input("오늘 기온은 어때요? "))   #입력값을 정수형으로 형변환

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
#elif 10 <= temp and temp < 30:
#elif 10 <= temp < 30:
elif 10 <= temp:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

#반복문
#범위 안에서 반복하기 : for문
for waiting_no in [1, 2, 3, 4, 5]:
    print("대기번호 : {0}" .format(waiting_no))

for waiting_no in range(5): #0부터 5직전까지(0~4), 0, 1, 2, 3, 4
    print("대기번호 : {0}" .format(waiting_no))
    
for waiting_no in range(1, 6): #1부터 6직전까지(1~5), 1, 2, 3, 4, 5
    print("대기번호 : {0}" .format(waiting_no))
    
for waiting_no in range(1, 6, 2): #1부터 6직전까지(1~5)에서 2씩 간격 주기, 1, 3, 5
    print("대기번호 : {0}" .format(waiting_no))

orders = ["아이언맨", "토르", "스파이더맨"]
for customer in orders:
    print("{0} 님, 커피가 준비됐습니다. 픽업대로 와 주세요." .format(customer))

#조건을 만족할 동안 반복하기 : while문
customer = "토르"
index = 5

while index >= 1:
    print("{} 님, 커피가 준비됐습니다." .format(customer))
    index -= 1  #횟수 1회 차감
    print("{}번 남았어요." .format(index))
    if index == 0:
        print("커피를 폐기 처분합니다.")

"""
customer = "아이언맨"
index = 1

while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1}회" .format(customer, index))
    index += 1
#Ctrl + c 입력 시 강제 종료
"""

customer = "토르"
person = None   #초기화

while person != customer:
    print("{0} 님, 커피가 준비됐습니다." .format(customer))
    person = input("이름이 어떻게 되세요? ")

#흐름 제어하기 : continue와 break
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:       #결석한 학생이면
        continue                #다음 학생으로 넘어가기
    elif student in no_book:    #책을 가져오지 않으면 바로 수업 종료
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요." .format(student))
        break                   #반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요." .format(student))

#for문 한 줄로 작성하기 : list comprehension
#[동작 for 변수 in 반복 대상]
students = [1, 2, 3, 4, 5]
print(students)

#각 항목에 100 더하기
students = [i + 100 for i in students]
print(students)

students = ["Iron man", "Thor", "Spider Man"]
print(students)

#각 이름을 이름의 길이 정보로 변환
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "Spider Man"]
print(students)

#각 이름을 모두 대문자로 변경
students = [i.upper() for i in students]
print(students)
'''
#6.3 실습 문제: 태시 승객 수 구하기
from random import *

total_customer = 0

for customers in range(1, 51):
    time = randint(5, 50)

    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))
        total_customer += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))

print("총 탑승객 : {}명" .format(total_customer))

#셀프체크
"""
price = 1000
quantity = 6

for i in range(quantity):
    print("2+1 상품입니다.")

print("총 가격은 {}원입니다." .format(int(price * (quantity - quantity / 3))))
"""

price = 1000
goods = 3
total = 0

for i in range(1, goods + 1):
    print("2+1 상품입니다.")
    if i % 3 == 0:
        continue
    total += price

print("총 가격은 " + str(total) + "원입니다.")