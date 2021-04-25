#리스트, 딕셔너리, 함수 등을 추가해서 업데이트

name = input("이름을 입력하시오: ")
print(name, "님 반갑습니다. {0}(HP 100)으로 게임을 시작합니다.".format(name))
print("길을 가다가 퉁퉁이를 만났습니다.")
print("1.싸운다  2.도망간다")
num = int(input("선택: "))
if num == 1:
    print("퉁퉁이에게 이겼다 야호!!")
elif num == 2:
    print("도망가다 퉁퉁이에게 잡혀서 게임오버!!")
else:
    print("입력을 잘못 해서 게임 오버!!")