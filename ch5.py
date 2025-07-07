#리스트(list) : 변수를 하나로 관리 (하나의 리스트는 여러 값을 가짐)
subway = [10, 20, 30]
print(subway)

empty_list = [] #빈 리스트 생성

subway = ["푸", "피글렛", "티거"]
print(subway)

#피글렛이 몇 번째 칸에 탔는가?, 1
print(subway.index("피글렛"))

#이요르 탑승, ['푸', '피글렛', '티거', '이요르']
subway.append("이요르")
print(subway)

#루가 푸와 피글렛 사이에 탑승, ['푸', '루', '피글렛', '티거', '이요르']
subway.insert(1, "루")
print(subway)

#지하철 역마다 한 명씩 내림
print(subway.pop()) #이요르 내림, 이요르
print(subway)       #['푸', '루', '피글렛', '티거']

print(subway.pop()) #티거 내림, 티거
print(subway)       #['푸', '루', '피글렛']

#지하철에서 모두 내림, []
subway.clear()
print(subway)

#같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거"]
subway.append("푸")
print(subway)
print(subway.count("푸"))   #2

#리스트 정렬하기
num_list = [5, 2, 4, 3, 1]
num_list.sort()             #오름차순 정렬, [1, 2, 3, 4, 5]
print(num_list)

num_list.sort(reverse=True) #내림차순 정렬, [5, 4, 3, 2, 1]
print(num_list)

num_list.reverse()          #순서 뒤집기, [1, 2, 3, 4, 5]
print(num_list)

my_list = [1, 3, 2]
my_list.sort()
print(my_list)      #my_list 리스트 데이터 변경됨, [1, 2, 3]
your_list = [1, 3, 2]
new_list = sorted(your_list)
print(your_list)    #your_list 리스트 데이터는 변경되지 않음, [1, 3, 2]
print(new_list)     #your_list가 정렬된 새로운 리스트, [1, 2, 3]

mix_list = ["푸", 20, True, [5, 2, 4, 3, 1]]
print(mix_list)

mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(mix_list) #['푸', 20, True]
print(num_list) #[5, 2, 4, 3, 1, '푸', 20, True]

"""
append(), insert(), clear(), sort(), reverse()
, extend()
: 별도 문장으로 실행 후 변경된 리스트를 print() 문으로 출력
: 수행 후 반환하는 값 없이 리스트 자체가 변경됨

index(), pop(), count()
: print() 문 안에서 실행과 동시에 값 출력
: 동작 수행 후 값을 반환함
"""

#딕셔너리(dictionary) key1 : value1
#이때, key -> 중복 X, 변하지 않는 값
cabinet = {3: "푸", 100: "피글렛"}

empty_dict = {} #빈 딕셔너리 생성

print(cabinet[3])       #key3에 해당하는 value, 푸
print(cabinet[100])     #key100에 해당하는 value, 피글렛
print(cabinet.get(3))   #key3에 해당하는 value, 푸

#get() 함수 -> 정의되지 않은 key 전달하면 None 출력 후 프로그램 계속 실행
print(cabinet.get(5))   #None
print("hi")             #hi

#대괄호 -> 정의되지 않은 key 전달하면 오류 발생 후 프로그램 종료, error
#print(cabinet[5])
#print("hi")

#key에 해당하는 값이 없으면 기본값 사용, 사용 가능
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet["A-3"])   #푸
print(cabinet["B-100"]) #피글렛

#in 연산자 : 문자열에 해당 글자가 포함됐는지 확인
print("곰" in "곰돌이")     #True
print("돌이" in "곰돌이")   #True
print("푸" in "곰돌이")     #False

#값 변경/추가/삭제
cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거"     #key에 해당하는 값 O -> 값 변경
cabinet["C-20"] = "이요르"  #key에 해당하는 값 X -> 값 추가
print(cabinet)              #{'A-3': '티거', 'B-100': '피글 렛', 'C-20': '이요르'}

del cabinet["A-3"]
print(cabinet)  #{'B-100': '피글렛', 'C-20': '이요르'}

print(cabinet.keys())   #key만 출력, dict_keys(['B-100', 'C-20'])
print(cabinet.values()) #value만 출력, dict_values(['피글렛', '이요르'])
print(cabinet.items())  #key, value 한 쌍으로 출력, dict_items([('B-100', '피글렛'), ('C-20', '이요르')])

cabinet.clear()
print(cabinet)  #{}

#튜플(tuple) : 리스트의 읽기 전용 버전
#값 변경, 추가, 삭제 등 불가 but 리스트보다 속도가 빠름
menu = ("돈가스", "치즈돈가스")
print(menu[0])  #돈가스
print(menu[1])  #치즈돈가스

name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby) #피글렛 20 코딩
print(age, hobby, name) #20 코딩 피글렛

(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival)  #김포 > 제주
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)  #제주 > 김포

#세트(set)
#중복 X, 데이터 순서 보장 X
my_set = {1, 2, 3, 3, 3}
print(my_set)   #{1, 2, 3}

java = {"푸", "피글렛", "티거"} #자바 개발자 세트
python = set(["푸", "이요르"])  #파이썬 개발자 세트

empty_set = set()   #빈 세트 생성

#교집합, {'푸'}
print(java & python)
print(java.intersection(python))

#합집합, {'이요르', '피글렛', '푸', '티거'}
print(java | python)
print(java.union(python))

#차집합, {'티거', '피글렛'}
print(java - python)
print(java.difference(python))

#파이썬 개발자 추가(기존 개발자: 푸, 이요르), {'푸', '이요르', '피글렛'} 
python.add("피글렛")
print(python)

#자바 개발자 삭제(기존 개발자: 푸, 피글렛, 티거), {'푸', '티거'}
java.remove("피글렛")
print(java)

#자료구조 변환
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))   #<class 'set'>

menu = list(menu)   #리스트로 변환, ['주스', '우유', '커피'] <class 'list'>
print(menu, type(menu))

menu = tuple(menu)  #튜플로 변환, ('우유', '주스', '커피') <class 'tuple'>
print(menu, type(menu))

#5.6 실습 문제: 당첨자 뽑기
from random import shuffle, sample

lst = [1, 2, 3, 4, 5]
print(lst)                      #원본 리스트 출력
shuffle(lst)                    #리스트 섞기
print(lst)                      #섞은 후 리스트 출력
print(sample(lst, 1))           #리스트에서 값 1개를 무작위로 뽑기
print(sample(lst, len(lst)))    #shuffle() 함수와 동일한 동작 수행

"""
id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(id)
shuffle(id)
print(id)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : " + str(sample(id, 1)))
print("커피 당첨자 : " + str(sample(id, 3)))
print("-- 축하합니다! --")
"""

users = range(1, 21)        #1부터 21 직전까지 연속한 숫자 리스트 생성
#print(type(users))         #<class 'range'>
users = list(users)         #users를 리스트 자료구조로 변환, shuffle() -> 리스트에서만 사용 가능
shuffle(users)              #리스트 섞기
winners = sample(users, 4)  #users 리스트에서 중복 없이 4명 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))  #0번째 인덱스(1명)
print("커피 당첨자 : {0}" .format(winners[1:])) #1번째부터 마지막까지 슬라이싱(3명)
print("-- 축하합니다! --")

#셀프체크
course = ["자료구조", "알고리즘", "자료구조", "운영체제"]
#print(type(course))
print("신청한 과목은 다음과 같습니다.")
print(list(set(course)))