
min = float(input('Enter the number of call minutes used:'))
msg = float(input('Enter the number of text messages sent:'))
extramin = 0
extramsg = 0



#Calculates 911 fee
noofee = 0.44


#Calculates fee for minutes

if min < 50:
    exminplanfee = 0
else:
    exminplanfee = (min - 50) * 0.15

totalmin =  exminplanfee



#Calculates fee for messages
if msg < 50:
    exmsgplanfee = 0
else:
    exmsgplanfee = (msg - 50) * 0.15

totalmsg = exmsgplanfee


#Calculates tax
total = float(f'{(totalmsg + totalmin + noofee):.2f}')
tax = float(f'{(total * 0.05):.2f}')



#Prints bill
print(f'{" YOUR PHONE USAGE BILL " :=^50}')
print(f'{"Base Fee" :.<40} $ { 15 :>7.2f}')
print(f'{"911 Fee" :.<40} $ {noofee :>7.2f}')
if exminplanfee > 0:
    print(f'{"Extra Minutes Cost" :.<40} $ {exminplanfee :>7.2f}')
if exmsgplanfee > 0:
    print(f'{"Extra Messages Cost" :.<40} $ {exmsgplanfee :>7.2f}')
print(f'{"SUBTOTAL" :.<40} $ {total :>7}')
print(f'{"Tax Fee" :.<40} $ {tax :>7.2f}')
print(f'{"TOTAL BILL" :.<40} $ {( 15 + total + tax):>7.2f}')
print(f'{"":=<50}')
