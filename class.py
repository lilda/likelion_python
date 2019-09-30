class MyFirstClass:
    
    def __init__(self): #init 처음에 만들어주는 함수 self=자기자신
        self.color = "red"
    
    def change_color(self): #method는 함수안에서만 사용할수있다.
        self.color = "blue"
        

chair = MyFirstClass()
print(chair.color)
chair.change_color()
print(chair.color)



class MySecondClass:
    
    def __init__(self): 
        self.color = "red"
    
    def change_color(self, color): #color 지정하는게 아니라 사용자가 원하는 것을 받아주겠다.
        self.color = color
        

chair = MySecondClass()
print(chair.color)
chair.change_color("green") #green 이 color 가 된다.
print(chair.color)

class MyThirdClass:
    
    def __init__(self): 
        self.color = "red"
    
    def change_color(self, color="white"): #기봊값은 화이트로, 내가 바꾸고 싶을때는 내맘대로.
        self.color = color
        

chair = MyThirdClass()
print(chair.color)
chair.change_color() 
print(chair.color)
chair.change_color("green") 
print(chair.color)



class MyFourthClass:
    
    material = "wood"  #material = field / 이것은 처음시작에 무조건 이값으로 설정 
    
    def __init__(self): 
        self.color = "red"
    
    def change_color(self, color="white"): #기봊값(dafaut)은 화이트로, 내가 바꾸고 싶을때는 내맘대로.
        self.color = color
        

chair = MyFourthClass()  # chair = 오브젝트 / 클래스안에있는 객체에 접근한다.
chair.change_color()      # 오브젝트의 필드에 접근하겠다.
print(chair.color)
second_chair = MyFourthClass()
print(second_chair.color)
print("mmmmmmmmmmmmmmmmmmmmmm")
print(MyFourthClass.material)
chair.material = "plastic"
print(chair.material)
print(second_chair.material)

print("MMMMMMMMMMMMMMMMMMMMMM")
MyFourthClass.material = "water"  #wood 대신에 다 water로 바꿔줘 
chair1 = MyFourthClass()
chair2 = MyFourthClass()
MyFourthClass.material = "wood" # 다시 wood로 바꿔줘 
chair3 = MyFourthClass()
chair4 = MyFourthClass()

chair2.material = "air"

print(chair1.material)
print(chair2.material)
print(chair3.material)
print(chair4.material)

chair1.color = "red"


















