class BST:
    def __init__(self, b_num, b_name, b_outher, b_type):
        self.num = b_num
        self.name = b_name
        self.outher = b_outher
        self.type = b_type
        self.decount = 0

shopping_bag=[]

booklist = [
    BST('1', '김종욱책', '김종욱', 1),
    BST('2', '양현동책', '양현동', 1),
    BST('3', '김류은책', '김류은', 1)
]

a = 4

def book_in():
    global a
    b = input("도서 이름을 입력해 주세요:")
    c = input("저자를 입력해주세요:")
    d = input("기증할 책의 수량을 입력해주세요:")
    booklist.append(BST(f"{a}", b, c, d))
    a += 1
    return 1

def login(id_user, pw_user):
    choice = input("1.회원 가입\n2.로그인\n3.나가기\n 입력:")
    if choice == '1':
        id_user = input("등록할 아이디를 입력 해 주세요.:")
        pw_user = input("등록할 비밀 번호를 입력 해 주세요.:")
        print("회원 가입이 완료 되었 습니다.")
        login(id_user, pw_user)
    elif choice == '2':
        id = input("아이디를 입력 해 주세요.:")
        pw = input("비밀번호를 입력 해 주세요.:")
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
    choice=input("검색 방식 설정\n1.번호 조회\n2.도서 이름 조회\n3.저자 이름 조회\n4.종료\ng.도서기증하기\nc.장바구니\n입력:")
    if choice=="1":
        return 1
    elif choice=="2":
        return 2
    elif choice == "3":
        return 3
    elif choice == "4":
        exit(1)
    elif choice == "g":
       book_in()
       return scan()
    elif choice == "c":
        choice=input(f"{shopping_bag[:]}\np.대여하기\nc.둘러보기")
        if choice == 'p':
            print(f"{shopping_bag[:]}를 대여 합니다.")
            exit(1)
        elif choice == 'c':
            return scan()
    else:
        print("잘못 입력 하셨 습니다.")
        return scan()

def search(num):
        if num == 1:
            s = input("조회할 번호를 입력해주세요:")
            for a in booklist:
                if(a.num == s):
                    return b_choice(a)
        elif num == 2:
            s = input("조회할 도서명을 입력해주세요:")
            for a in booklist:
                if(a.name == s):
                    return b_choice(a)
        elif num == 3:
            s = input("조회할 도서의 저자를 입력해주세요:")
            for a in booklist:
                if(a.outher == s):
                    return b_choice(a)
        else:
            print("잘못 입력 하셨 습니다. 다시 입력해 주세요.")
            return search(num)

def b_choice(a):
    print("=" * 20, "\n" f"번호:{a.num}\n책이름:{a.name}\n저자:{a.outher}\n대출 가능 권수:{a.type}권", "\n", "=" * 20, "\n")
    if a.type == '0':
        print("아쉽지만 대여 가능한 도서가 없습니다.")
        return 0
    choice = input("1. 장바구니에 넣기\n2.나가기")
    if choice == '1':
        print(f"장바구니에 {a.name}이 담겼습니다.")
        return a.num
    elif choice == '2':
        print("나가기를 선택하셨습니다.")
        return 0
    else:
        print("잘못입력하셨습니다.")
        return b_choice(a)

def sopping(num):
    for a in booklist:
        if a.num == num:
            shopping_bag.append(a.name)

login(None, None)
while 1:
    num = scan()
    num = search(num)
    sopping(num)