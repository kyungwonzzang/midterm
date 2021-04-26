#리스트, 딕셔너리, 함수 등을 추가해서 업데이트
import sys
item = ["비어있음"]
ability = { "대나무 헬리콥터" : "하늘을 날아 이동할 수 있다.",}
def 대나무헬리콥터():
    print("대나무 헬리콥터로 빠르게 이동합니다.")    

name = input("이름을 입력하시오: ")
hp1 = int(50)
hp2 = int(100)

if name == "노진구":
    print("노진구는 약해서 HP50 으로 시작합니다.")
    print(name, "님 반갑습니다. {0}( HP",hp1,")으로 게임을 시작합니다.".format(name))
else:
    print(name, "님 반갑습니다. {0}( HP",hp2,")으로 게임을 시작합니다.".format(name))

print("내 아이템 : ",item)
print("길을 가다가 퉁퉁이를 만났습니다.")
print("1.싸운다  2.도망간다")

num1 = int(input("선택: "))
if num1 == 1:
    print("퉁퉁이에게 이겼다 야호!!")
elif num1 == 2:
    print("도망가다 퉁퉁이에게 잡혀서 게임오버!!")
    sys.exit()
else:
    print("입력을 잘못 해서 게임오버!!")
    sys.exit()

print("퉁퉁이에게 빼았겼던 『대나무 헬리콥터』를 얻었다!!")
item.append("대나무 헬리콥터")
print("내 아이템 : ",item[1:])
action1 = input("아이템의 성능을 확인하려면 아이템 이름을 입력하세요. : ")
print(action1,"은(는)",ability[action1])

print("집으로 돌아갈 시간입니다.")
print("어떻게 집으로 갈 것입니까?")

num2 = int(input("1.걸어간다.   2.대나무 헬리콥터를 사용한다. : "))
if num2 == 1:
    print("집으로 걸어가다 복수하러 온 퉁퉁이에게 기습을 당했다.")
    print("기습을 당해서 게임오버!!")

elif num2 == 2:
    대나무헬리콥터()
    print("")
    print("도라에몽 게임 1일차 CLEAR!!!")