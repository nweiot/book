class BST:
    def __init__(self):
        self.name = 0
        self.num = 0
        self.outher = 0

a=BST()
b=BST()
c=BST()

a.num=1
b.num=2
c.name=3
a.name="종욱이의 기묘한 모험"
b.name="현동 왕자와 복이 공주"
c.name="김류은"
a.outher="김종욱"
b.outher="양현동"
c.outher="김류은"


def login(id_user, pw_user):
    choice = input("1.회원 가입\n2.로그인\n3.나가기")
    if choice == '1':
        id_user = input("등록할 아이디를 입력 해 주세요.")
        pw_user = input("등록할 비밀 번호를 입력 해 주세요.")
        print("회원 가입이 완료 되었 습니다.")
        login(id_user, pw_user)
    elif choice == '2':
        id = input("아이디를 입력 해 주세요.")
        pw = input("비밀번호를 입력 해 주세요.")
        if id_user == id and pw_user == pw:
            pass
        else:
            print("ID 또는 PW를 확인해주세요.")
            login(id_user, pw_user)
    elif choice == '3':
        exit(1)
    else:
        login(id_user, pw_user)

def scan():
    choice=input("검색 방식 설정\n1.번호 조회\n2.도서 이름 조회\n3.저자 이름 조회\n4.종료")
    if choice=="1":
        return 1
    elif choice=="2":
        return 2
    elif choice == "3":
        return 3
    elif choice == "4":
        exit(1)
    else:
        print("잘못 입력 하셨 습니다.")
        return scan()

def search(num):
    if num == 1:
        s = input("조회할 번호를 입력해주세요:")

    elif num == 2:
        s = input("조회할 도서명을 입력해주세요:")

    elif num == 3:
        s = input("조회할 도서의 저자를 입력해주세요:")


login(None, None)
num = scan()
search(num)
count=range(a, c)


