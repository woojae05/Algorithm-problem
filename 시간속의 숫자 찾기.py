n = int(input())

if(n<3):
	print(1920*(n+1))
else:
	if(n<13):
		print(1920*(n+1)+60*60)
	elif(n<23):
		print(1920*(n+1)+60*60*2)
	elif(n>=23):
		print(1920*(n+1)+60*60*3)