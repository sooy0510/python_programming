"""
파이선 모듈안에는 함수와 클래스를 선언할 수 있다
"""

def add(n1,n2):
    #pass
    return n1+n2

print(type(add))
print(add(19,20))

# ctrl + shift + f10 실행

add2 = lambda n1,n2 : n1 + n2
print(type(add2))
print(add2(100,200))

#class 선언
class User:
    # 생성자 선언
    def __init__(self,name): #self는 java에서 this개념
        self.name = name

    # toString, toString없으면 주소를 호출
    def __str__(self):
        return self.name

#객체 생성
user = User("파이썬")
print(user)