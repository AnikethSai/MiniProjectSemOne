def split():
    # Iterate through each expense
    for i in expenses:
        # Get the total amount for the current expense and the payer
        amount = expen[i]['amount']
        payer = expen[i]['payer']
        
        # Calculate the equal share each person should pay
        share = amount / n  # Each person's share (equally divided among 'n' people)

        # Iterate through all people to update their balance
        for person in peo:
            if person == payer:
                # Payer has already paid the full amount, so they owe nothing
                p1[payer][person] = - (amount - share)  # Payer gets back the share from others
            else:
                # Others owe their share to the payer
                p1[payer][person] = share  # Person owes the payer
                p1[person][payer] = -share  # Payer is owed money by others

        print(f"Expense '{i}' split: {share} per person, payer: {payer}")
    print("Updated debts between people:", p1)
