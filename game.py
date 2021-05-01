#리스트, 딕셔너리, 함수 등을 추가해서 업데이트
import sys
item = ["비어있음"]
ability = { "대나무 헬리콥터" : "하늘을 날아 이동할 수 있다.", "공기포" : "근접에서 사용시 상대방을 제압할수있다.",
            "단팥빵" : "먹으면 hp를 30 회복한다."}
def 대나무헬리콥터():
    print("대나무 헬리콥터로 빠르게 이동합니다.")
def 공기포():
    print("공기포로 상대방을 제압합니다.")
def 단팥빵():
    print("단팥빵을 먹고 hp 30 을 회복합니다.")

name = input("이름을 입력하시오: ")
print("")

hp1 = int(50)
hp2 = int(100)

if name == "노진구":
    print("노진구는 약해서 HP50 으로 시작합니다.")
    print(name, "님 반갑습니다. ( HP",hp1,")으로 게임을 시작합니다.".format(name))
    nowhp = int(hp1)
else:
    print(name, "님 반갑습니다. ( HP",hp2,")으로 게임을 시작합니다.".format(name))
    nowhp = int(hp2)
print("내 아이템 : ",item)
print("")

print("길을 가다가 퉁퉁이를 만났습니다.")
print("1.싸운다  2.도망간다")
num1 = int(input("선택: "))
print("")

if num1 == 1:
    print("퉁퉁이에게 이겼다 야호!!")
    print("")
elif num1 == 2:
    print("도망가다 퉁퉁이에게 잡혀서 게임오버!!")
    sys.exit()
else:
    print("입력을 잘못 해서 게임오버!!")
    sys.exit()


print("퉁퉁이에게 빼았겼던 『대나무 헬리콥터』를 얻었다!!")
item.append("대나무 헬리콥터")
print("내 아이템 : ",item[1:])
print("")

action1 = input("아이템의 성능을 확인하려면 아이템 이름을 입력하세요. : ")
print(action1,"은(는)",ability[action1])
print("")

print("집으로 돌아갈 시간입니다.")
print("")

print("어떻게 집으로 갈 것입니까?")
num2 = int(input("1.걸어간다.   2.대나무 헬리콥터를 사용한다. : "))
print("")
print("집으로 가는중 ...")
print("")

if num2 == 1:
    print("집으로 걸어가다 바닥에 떨어진 공기포를 주웠다")
    item.append("공기포")
    print("내 아이템 : ",item[1:])
    print("")

    action2 = input("아이템의 성능을 확인하려면 아이템 이름을 입력하세요. : ")
    print(action2,"은(는)",ability[action2])
    print("")

    print("집으로 가는중 ...")
    print("")

    print("집으로 걸어가다 복수하러 온 퉁퉁이에게 기습을 당한다.")
    nowhp = nowhp - 20
    print("20의 피해를 입었다. 현재 ( HP",nowhp,")")
    print("")

    print("아이템을 사용하세요.")
    print("내 아이템 : ",item[1:])
    print("")

    action3 = input("사용할 아이템 입력 : ")
    if action3 == "대나무 헬리콥터":
        대나무헬리콥터()
        print("")

        print("대나무 헬리콥터를 이용해 날아가려다 퉁퉁이에게 붙잡혀서 게임오버")
        sys.exit()
    
    elif action3 == "공기포":
        공기포()
        print("퉁퉁이에게 이겼다 야호!!")
        print("")

        print("퉁퉁이를 제압하고 단팥빵을 얻었다.")
        item.append("단팥빵")
        print("내 아이템 : ",item[1:])
        print("")

        action4 = input("아이템의 성능을 확인하려면 아이템 이름을 입력하세요. : ")
        print(action4,"은(는)",ability[action4])
        print("집으로 가는중 ...")
        print("")

        print("집에 도착하였습니다.")

        print("")
        print("집에서 무엇을 할까요")
        num3 = int(input("1.잠을 잔다.  2.단팥빵을 먹고 잔다. : "))
        print("")

        if num3 == 1:
            print("현재 체력 ( hp",nowhp,")")
            print("잠을 잡니다.")
            print("")

            print("도라에몽 게임 1일차 CLAER!!!")

        elif num3 == 2:
            단팥빵()
            nowhp = nowhp + 30
            print("현재 체력 ( hp",nowhp,")")
            print("잠을 잡니다.")
            print("")

            print("도라에몽 게임 1일차 CLAER!!!")

elif num2 == 2:
    대나무헬리콥터()
    print("집으로 가는중 ...")
    print("")

    print("집에 도착하였습니다.")
    print("")

    print("현재 체력 ( hp",nowhp,")")
    print("잠을 잡니다.")
    print("")

    print("도라에몽 게임 1일차 CLAER!!!")