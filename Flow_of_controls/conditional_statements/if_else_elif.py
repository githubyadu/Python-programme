fix_amount=10000
withdraw=int(input('enter the amount'))

if  withdraw<=fix_amount:
    balance=fix_amount-withdraw
    print('your balance',balance)

else:
    print('insufficient balance')

