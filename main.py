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
    peo = []
    originalNames={}
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

        expSheet[expname] = {'amount': expamt, 'payer': payer}
        expense_name.append(expname)
    print('\n')
    return expSheet,expense_name

def print_expenses(expSheet):
    print('Expenses entered:\n')
    for k, v in expSheet.items():
        print(f"  {k}: {v}")

def split(peo,p1,expSheet,expense_name,originalNames):
    for i in expense_name:
        expamt = expSheet[i]['amount']
        payer = expSheet[i]['payer']
        split_people=[]
        print('Splitting expense',i,' of amount %.2f'%expamt)
        print('Payer is ',payer,'\nWho should split this expense?')
        split_opt=input('Enter \'all\' to split among everyone or press enter to split among specific people')

        if split_opt=='all':
            split_people=peo[:]
            part = expamt / len(split_people)
            split_people.remove(payer)
        else:
            while True:
                person = input('Enter a person to split the expense with (Press enter to finish/move to next person)').lower()
                if person.lower() == '':
                    print('\n')
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
            p1[payer][person] += part
            p1[person][payer] -= part
            print(f"{originalNames[person]} owes {originalNames[payer]} {part:.2f}")
        print('\n')
    print('\n')
    return p1
def final_bal(p1,peo,originalNames):
    print("\nFinal Balances:")
    done = set()
    for person in peo:
        for other in peo:
            if person!=other and (person,other) not in done:
                if p1[person][other] > 0:
                    print(originalNames[other], ' owes ', originalNames[person],' %.2f' %(p1[person][other]))
                elif p1[other][person] > 0:
                    print(originalNames[person],' owes ',originalNames[other],' %.2f'%(p1[other][person]))
                done.add((person, other))
                done.add((other, person))


def save_to_file_user_input(peo, p1, expSheet, originalNames):
    filepath = input('Enter the full path where the file should be saved (e.g., C:\\Users\\YourName\\Downloads): ').strip()
    filename = input('Enter the name of the file (e.g., Expenses.txt): ').strip()
    if not filepath.endswith("\\"):
        filepath += "\\"
    fullpath = filepath + filename

    try:
        with open(fullpath, 'w') as f:
            f.write("People:\n")
            for name in peo:
                f.write(f"  {originalNames[name]} (equalized: {name})\n")

            f.write("\nExpenses:\n")
            for exp, details in expSheet.items():
                f.write(f"  {exp}: {details['amount']} paid by {originalNames[details['payer']]}\n")

            f.write("\nFinal Balances:\n")
            done = set()
            for person in peo:
                for other in peo:
                    if person != other and (person, other) not in done:
                        if p1[person][other] > 0:
                            f.write(f"  {originalNames[other]} owes {originalNames[person]}: {p1[person][other]:.2f}\n")
                        elif p1[other][person] > 0:
                            f.write(f"  {originalNames[person]} owes {originalNames[other]}: {p1[other][person]:.2f}\n")
                        done.add((person, other))
                        done.add((other, person))
        print(f"Data successfully saved to {fullpath}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


try:
    n = validInput('Enter the number of people: ')
    if n <= 0:
        raise ValueError("Number of people must be a positive integer.")
except ValueError as e:
    print(e)
    exit()
else:
    peo,p1,originalNames=people(n)
    p1=dataSheet(peo,p1)
    expSheet, expense_name = expenses(peo)
if expense_name:
    p1=split(peo,p1,expSheet,expense_name,originalNames)
    final_bal(p1,peo,originalNames)
    save_to_file_user_input(peo, p1, expSheet, originalNames)
