# 1. 출력 함수 : print()

# 표준 출력
print('Hello') # 결과 Hello
print('World!') # 결과 World!

# 한줄 연결 출력
print('Hello', end='') #end를 사용하면 위 아래 print문을 연결하게 된다.
print('World')
# 결과 HelloWorld!

print('Hello', 'World!') # 결과 Hello World!
print('Hello' + 'World!') # 결과 HelloWorld!

# 1-2.  입력 함수 : input()
# 입력받은곳에 기억을 해야하기 때문에 사용자가 어떤 값을 입력하게 하고, 
# 그 값을 변수에 저장한다
# input("메시지")

# 표준 입력
x = input()

x = input('x입력 :')
y = input('y 입력 :')

# 표준 출력
print(x, '+',y, '=' ,x+y)
x 입력 : 10 
y 입력 : 5
10 + 5 = 15
