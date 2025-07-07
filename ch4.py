sentence1 = '나는 소년입니다.'
print(sentence1, type(sentence1))
sentence2 = "파이썬은 쉬워요."
print(sentence2, type(sentence2))
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)

#인덱스(index) : 데이터의 순서 또는 위치 (변수명[인덱스])
jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])    #양수 인덱스는 0부터 시작, 1

#슬라이싱(slicing) : 데이터 자르기 (변수명[시작 인덱스:종료 인덱스], 시작 인덱스부터 종료 인덱스 직전까지)
print("연 : " + jumin[0:2]) #0부터 2 직전까지, 99
print("월 : " + jumin[2:4]) #2부터 4 직전까지, 02
print("일 : " + jumin[4:6]) #4부터 6 직전가지, 29

print("생년월일 : " + jumin[:6])            #처음부터 6 직전까지, 990229
print("주민등록번호 뒷자리 : " + jumin[7:])  #7부터 끝까지, 1234567
print("주민등록번호 뒷자리 : " + jumin[-7:]) #뒤에서 7번째 위치부터 끝까지, 1234567 (음수 인덱스는 -1부터 시작)

#문자열 처리 함수 (문자열(또는 변수).함수())
python = "Python is Amazing"

print(python.lower())                   #전체 소문자로 변환, python is amazing
print(python.upper())                   #전체 대문자로 변환, PYTHON IS AMZAING
print(python[0].isupper())              #인덱스 0에 있는 값이 대문자인지 확인, True
print(python[1:3].islower())            #인덱스 1부터 2에 있는 값이 소문자인지 확인, True
print(python.replace("Python", "Java")) #Python을 Java로 바꾸기, Java is Amazing
    #python 변수에 저장된 값 자체가 바뀌지는 않는다!!!

#문자열 내 문자의 위치 찾기
find = python.find("n")             #처음 발견한 n의 인덱스, 5
print(find)
find = python.find("n", find + 1)   #인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스, 15
print(find)
find = python.find("Java")          #Java가 없으면 -1 반환 후 다음 문장 실행
print(find)
index = python.index("n", 2, 6)     #인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스, 5
print(index)
#index = python.index("Java")       #Java가 없으면 오류 발생 후 프로그램 종료
#print(index)

print(python.count("n"))    #지정한 문자 또는 문자열이 나오는 횟수, 2
print(python.count("v"))    #지정한 문자 또는 문자열이 없으면 0, 0
print(len(python))          #문자열 길이 정보(공백 포함) 출력

#문자열 포매팅(string formatting) : 원하는 위치에 특정한 값 또는 변수를 넣어 하나의 문자열로 표현
    #1. 서식 지정자(format specifier) 사용하기
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)  #%s로도 정숫값 표현 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

    #2. format() 함수 사용하기
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
#{} 안에 인덱스가 없으면 순서대로, 인덱스가 있으면 인덱스에 맞춰 값이 들어감
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))

    #3. f-문자열 사용하기 : 문자열이 나오기 전에 정의한 변수의 값 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자(escape character)
print("백문이 불여일견\n백견이 불여일타")    #\n : 줄바꿈
print("저는 '나도코딩'입니다.")             #또는 print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")           #따옴표 사용 시에는 \"
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")    #탈출문자와 동일한 형식에서는 \\
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")       #r : 문자열 내 어떤 값이 있든지 무시하고 출력
print("Red Apple\rPine")    #\r : 커서를 맨 앞으로 이동(Red를 덮어씀), PineApple
print("Redd\bApple")        #\b : 앞 글자 하나 삭제, RedApple
print("Red\tApple")         #\t : 여러 칸 띄어쓰기, Red     Apple

#4.6 실습 문제: 비밀번호 만들기
url = "http://naver.com"
#url = "http://daum.com"
#url = "http://google.com"
#url = "http://youtube.com"

rmurl = url[7:-4]
#rmurl = url.replace("http://", "") #rmurl = naver.com
#rmurl = rmurl[:rmurl.index(".")]   #rmurl = naver
pw = rmurl[:3] + str(len(rmurl)) + str(rmurl.count("e")) + "!"

print(f"{url}의 비밀번호는 {pw}입니다.")

#셀프체크
sen = "the early bird catches the worm."
#sen = "Actions Speak Louder Than Words."
#sen = "PRACTICE MAKES PERFECT"

sen = (sen[0].upper()) + (sen[1:].lower())
print(sen)
#print(sen.capitalize())    #첫 글자는 대문자로, 나머지는 소문자로 변경