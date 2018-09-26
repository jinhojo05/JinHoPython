# 복권 번호 만들기

def Lotto():
    import random
    List_number = []


    for i in range(0, 5):

        while True:
            a = random.randrange(1, 15)
            if List_number.count(a)==0:
                break

        List_number.append(a)

    List_number.sort()

    return List_number



# 복권 번호와 번호랑 비교해서 같은 개수 리턴해주는 함수
def Match( A, B ):
    coMatch = 0

    return coMatch


# 프로그램 시작
list_ = []
List_lotto = []
List_Robort = []
List_lotto = Lotto()


a = int(input('숫자를 입력하세요 :'))
b = int(input('숫자를 입력하세요 :'))
c = int(input('숫자를 입력하세요 :'))
d = int(input('숫자를 입력하세요 :'))
e = int(input('숫자를 입력하세요 :'))
list_ = [a]
list_.append(b)
list_.append(c)
list_.append(d)
list_.append(e)


print ('이번 당첨 번호 : ', List_lotto)

coMatch = Match( List_Lotto, list_ )
print ('당신의 숫자 : ', list_, '맞흰 개수:' , coMatch)
for x in range(1, 10):
    List_Robort = Lotto()
    coMatch = Match( List_lotto, List_Robort )
    print ('로봇' , x,'의 숫자:', List_Robort, coMatch)

