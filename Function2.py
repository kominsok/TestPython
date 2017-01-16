def add(a,b):
    print("add %d+%d"%(a,b))
    return a+b

def sub(a,b):
    print("sub %d-%d"%(a,b))
    return a-b

def mul(a,b):
    print("mul %d*%d"%(a,b))
    return a*b

def div(a,b):
    print("div %d/%d"%(a,b))
    return a/b

def choose_menu():
    print('원하는 연산을 고르세요')
    print('add,sub,mul,div,quit')
    return input('당신의선택은:')


menu={'add':add,'sub':sub,'mul':mul,'div':div}
choice=choose_menu()

while choice!='quit':
    if menu.get(choice):
        x=input('first value:')
        y=input('second value:')
        print(menu[choice](int(x),int(y)) )
        choice=choose_menu()