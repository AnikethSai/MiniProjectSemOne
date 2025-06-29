def validInput(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Invalid input. Please enter a positive integer")

def people(n):
    originalNames={}
    peo = []
    p1 = {}
    for i in range(n):
        name = input('Enter name: ')
        name1=name.lower()
        peo.append(name1)
        originalNames[name1]=name
        p1[name1] = {}
    print('\n')
    return peo,p1,originalNames

def dataSheet(peo,p1):
    for person in peo:
        for other in peo:
            if person != other:
                p1[person][other]=0
    return p1

def expenses(peo):
    expSheet = {}
    expense_name = []
    n1 = validInput('Enter the number of expenses: ')

    for i in range(n1):
        expname = input('Enter the name of the expense: ')
        expamt = validInput('Enter the expense amount: ')
        while True:
            payer = input('Enter the payer\'s name: ').lower()
            if payer in peo:
                break
            else:
                print("Invalid payer name; retry")
        print('\n')
        expSheet[expname] = {'amount': expamt, 'payer': payer, 'split_details':[]}
        expense_name.append(expname)
    print('\n')
    return expSheet,expense_name

def print_expenses(expSheet):
    print('Expenses entered:\n')
    for k, v in expSheet.items():
        print(f"  {k}: {v}")

def split(peo,p1,expSheet,expense_name,originalNames):
    global split_opt
    split_opt=''
    for i in expense_name:
        expamt = expSheet[i]['amount']
        payer = expSheet[i]['payer']
        split_people=[]
        if len(peo)!=2:
            print('Splitting expense', i, ' of amount %.2f' % expamt)
            print('Payer is ', payer, '\nWho should split this expense?')
            split_opt = input(
                'Enter \'all\' to split among everyone (or) press enter to split among specific people: ').lower().strip()

        if split_opt=='all' or len(peo)==2:
            split_people=peo[:]
            part = expamt / len(split_people)
            split_people.remove(payer)
        else:
            def splitList():
                while True:
                    person = input(
                        'Enter a person to split the expense with (Press enter to finish/move to next person): ').lower().strip()
                    if person.lower() == '':
                        # print('\n')
                        break
                    elif person not in peo:
                        print(f"{person} is not in the list of people.")
                    elif person == payer:
                        print(f"{person} is the payer and cannot split.")
                    elif person in split_people:
                        print(f"{person} is already added.")
                    else:
                        split_people.append(person)
                    if len(split_people) == len(peo) - 1:
                        print('Everyone has been added.')
                        break
            splitList()
            part = expamt / (len(split_people) + 1)
        if not split_people:
            print('Retry:')
            while not split_people:
                splitList()
        for person in split_people:
            p1[payer][person] += part
            p1[person][payer] -= part
            expSheet[i]['split_details'].append({'name':person,'amount':part})
            print(f"{originalNames[person]} owes {originalNames[payer]} {part:.2f}")
        print('\n')
    return p1
def final_bal(p1,peo,originalNames):
    final_balances="\nFinal Balances:\n\n"
    done = set()
    for person in peo:
        for other in peo:
            if person!=other and (person,other) not in done:
                if p1[person][other] > 0:
                    final_balances+=f"{originalNames[other]} owes {originalNames[person]} %.2f\n" %(p1[person][other])
                elif p1[other][person] > 0:
                    final_balances+=f"{originalNames[person]} owes {originalNames[other]} %.2f\n"%(p1[other][person])
                done.add((person, other))
                done.add((other, person))
    return final_balances

def expense_summary(expSheet,originalNames):
    summary='\nExpense Summary:\n'
    summary+= '\n'+ '-'*50 + '\n'
    for exp, details in expSheet.items():
        summary+=f'Expense: {exp}\n'
        summary+=f"Amount: {details['amount']}\n"
        summary+=f"Paid by: {originalNames[details['payer']]}\n"

        if len(details['split_details'])==len(originalNames)-1:
            summary+='Split among: All\n'
        else:
            summary+='Split Among: '
            split_names=[]
            for split in details['split_details']:
                split_names.append(originalNames[split['name']])
            summary+=f'{originalNames[details['payer']]},'+','.join(split_names)+'\n'
        for split in details['split_details']:
            summary+=f"    {originalNames[split['name']]} owes {originalNames[details['payer']]}: {split['amount']:.2f}\n"
        summary+='\n'+"-" * 50 + '\n'
    return summary
def saveToFile(peo, p1, expSheet, originalNames):
    filepath = input('Enter the path of the folder where the file should be saved (e.g., C:\\Users\\YourName\\Downloads): ').strip().lstrip('\"').rstrip('\"')
    filename = input('Enter the name of the file (e.g., Expenses): ').strip()
    if not filepath.endswith("\\"):
        filepath += "\\"
    fullpath = filepath + filename +'.txt'

    try:
        expense_details = expense_summary(expSheet, originalNames)
        final_balances=final_bal(p1,peo,originalNames)
        with open(fullpath, 'w') as f:
            f.write(expense_details)
            f.write('\n')
            f.write(final_balances)
        print(f"Data successfully saved to {fullpath}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


try:
    n = validInput('Enter the number of people: ')
    if n <= 1:
        raise ValueError("Number of people must be a positive integer greater than 1.")
except ValueError as e:
    print(e)
    exit()
else:
    peo,p1,originalNames=people(n)
    p1=dataSheet(peo,p1)
    expSheet, expense_name = expenses(peo)
if expense_name:
    p1=split(peo,p1,expSheet,expense_name,originalNames)
    print(expense_summary(expSheet, originalNames))
    print(final_bal(p1, peo, originalNames))
    c='!'
    c=input('Do you want to save this data in a file? Press enter to save (or) type \'no\' to exit. ').strip()
    if c=='':
        saveToFile(peo, p1, expSheet, originalNames)
