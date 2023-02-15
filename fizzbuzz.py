word= ""
for n in range(1,101):

	if n%3==0:
		word+= "Fizz"
	if n%5==0:
		word+= "Buzz"
	if word== "":
		print(n)
	else: 
		print(word)