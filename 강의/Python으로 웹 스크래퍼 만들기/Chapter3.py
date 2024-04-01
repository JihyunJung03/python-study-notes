# If,Else,Elif 사용법

# 3가지 모두 조건부로 코드를 실행할 수 있게 해준다. 즉 내 코드를 어떤 조건에서 실행할지 정할 수 있다.
# if,elif,else 를 사용할 때는 조건을 정해야 한다.
# 들여쓰기에 항상 주의하자.
# 조건문에 사용되는 등호는 다음과 같다. > 크다, >= 크거나 같다, < 작다, <= 작거나 같다, == 같다, != 같지않다

# 1. if
# elif,else 와 같이 사용하게되는 경우 if에서 true의 결과가 나올 시 그 뒤의 코드는 실행하지 않는다.

winner = 5 #wineer 변수에 5를 저장한다.

if winner < 10:
  print("run!") #winner가 10보다 작으면 run!를 출력한다.

# winner가 5, 조건이 참이기 때문에 run!이 출력된다.


# 2. else
# 모든 경우가 false일 때 실행한다.
# else를 사용하는것은 선택사항이다.

winner = 50 #winner 변수에 50을 저장한다.

if winner < 10: #winner가 10보다 작으면
  print("if") #if를 출력한다.

else: #아니면
  print("else") #else를 출력한다.

# winner가 50, if 조건이 false, 즉 else를 출력한다.

# 3. elif
# 또다른 대안과 조건을 넣을 수 있도록 해준다.
# elif를 사용하는것은 선택사항이다.
# 무한대로 생성이 가능하다.

winner = 50 #winner 변수에 50을 저장한다.

if winner != 10: #winner가 10이 아니면
  print("if")#if를 출력한다.

elif winner <= 25: #아니면 winner가 25보다 작거나 같으면
  print("elif") #elif를 출력한다.

elif winner ==0 : #아니면 winner가 0일 경우
  print("elif 2") #elif 2를 출력한다.

elif winner ==50 : #아니면 winner가 50일 경우
  print("elif 3") #elif 3를 출력한다.

else: #아니면
  print("else") #Else를 출력한다.

# winner가 50, if 조건이 false, 3가지 elif 중 true인 elif3이 출력된다.
  


# And,Or 사용법

# And는 양쪽 조건 모두 충족되어야 한다.
# Or은 둘 중 하나가 true여야 한다.
# input("") - input은 오직 하나의 argument만 받는다.
# input("How old are you?") - 단순한 print가 아니다. value를 print하기도 하지만 응답을 기다리고 있다.
# console창에서 보면 How old are you?라고 뜨는데, 이후에 정지를 누르면 함수와 프로그램이 끝난다. 
# 하지만 멈춤 버튼을 누르지 않는다면 실행 상태로 대답을 기다린다. 해당 대답에 입력하고 엔터 누르면 그제야 프로그램이 끝난다.

# 함수의 반환 값을 변수로 저장해둔다.
age = input("How old are you?") # 36 입력 후 엔터

print("user answer", age) 
# user answer 36


type(age) #type 함수

print(type(age)) # age변수의 type을 print해서 어떤 type인지 확인해 본다. <class 'str'> 로 나옴
# 보는 것처럼 age 변수의 type이 'str(string)'인 것을 확인할 수 있다.

age = input("How old are you?")
print("user answer", age)  # type이 string으로 인식된다.

age = int(input("How old are you?")) # int는 user가 작성한 string을 받고, int는 그 string을 숫자로 바꾸어 준다.


#and는 if와 elif에 모두 적용할 수 있다. 양쪽 부분이 모두 true여야한다.

if age < 18 :
	print("You can't drink.")
elif age > 18 and age < 35 :
	print("You drink beer!") # 동시에 두 가지 조건을 확인해 준다.
else :
	print("Go ahead!")
# 18세 초과인 사람들을 나타냄, 즉 18세와 35세는 포함되지 않음


if age < 18 :
	print("You can't drink.")
elif age >= 18 and age <= 35 :
	print("You drink beer!") # 동시에 두 가지 조건을 확인해 준다.
else :
	print("Go ahead!")
# 18보다 크거나 같은지 따라서 18세 이상의 사람들을 잡아냄


if age < 18 :
	print("You can't drink.")
elif age >= 18 and age <= 35 :
	print("You drink beer!") # and는 양쪽 모두 true여야 한다. 동시에 두가지 조건을 확인해줌 
elif age == 60 or age == 70 : # or는 둘중 하나가 true여야 한다.
	print("Birthday party!")
else :
	print("Go ahead!")
# 60세라고 입력 Birthday party!가 뜬다.


# True and True == True
# False and True == False
# True and False == False
# False and False == False
# and는 두조건 모두 true여야 조건 성립이 된다.

# True or True == True
# True or False == True
# Flase or True == True
# False or False == False
# or는 오로지 한쪽이 true여도 괜찮다
	
# randint 사용법

### 랜덤한 숫자 주고 맞추기

user_choice = int(input("Choose number."))
pc_choice = 50

# 흐름제어 Control flow
if user_choice == pc_choice: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower!")
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher!") 


user_choice = int(input("Choose number."))
# pc_choice = random.randint(1,50) 
# 이 경우 동작하지 않는다. 이유는 random이라는 이름이 지정되지 않았기 때문이다.
# 즉 random은 모듈 이름이기 때문

if user_choice == pc_choice: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower!")
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher!") 


from random import randint
user_choice = int(input("Choose number."))
pc_choice = randint(1,50) 

# random이 모듈의 이름이니까 random 모듈에서 from randint function을 import 해준다.
# 'from 이 모듈에서 이 함수를 import 해줘'

# ramdom 모듈이 Python Standard Library에 기본적으로 포함되어 있다.

# randint(a,b) 이 function은 random한 정수 N을 반환한다.

# 즉 첫번째 parameter a는 N보다 작거나 같고, N은 두번째 parameter b보다 작거나 같다.


if user_choice == pc_choice: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher! Computer chose", pc_choice) 

# 50을 입력했을때
# 결과 Lower! Computer chose 44
	

