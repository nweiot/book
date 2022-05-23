
def login(id_user, pw_user):
    choice = input("1.회원가입\n2.로그인\n3.나가기")
    if choice == '1':
        id_user = input("등록할 아이디를 입력해주세요.")
        pw_user = input("등록할 비밀번호를 입력해주세요.")
        print("회원가입이 완료되었습니다.")
        login(id_user, pw_user)
    elif choice == '2':
        id = input("아이디를 입력해주세요.")
        pw = input("비밀번호를 입력해주세요.")
        if id_user == id and pw_user == pw:
            pass
        else:
            print("ID 또는 PW를 확인해주세요.")
            login(id_user, pw_user)
    elif choice == '3':
        exit(1)
    else:
        login(id_user, pw_user)

def search():
    choice=input("검색 방식 설정\n1.번호 조회\n2.도서 이름 조회\n3.저자 이름 조회\n4.종료")
일단 추가해봄



login(None, None)
