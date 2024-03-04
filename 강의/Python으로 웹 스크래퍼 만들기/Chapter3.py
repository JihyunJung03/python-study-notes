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
