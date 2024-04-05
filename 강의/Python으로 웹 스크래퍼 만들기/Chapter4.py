# DATA STRUCTURES

# 1. methods 
# 데이터에 연결된 함수 , 데이터의 안에 존재한다. 소괄호()를 쓰면 실행한다는 뜻이다.

print("nico".upper()) #대문자로 변경해주기
# 결과 NICO

print("nico".endswith("a")) #nico가 a로 끝나는지? 
# 결과 False
# 함수가 독립적으로 사용된다면 '함수'라고 하지만, 데이터에 결합된 함수는 '메소드'라고 부른다.

# 2. list
# 값들의 목록을 정렬할 수 있게 해준다.

number = [5, 3, 1, 5, 7, "True", True]
# number, boolean,string도 상관없다.
# 다양한 메소드가 있다. number.reverse(반대로),sort(정렬),remove,count


number.append(["🍕","🍔"])
print(number)
number.clear()
print(number)

#결과
[5, 3, 1, 5, 7, "True", True,["🍕","🍔"]]
[]

# 3. Tuple 
# ()괄호 사용 , 영원히 변경하지 못하는 데이터를 만들때, 수정하려면 clear해주고 다시 작성
number = (5, 3, 1, 5, 7, "True", True)
# number.count와 index만 있다.

# 4. Dictionary
# 중괄호를 사용하여 만들며 tuple도 가능하다.
# 데이터 수정 및 업데이트가 가능하다.

player = {
  'name' : "nico",
  'age' : 12,
  'alive' : True,
  'fav_food' : ("🍕","🍔"),
  'friend' : {
    'name': 'lynn',
    'fav_food': ["🍕"]
    }
}

print(player["friend"]["fav_food"])

### list, tuple, dictionary

days = ["Mon","Tue"] # list 대괄호 사용한다.
days =("Mon","Tue") # tuple 소괄호 사용한다.

days =("Mon","Tue")
days # days.count index 사용가능함


# 튜플은 불변하기 때문에 튜플을 만들면 그 내용을 변경할 수 없다.
# 튜플을 만들 때는 소괄호()를 써야하고, 그 안의 아이템에 접근할 때는 [] 대괄호를 써야한다.
# 튜플,리스트 둘다 0부터 시작하는 것 대신에 -1로 시작할 수 있다.
# 리스트와의 차이점이다.(리스트는 다양한 메소드 사용 가능)

days =("Mon","Tue")
print(days[0])
# 결과 : Mon , 리스트에서 했던 것처럼 인덱스로 아이템에 접근 가능하다.

days =("Mon","Tue","Wed")
print(days[-1])
# 결과: Wed 튜플,리스트 둘다 0부터 시작하는 것 대신에 -1로 시작할 수 있다.


### Dictionary

# {} 사용 , 리스트 처럼 변경 가능하다 변경 불가능한것은 튜플
# 딕셔너리에서는 키-값 쌍으로 이뤄져있다.
# 값으로는 string, number, boolean, list 등 어떤것이든 가능하다.

player = {
	'name' : 'nico', #string
	 'age': 12, #number
	 'alive': True #blooean
}
print(player)
# 결과 : {'name' : 'nico', 'age': 12,'alive': True }

print(player.methods) # methods에 get등 사용가능

player = {
	'name' : 'nico',
	 'age': 12,
	 'alive': True
}
print(player.get('age'))
# 결과 : 12

# 인덱스에서는 get[0] 이런식으로 적어야했다. 정렬되어있으니까.

player = {
	'name' : 'nico',
	 'age': 12,
	 'alive': True,
	 'fav_food': ["🍕","🍔"]
}
print(player.get('age'))
print(player.get('fav_food'))

# 결과
# 12
# ['🍕','🍔']

print(player['fav_food'])
# 결과 ['🍕','🍔']

#### 1) pop(키를 지운다)
player = {
	'name' : 'nico',
	 'age': 12,
	 'alive': True,
	 'fav_food': ["🍕","🍔"] #array
}
player.pop('age')
print(player)

# 결과 {'name' : 'nico','alive' : True, 'fav_food' : ["🍕","🍔"]}

### 2) xp추가해보기
player = {
	'name' : 'nico',
	 'age': 12,
	 'alive': True,
	 'fav_food': ["🍕","🍔"] #array
}
print(player)
player['xp'] = 1500
print(player)
# 결과 {'name' : 'nico', 'age': 12,'alive': True,'fav_food': ["🍕","🍔"]}
# 결과 {'name' : 'nico', 'age': 12,'alive': True,'fav_food': ["🍕","🍔"], 'xp': 1500}


### 3) append(추가)
player = {
	'name' : 'nico',
	 'age': 12,
	 'alive': True,
	 'fav_food': ["🍕","🍔"] #array
}
player['fav_food'].append('🍟')
print(player.get('fav_food'))
print(player['fav_food'])

# 결과 ["🍕","🍔","🍟"]
# 결과 ["🍕","🍔","🍟"]




