print('insert the card')
language=input('enter the any language=')
if 'language'=='english':
	print('you select english language')
else:
	print('you select hindi language')
pin=int(input('enter your 4 digit pin='))
if pin=='1234':
	print('what you want')
	print('if you want cash choice 1')
	print('if you want   balance  inquary choice 2')
choice=int(input('enter what you want='))
if choice==1:
	print('you choice cash')
elif choice==2:
	print('you choice balance inquary')
balance=1000
balance=int(input('enter the balance='))
if balance==500:
	print('you can take')
else:
	print('not take')