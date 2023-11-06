# def add():
#     a=int(input("enter a :"))
#     b=int(input("enter b:"))
#     sum=a+b
#     print(sum)
# def sub():
#     a=int(input("enter a :"))
#     b=int(input("enter b:"))
#     result=a-b
#     print(result)
# def div():
#     a=int(input("enter a :"))
#     b=int(input("enter b:"))
#     result=a/b
#     print(result)
# print("1. add \n 2. sub \n 3.div \n")
# while True:
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         add()
#     elif ch==2:
#         sub()
#     elif ch==3:
#         div()
#     else:
#         print("invalid")
#         break


# def add():
#     uiyuy
# list=[]
# while True:
#     print("/n create list:")
#     print("1.add element")

#     choice=input("enter the choice")
#     if choice==1:
#         print()

l=[]
def create():
    n=int(input("enter limit:"))
    for i in range(n):
        item=input("enter item:")
        l.append(item)
    print(l)

def add():
    item=input("enter item to add:")
    l.append(item)
    print(l)
def replace():
    n=int(input("enter item to replace:"))
    l.pop(n)
    new=input("enter new item:")
    l.insert(n,new)
    print(l)
def remove():
    item=input("enter item to remove:")
    l.remove(item)
    print(l)

def sort():
    item=input("enter item to sort")
    l.sort(item)
    print(l)
def exit():
    item=input("enter item to exit:")
    l.exit(item)
    print(l)
print("1. create \n 2. add \n 3. replace \n 4. remove \n 5. sort \n 6. exit \n")
while True:
    ch=int(input("enter the choice:"))
    if ch==1:
        create()
    elif ch==2:
        add()
    elif ch==3:
        replace()
    elif ch==4:
        remove()
    elif ch==5:
        sort()
    elif ch==6:
        exit()
    else:
        print("invalid")
        break

