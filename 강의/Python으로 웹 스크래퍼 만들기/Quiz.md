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

```py
playing = True

while playing:
  a = int(input("Choose a number:\n"))
  b = int(input("Choose another one:\n"))
  operation = input(
      "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
  )
  if operation == "+":
    print("Result: ", a + b)
  elif operation == "-":
    print("Result: ", a - b)
  elif operation == "*":
    print("Result: ", a * b)
  elif operation == "/":
    print("Result: ", a / b)
  elif operation == "exit":
    playing = False
```

```py
Day 3

1. get_yearly_revenue (연간 매출 계산)
monthly_revenue (월간 매출)를 인수로 받고, revenue for a year (연간 매출)를 리턴.

def get_yearly_revenue(monthly_revenue):
  return monthly_revenue * 12

2. get_yearly_expenses (연간 비용 계산)
monthly_expenses (월간 비용)를 인수로 받고, expenses for a year (연간 비용)를 리턴.

def get_yearly_expenses(monthly_expenses):
  return monthly_expenses * 12

3. get_tax_amount (세금 계산)
# profit (이익) 를 인수로 받고, tax_amount (세금 금액) 를 리턴.
# Requirements (요구사항)
# get_tax_amount 함수는 if/else 를 사용해야한다.
# 만약 (if) profit이 100,000 초과이면. 세율은 25% 이다.
# 아닌 경우에는 (else). 세율은 15% 이다.

def get_tax_amount(profit):
  if profit > 100000:
    return profit * 0.25

  else:
    return profit * 0.15

4. apply_tax_credits (세액 공제 적용)
tax_amount (세금 금액), tax_credits (세액 공제율)를 인수로 받고, amount to discount (할인할 금액)를 리턴.

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount * tax_credits


monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
```

```py
Day 4

# 사칙연산 구현하기
playing = True

while playing:
  a = int(input("Choose a number:\n"))
  b = int(input("Choose another one:\n"))
  operation = input(
      "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
  )
  if operation == "+":
    print("Result: ", a + b)
  elif operation == "-":
    print("Result: ", a - b)
  elif operation == "*":
    print("Result: ", a * b)
  elif operation == "/":
    print("Result: ", a / b)
  elif operation == "exit":
    playing = False

```

```py
Day 5

1. print()은 "메소드"이고 'nico'.upper()는 "함수"다. False
# print()은 파이썬 내장 함수이며 객체에 속하지 않기 때문에 메소드가 아니다.
# 'nico'.upper()는 문자열 객체의 메소드로 호출되는 함수이므로 함수이다.

2. 메소드란 무엇인가? 파이썬 객체에 속한 함수들

3. 리스트는 변경 가능하다. True

4. 튜플은 변경 불가능하다. False

튜플은 변경 불가능한 데이터 타입으로, 한 번 생성되면 수정할 수 없다.

5. 🍎에 대하여 어떻게 접근하는가?
food = ['🍔', '🍕', '🍌', '🍎', '🥑'] 정답 : food[3]

🍎는 리스트의 네 번째 요소이므로 인덱스 3으로 접근한다.

6. 🍕에 대하여 어떻게 접근하는가?
food = ('🍔', '🍕', '🍌', '🍎', '🥑') 정답 : food[-4]

🍕는 튜플의 두 번째 요소이므로 음수 인덱스 -4로 접근한다.

7. 딕셔너리는 변경 불가능하다. False

딕셔너리는 변경 가능한 데이터 타입으로, 요소를 추가, 수정, 삭제할 수 있다.

8. 리스트와 튜플은 숫자만 포함할 수 있다. False

리스트와 튜플은 숫자뿐만 아니라 다양한 데이터 타입의 요소를 포함할 수 있다.

9. 튜플의 리스트를 만들 수 있다. True

리스트 안에 튜플을 요소로 포함시킬 수 있다.

```

```py
Day 6

1. OOP는 무엇을 의미하는가? - 객체 지향 프로그래밍(Object Oriented Programming)

2. OOP는 파이썬에만 존재한다. - False
 # OOP(Object Oriented Programming)은 프로그래밍 패러다임 중 하나로,
 # 파이썬 뿐만 아니라 다양한 프로그래밍 언어에서 지원한다. 파이썬은 OOP를 지원하는 언어 중 하나일 뿐이다.

3. OOP를 사용하려면 파이썬 설정 화면에서 활성화해야 한다. - False
# OOP를 사용하려면 별도의 설정이 필요하지 않다.
# # OOP는 프로그래머가 선택하는 프로그래밍 패러다임 중 하나이며,
# 언어 자체에서 내장된 기능이 아니기 때문에 파이썬 설정 화면에서 활성화할 필요가 없다.

4. OOP란 무엇인가? - 코드를 구성하는 패러다임(Paradigm for organizing code)

5. 메소드(Method)란 무엇인가? - 클래스 내부의 함수(Function)

6. 클래스의 init 메소드는 클래스가 인스턴스화될 때 자동으로 호출된다. - True

7. 클래스 메소드가 받는 첫 번째 인자는 무엇인가? - 클래스의 인스턴스에 대한 참조(A reference to the instance of the class)

8. Human("nico")를 만들려면 Human의 init 메소드는 어떻게 보여야 하는가? __init__(self, name)

9. 클래스의 인스턴스를 출력하려고 할 때 파이썬이 자동으로 호출하는 메소드는 무엇인가? False

# 클래스의 인스턴스를 출력하려고 할 때 호출되는 메소드는 __str__이다. __str__ 메소드는 객체를 문자열로 표현할 때 호출되는 특수 메소드이다.

10. 클래스에는 init 및 str 두 개의 밑줄 메소드만 있다.  False
# 클래스에는 __init__ 및 __str__ 외에도 다른 밑줄 메소드들이 존재한다. 예를 들어, __repr__, __len__, __getitem__, __setitem__ 등 다양한 밑줄 메소드들이 있다.

11: 상속을 왜 사용하는가? - 많은 클래스들 간에 공통 속성 및 메소드를 공유하기 위해

12: Woman 클래스가 Human 클래스를 상속하도록 하려면 어떻게 해야 하는가?  class Woman(Human)

13: super()는 무엇을 가리키는가? 부모 클래스(Parent class)

14: 클래스가 다른 클래스를 상속할 때 무엇을 상속하는가?
  메소드, 속성(Methods, properties)

15: Woman 및 Man 클래스가 Human의 하위 클래스인 경우 Woman이 Human에 없는 고유한 메소드를 가질 수 있고 또한 Man과는 다른 속성을 가질 수 있는가? - True

```
