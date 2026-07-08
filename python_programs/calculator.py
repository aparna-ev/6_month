print("Lets calculate.............")
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():

    n1=float(input("enter first number: "))
    again=True
    while again:
        n2=float(input("enter second number :"))
        for symbol in operation:
            print(symbol)
        operation_symbol=input("enter operation: ")
        answer=operation[operation_symbol](n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        choice=input("if you want to continue 'y' else 'n': ").lower()
        if choice=="y":
             n1=answer
        else:

             again=False
             print("\n"*20)
             calculator()

calculator()
