my_name = "jihyun"
age = 30
dead = False
print("Hello my name is", my_name)

def say_hello():
  print("hello how r u?")

say_hello()

# 차례대로 덧셈,뺄셈,곱셈,나눗셈,제곱을 사용해보았다.
# 인수에 값이 입력되지 않을 경우를 대비하여 기본값을 설정해주었다.

def plus(a=0,b=0): ## 기본값 설정해주기
  print(a+b)

plus(2,6) # 8
plus() # 0

def minus(a=0,b=0):
  print(a-b)

minus(2,5) # -3
minus() # 0

def multiply(a=0,b=0):
  print(a*b)

multiply(3,8) # 24
multiply() # 0

def divide(a=0,b=1): 
  print(a/b)

divide(8,3) # 2.6666666666666665
divide() # 0.0
divide(5) # 5.0

def square(a=0,b=1):
  print(a**b)

square(2,4) # 16
square() # 0

# return을 사용하여 함수를 실행시켜보았다.
# 변수를 사용하는 경우, 사용하지 않는 경우를 나누었다.

def tax_calc(money):
  return money * 0.35 # 함수 바깥으로 보낸다.

def pay_tax(tax):
  print("thank you for paying",tax)

#1. 변수를 선언하는 방법
to_pay = tax_calc(1500000) #money 
pay_tax(to_pay)

#2. 변수를 선언하지 않는 방법
pay_tax(tax_calc(1500000))

my_name = "jihyun"
my_age = "20"
my_color_eyes = "brown"

print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")

#f""는 format을 사용한다.
#f를 사용함으로써 string과 변수를 같이 사용할 수 있다.
#f를 사용할 때는 변수를 {}로 감싸서 사용한다.
#f를 사용할 때는 변수를 ,로 감싸서 사용한다.
#f를 사용할 때는 변수를 +로 감싸서 사용한다.
#return 키워드는 함수를 끝내기 때문에 return 이후의 코드는 실행되지 않는다.

def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍬"

juice = make_juice("🍎") #make_juice 함수를 실행한다.
cold_juice = add_ice(juice) #add_ice 함수를 실행한다.
perfect_juice = add_sugar(cold_juice) #add_sugar 함수를 실행한다.

print(perfect_juice)#perfect_juice를 출력한다.