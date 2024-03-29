# 파이썬 조건문 사용하기

### If, Else, Elif 사용법

1. 3가지 모두 조건부로 코드를 실행할 수 있게 해준다. 즉 내 코드를 어떤 조건에서 실행할지 정할 수 있다.
2. if,elif,else 를 사용할 때는 조건을 정해야 한다.
3. 들여쓰기에 항상 주의하자.
4. 조건문에 사용되는 등호는 다음과 같다.
5. \> 크다, >= 크거나 같다, < 작다, <= 작거나 같다, == 같다, != 같지않다

### If

1. if
2. elif,else 와 같이 사용하게되는 경우 if에서 true의 결과가 나올 시 그 뒤의 코드는 실행하지 않는다.

### Else

1. 모든 경우가 false일 때 실행한다.
2. else를 사용하는 것은 선택사항이다.

### Elif

1. 또다른 대안과 조건을 넣을 수 있도록 해준다.
2. elif를 사용하는 것은 선택사항이다.
3. 무한대로 생성이 가능하다.

<br/>

# And, Or사용법

1. And는 양쪽 조건 모두 충족되어야 한다.
2. Or은 둘 중 하나가 true여야 한다.

### type(age) type 함수

```py
print(type(age))
# age변수의 type을 print해서 어떤 type인지 확인해 본다.
# age 변수의 type이 'str(string)'인 것을 확인할 수 있다.

age = input("How old are you?")
  print("user answer", age) # type이 string으로 인식된다.

age = int(input("How old are you?"))
# int는 user가 작성한 string을 받고, int는 그 string을 숫자로 바꾸어 준다.
```

### and는 if와 elif에 모두 적용할 수 있다. 양쪽 부분이 모두 true여야한다.

```py
if age < 18 :
  print("You can't drink.")
elif age > 18 and age < 35 :
  print("You drink beer!")
# 동시에 두 가지 조건을 확인해 준다.
else :
  print("Go ahead!")
# 18세 초과인 사람들을 나타냄, 즉 18세와 35세는 포함되지 않는다.
```

```py
if age < 18 :
  print("You can't drink.")
elif age >= 18 and age <= 35 :
  print("You drink beer!")
# 동시에 두 가지 조건을 확인해 준다.
else :
  print("Go ahead!")
#  18보다 크거나 같은지 따라서 18세 이상의 사람들을 잡아낸다.
```

```py
if age < 18 :
  print("You can't drink.")
elif age >= 18 and age <= 35 :
  print("You drink beer!")
# and는 양쪽 모두 true여야 한다. 동시에 두가지 조건을 확인해준다.
elif age == 60 or age == 70 :
# or는 둘중 하나가 true여야 한다.
  print("Birthday party!")
else :
  print("Go ahead!")
# 60세라고 입력 Birthday party!가 뜬다.
```

### and는 두조건 모두 true여야 조건 성립이 된다.

True and True == True<br/>
False and True == False<br/>
True and False == False<br/>
False and False == False<br/>

### or는 한쪽만 true여도 조건 성립이 된다.

True or True == True<br/>
True or False == True<br/>
Flase or True == True<br/>
False or False == False<br/>

# randint 사용법

### 랜덤한 숫자 맞추기

```py
user_choice = int(input("Choose number."))
pc_choice = 50

흐름제어 Control flow
if user_choice == pc_chioce: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower!")
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher!")
```

```py
user_choice = int(input("Choose number."))
pc_choice = random.randint(1,50)

# 이 경우 동작하지 않는다. 이유는 random이라는 이름이 지정되지 않았기 때문이다.
# 즉 random은 모듈 이름이기 때문.

흐름제어 Control flow
if user_choice == pc_chioce: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower!")
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher!")
```

```py
from random import randint
user_choice = int(input("Choose number."))
pc_choice = randint(1,50)

# random이 모듈의 이름이니까 random 모듈에서 from randint function을 import 해준다.
# 'from 이 모듈에서 이 함수를 import 해줘'

# amdom 모듈이 Python Standard Library에 기본적으로 포함되어 있다.

# randint(a,b) 이 function은 random한 정수 N을 반환한다.

# 즉 첫번째 parameter a는 N보다 작거나 같고, N은 두번째 parameter b보다 작거나 같다.


if user_choice == pc_chioce: # 동일한 경우
	print("You won!")
elif user_choice > pc_choice: # user가 pc보다 큰 경우
	print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice: # user가 pc보다 작은 경우
	print("Higher! Computer chose", pc_choice)

50을 입력했을때
결과 Lower! Computer chose 44

```
