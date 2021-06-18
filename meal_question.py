day=input('enter the day=')
meal=input('enter the meal=')
if day=='monday':
	if meal=='breakfast':
		print('poori sabji')
	if meal=="lunch":
		print('sambhar rice')
	if meal=='dinner':
		print('chicken rice')
elif day=='tuesday':
	if meal=='breakfast':
		print('poha')
	if meal=='lunch':
		print('rajma rice')
	if meal=='dinner':
	   print('roti sabji')
else:
    print('nothing')
