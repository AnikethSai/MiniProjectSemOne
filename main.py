# payer: expSheet[i]['payer']
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
pcopy=p1
def dataSheet():
    for i in range(n):
        p2 = peo[:]
        p2.remove(peo[i])
        for j in range(len(p2)):
            p1[peo[i]][p2[j]] = 0
    return p1
def expenses():
    n1 = int(input('Enter the number of expenses: '))
    for i in range(n1):
        global expname
        expname = input('Enter the name of the expense: ')
        expamt = int(input('Enter the expense amount: '))
        payer = input('Enter the payer\'s name: ')

        if payer not in peo:
            print("Invalid payer name; retry")
            continue

        expSheet[expname] = {'amount': expamt, 'payer': payer}
        print('Expenses entered: \n')
        for k, v in expSheet.items():
            print(f"  {k}: {v}")
        global expense
        expense = list(expSheet.keys())
def split():
    for i in expense:
        part = expSheet[i]['amount']/n
        print(f"\nSplitting expense '{expname}' of amount {expSheet[i]['amount']:.2f}:")
        payer = expSheet[i]['payer']
        for person in peo:
            if person != payer:
                p1[payer][person] += part
                p1[person][payer] -= part
                print(f"  {person} owes {payer} {part:.2f}")


def final_bal():
    print("\nFinal Balances:")
    done = set()
    for person in peo:
        for other in peo:
            if person!=other and (person,other) not in done:
                if p1[person][other] > 0:
                    print(other, ' owes ',  person,' %.2f' %(p1[person][other]))
                elif p1[other][person] > 0:
                    print(person,' owes ',other,' %.2f'%(p1[other][person]))
                done.add((person, other))
                done.add((other, person))

people()
a = dataSheet()
expenses()
split()
final_bal()
print(a)


