# payer: expen[i]['payer']
'''
p1 -> stroes the main datasheet dictionary

'''
peo = []
p1 = {}
n = int(input('Enter the number of people '))
expSheet = {}
def people():
    for i in range(n):
        name = input('Enter name: ')
        peo.append(name)
        p1[name] = {}
    return p1
def dataSheet():
    for i in range(n):
        p2 = peo[:]
        p2.remove(peo[i])
        for j in range(len(p2)):
            p1[peo[i]][p2[j]] = None
    return p1
def expenses():
    n1 = int(input('Enter the number of expenses: '))
    for i in range(n1):
        global expname
        expname = input('Enter the name of the expense: ')
        expamt = int(input('Enter the expense amount: '))
        payer = input('Enter the payer\'s name: ')
        expSheet[expname] = {'amount': expamt, 'payer': payer}
        global expense
        expense = list(expSheet.keys())
    print(expSheet)
def split():
    for i in expense:
        part = expSheet[i]['amount']/n
        global p1k
        p1k = list(p1[expSheet[i]['payer']].keys())
        for j in range(n-1):
            p1[expSheet[i]['payer']][p1k[j]] = part
        print('Final: ', expSheet)
        print(part)


people()
a = dataSheet()
expenses()
split()
print(a)
print('p1k:',p1k)


