blogs = ["1", "2", "3"]

for blog in blogs:
    print(blog)
    
for i in range(1):
    # 0 ~ 9
    print("1") #반복할때 숫자(반복된 횟수)와 함께 1 출력
    
for _ in range(1):
    print("HEllo Django") #10번 반복할때 숫자는 보이지 않게
    
    
aaa = { "사과" : 1, "배": 2, "포도":3 , "바나나": 234} #dict="key":value

for k, v in aaa.items():
    print(k + " " + str(v))
    
def func(a, b):
    #def d():
        #print("1234")     #함수안에 함수를 사용할수있지만 하지말자. 함수안에서만 사용할수있음
    return a + b   # 숫자뿐만아니라 문자도 할수있다 abc+def = abcdef
    print(func(10, 20))    

def func2(f):
    print(f(10, 10))
    return

func2(func)

def plus(i, j):
    return i + j

def minus(i, j):
    return i - j

def triple_plus(i, j, l):
    return i + j + l

# args -> 파라미터가 몇개 필요한지 모르니, 첫 번째 이후 인자들을 모두 args라고 부르겠다. args는 리스트
def 출력(calc, *args):
    print(calc(*args))
    
출력(plus, 1, 2)
출력(minus, 1, 2)
출력(triple_plus, 1, 2, 3)
    

    