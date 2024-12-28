peo =[]
p1={}
n=int(input('Enter the number of people '))
expen={}
exppay={}
def people():
    for i in range(n):
        name=input('Enter name: ')
        peo.append(name)
        p1[name]={}
    return p1

def dataSheet():
    for i in range(n):
        p2=peo[:]
        p2.remove(peo[i])
        #print(p2)
        for j in range(len(p2)):
            p1[peo[i]][p2[j]]=None
    return p1

def expenses():
    n=int(input('Enter the number of expenses: '))
    for i in range(n):
        exp=input('Enter the name of the expense: ')
        expamt=int(input('Enter the expense amount: '))
        payer=input('Enter the payer\'s name: ')
        expen[exp] = {'amount': expamt, 'payer': payer}
        #print(expen)
        #exppay[exp]=payer
    print(expen)
   # print(exppay)
        
people()
a=dataSheet()
expenses()
print(a)
        
        
