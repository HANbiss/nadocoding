#연산자(operator)
#산술 연산자 : 값 연산
print(1 + 1)    #더하기, 2
print(3 - 2)    #빼기, 1
print(5 * 2)    #곱하기, 10
print(6 / 3)    #나누기, 2.0

print(2 ** 3)   #거듭제곱, 8
print(10 % 3)   #나머지, 1
print(10 // 3)  #몫, 3

#비교 연산자 : 값 비교 (True / False)
print(10 > 3)       #크다, True
print(4 >= 7)       #크거나 같다, False
print(10 < 3)       #작다, False
print(5 <= 5)       #작거나 같다, True
print(3 + 4 == 7)   # 같다, True
print(1 != 3)       # 다르다, True

#논리 연산자 : 참 거짓 판단
print((3 > 0) and (3 > 5))  #모두 참이면 참, False
print((3 > 0) or (3 > 5))   #하나라도 참이면 참, True
print(not(1 != 3))          #참이면 거짓, 거짓이면 참, False

"""
단축평가
(5 > 4 > 3) == (5 > 4 and 4 > 3)
print(5 > 4 > 3) : 5 > 4는 참이므로 다음 수식 확인, True
print(4 > 5 > 3) : 4 > 5는 거짓이므로 다음 수식 확인하지 않고 결과 출력, False

연산자의 우선순위
[], {}, () -> ** -> *, /, //, % -> +, - ->, not, in, <, <=, >, >=, !=, == -> and, or -> =
"""

number = 2 + 3 * 4
print(number)
#number = number + 2
number += 2     #16
print(number)
number -= 2     #number = number - 2, 14
print(number)
number *= 2     #number = number * 2, 28
print(number)
number /= 2     #number = number / 2, 14.0
print(number)
number **= 2    #number = number ** 2, 196.0
print(number)
number //= 2    #number = number // 2, 98.0
print(number)
number %= 2     #number = number % 2, 0.0
print(number)

#함수(function) : 파이썬에서 특정 기능을 수행하도록 미리 만들어 둔 명령어
print(abs(-5))          #-5의 절대값, 5
print(pow(4, 2))        #4를 제곱한 값, 16
print(max(5, 12))       #5와 12 중 큰 값, 12
print(min(5, 12))       #5와 12 중 작은 값, 5
print(round(3.14))      #3.14를 소수점 이하 첫째 자리에서 반올림한 정수, 3
print(round(4.678, 2))  #4.678을 소수점 이하 셋째 자리에서 반올림한 값, 4.68

#모듈(module) : 어떤 기능을 하는 코드를 모아 높은 파이썬 파일
#from 모듈명 import 기능
from math import *  #math 모듈의 모든 기능을 가져다 쓰겠다!

result = floor(4.99)    #4.99의 내림, 4
print(result)
result = ceil(3.14)     #3.14의 올림, 4
print(result)
result = sqrt(16)       #16의 제곱근, 4.0
print(result)

"""
import math
#math의 모든 기능을 가져다 쓰겠다! -> math.을 함께 작성
result = math.floor(4.99)
"""

from random import *
print(random())                 #0이상 1 미만 사이에서 난수 생성
print(random() * 10)            #0.0이상 10.0 미만에서 난수 생성
print(int(random() * 10))       #0이상 10 미만 정수에서 난수 생성
print(int(random() * 10) + 1)   #1이상 11 미만 정수에서 난수 생성

print(randrange(1, 46)) #1이상 46 미만에서 난수 생성
print(randint(1, 45))   #1이상 45 이하에서 난수 생성

#3.5 실습 문제: 스터디 날짜 정하기
#from random import *
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정됐습니다.")

#셀프체크
cels = 30
#cels= 10
fahr = (cels * 9 / 5) + 32
print("섭씨 온도 : " + str(cels))
print("화씨 온도 : " + str(fahr))