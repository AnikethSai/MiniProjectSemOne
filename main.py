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
            p1[peo[i]][p2[j]] = 0
    return p1
def expenses():
    n1 = int(input('Enter the number of expenses: '))
    for i in range(n1):
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
        expamt = expSheet[i]['amount']
        payer = expSheet[i]['payer']
        split_people=[]
        print('Splitting expense ',i,' of amount %.2f'%expamt)
        print('Payer is ',payer,'. Who should split this expense?')
        split_opt=input('Enter \'all\' to split among everyone or press enter to split among specific people')

        if split_opt=='all':
            split_people=peo[:]
            part = expamt / len(split_people)
            split_people.remove(payer)
        else:
            while True:
                person = input('Enter a person to split the expense with (enter done to finish)').strip()
                if person.lower() == 'done':
                    break
                elif person not in peo:
                    print(f"{person} is not in the list of people.")
                elif person == payer:
                    print(f"{person} is the payer and cannot split.")
                elif person in split_people:
                    print(f"{person} is already added.")
                else:
                    split_people.append(person)
            part = expamt / (len(split_people) + 1)

        if not split_people:
            print(f"No valid people to split the expense. Skipping this expense.")
            continue

        for person in split_people:
            #if person != payer:
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
dataSheet()
expenses()
split()
final_bal()
