# 오늘 배울 것은 바로 상속 => 매우매우 중요하다.
# class 끼리는 두칸을 띄운다.

class Mother:
    _balance = 1000  #상속받게 하고 싶지 않을때 _를 붙인다.
    
    def house(self):
        return "판교 아파트"
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(self.name)
  

class Father:
    balance = 500
  
    def __init__(self, name):
        self.name = name
  

class Child(Mother, Father):
    fund = 30        #field는 한개밖에 상속 받지 못함.
    def __init__(self, name, age):
        print(super()._balance)
        super().__init__(name)
        self.age = age
        
        
    @property  #=> methd처럼 생겻지만 field처럼 쓸수있어 뒤에 ()를 사용하지 않아도 된다.
    def balance(self):
        sum = Mother.balance
        sum += Father.balance
        return sum
    
    #override   : 엄마한테 받은 기능을 사용하거나 더 추가 하고 싶을때 사용
    #def speak(self):
        #super().speak()
        #print(str(self.age)) #age는 숫자이므로 str를 써서 문자로 바꿔줘야댐
    
    # print(self.name + " " + str(self.age)) : 이렇게 해줘도 댐ㅁ 근데 오버라이드를 사요하면 엄마에게도 있는 speak를 사용할 수 있게 되어 더욱 좋다.
    
mother = Mother("이씨")  #=> 초기화함수 init에 보면 self와 name을 가지게 되어있으니 이름을 써줘야댐
father = Father("최씨")
child = Child("박씨", 10)
mother.speak()
child.speak()

# --------------------------------------------


    
    
    
    