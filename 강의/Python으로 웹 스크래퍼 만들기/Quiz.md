```py
Day 1

1. 파이썬으로 변수 만드는 방법?
   age = 20

2. 파이썬은 코드를 위에서 부터 아래로 읽어낸다.
   True

3. 변수명에 공백이 들어갈 수 있다.
   False

4. myName(변수이름) = "jihyun" (문자열 값)
   True(boolean 값 참(True) 또는 거짓(False) 두 가지 중 하나의 값을 가지는 데이터 유형)

5. 변수명은 숫자로 시작할 수 없다.

6. my_age = "34"
   변수의 데이터 타입은 String이다.

7. dead = "True"
   False

8. dead = true
   False => True의 앞글자가 대문자인 경우는 True가 성립된다. (PEP 285 참고)
            파이썬에 bool이 추가되던 당시, 빌트인 상수들이 모두 대문자로 시작했기에 일관성을 유지하기 위해 선택됐다.

9. false 와 False 은 같다.
   False => 대소문자를 구별하기 때문
```

```py
Day 2

1. 파이썬에서 함수를 생성하는 방법이 맞는가? False

fun say_hello():
    print("hello")

# 아래와 같이 코드를 수정해 준다.
def say_hello(): # 파이썬에서 함수를 생성할 때 def를 사용한다
	print("hello")


2. "화이팅"을 출력하는 cheer 함수가 실행되는가? False

def cheer():
    print("화이팅")

cheer

# 아래와 같이 코드를 수정해 준다.
def cheer():
    print("화이팅")

cheer() # 괄호 추가


3. start라는 함수를 실행할 때 어떻게 하는가?

start() # 함수이름()


4. 이 코드는 작동을 하는가? False

def hello():
print("hi!")

# 아래와 같이 코드를 수정해 준다.
def hello():
  print("hi!") # 반드시 탭, 띄워쓰기 2번으로 구분


5. 이 코드는 에러 없이 잘 돌아가는가? False

def alert():
    print("warning!!!")
alert("error detected")

# 위의 코드에서 alert() 함수는 인자를 받지 않지만,
# 함수를 호출할 때 "error detected" 문자열을 인자로 전달하려고 하고 있다.
# 여기서는 함수 정의에서 인자를 받지 않았으므로 함수 호출 시에도 인자를 전달하지 않는다.

# 따라서 아래와 같이 코드를 수정해 준다.

def alert():
    print("warning!!!")
alert()


6. 함수 이름의 첫글자로 숫자가 가능한가? False

# 함수 이름은 문자로 시작해야 하며 (a-z, A-Z) 또는 밑줄(_)로 시작할 수 있다.
# 이름의 뒷부분은 문자, 숫자, 또는 밑줄로 이루어질 수 있다.


7. 이 코드는 에러 없이 잘 돌아가는가? False

def alert(error):
    print("warning!!!", error)
alert()

# alert() 함수를 정의할 때 error라는 인자를 필요로 하고 있지만,
# 함수를 호출할 때 인자를 전달하지 않고 있으므로 코드에 오류가 발생한다.
# 함수를 호출할 때는 함수가 정의될 때와 동일한 개수의 인자를 전달해야 한다.
# 따라서 아래와 같이 코드를 수정해 준다.

def alert(error):
    print("warning!!!", error)

alert("error detected")  # "error detected" 문자열을 인자로 전달한다.
```
