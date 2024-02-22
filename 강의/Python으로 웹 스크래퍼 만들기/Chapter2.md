# 파이썬 함수의 구조

### 함수의 구조

1. def 함수*이름(매개변수):
   수행할*문장1
   수행할\_문장2
   print()

함수이름(인수)

2. 매개변수(parameter)와 인수(arguments)는 혼용해서 사용하는 용어이다
   입력으로 전달된 값을 받는 변수, 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.

### 주의사항

1. 인수가 없을 시 기본값을 설정해주어야 오류가 발생하지 않는다.
   def say_hello(user_name="anonymous"):
   print("hello",user_name)

   say_hello()
   결과 : hello anonymous

2. 주석은 #으로 달기

3. Ture,False 입력시 앞글자 대문자 사용하기

### 함수명 주의사항

1. 숫자로 시작하면 X
2. 특수문자는 언더바(\_)만 사용가능
3. 공백 포함 X
4. 키워드 사용 금지
5. 스네이크 케이스(snake_case) 사용
   user # snake_case
   User # CamelCase
