user=int(input('enter the number'))
user1=int(input('enter the number'))
user2=int(input('enter the number'))
if user==user1 and user1==user2 :
	print(' triangle hai')
elif user==user1 and user1!=user2:
	print("isosceles hai")
else:
	print("not equal")