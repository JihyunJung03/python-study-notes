# 파이썬 조건문 사용하기

### If,Else,Elif 사용법

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

# And,Or사용법

1. And는 양쪽 조건 모두 충족되어야 한다.
2. Or은 둘 중 하나가 true여야 한다.

### type(age) type 함수

print(type(age)) # age변수의 type을 print해서 어떤 type인지 확인해 본다.<br/>
보는 것처럼 age 변수의 type이 'str(string)'인 것을 확인할 수 있다.<br/>

age = input("How old are you?")<br/>
print("user answer", age) type이 string으로 인식된다.<br/>

age = int(input("How old are you?"))<br/>
int는 user가 작성한 string을 받고, int는 그 string을 숫자로 바꾸어 준다.<br/>

### and는 if와 elif에 모두 적용할 수 있다. 양쪽 부분이 모두 true여야한다.

if age < 18 :<br/>
print("You can't drink.")<br/>
elif age > 18 and age < 35 :<br/>
print("You drink beer!") # 동시에 두 가지 조건을 확인해 준다.<br/>
else :<br/>
print("Go ahead!") <br/># 18세 초과인 사람들을 나타냄, 즉 18세와 35세는 포함되지 않음<br/>

if age < 18 :<br/>
print("You can't drink.")<br/>
elif age >= 18 and age <= 35 :<br/>
print("You drink beer!") # 동시에 두 가지 조건을 확인해 준다.<br/>
else :<br/>
print("Go ahead!") # 18보다 크거나 같은지 따라서 18세 이상의 사람들을 잡아냄<br/>

if age < 18 :<br/>
print("You can't drink.")<br/>
elif age >= 18 and age <= 35 :<br/>
print("You drink beer!") # and는 양쪽 모두 true여야 한다. 동시에 두가지 조건을 확인해줌<br/>
elif age == 60 or age == 70 : # or는 둘중 하나가 true여야 한다.<br/>
print("Birthday party!")<br/>
else :<br/>
print("Go ahead!") # 60세라고 입력 Birthday party!가 뜸.<br/>

True and True == True<br/>
False and True == False<br/>
True and False == False<br/>
False and False == False<br/>

### and는 두조건 모두 true여야 조건 성립이 된다.

True or True == True<br/>
True or False == True<br/>
Flase or True == True<br/>
False or False == False<br/>

### or는 오로지 한쪽이 true여도 괜찮다.
