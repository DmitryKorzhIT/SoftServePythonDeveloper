def get_reply(number):

	try:
		number = int(number)

	except:
		return 'Please change your input on an integer number.'

	else:
		if number%5==0 and number%3==0:
			return 'FizzBuzz'

		elif number%3==0:
			return 'Fizz'

		elif number%5==0:
			return 'Buzz'

		else:
			return ''