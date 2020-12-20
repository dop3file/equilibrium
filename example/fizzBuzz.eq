for (i=1, i<=100,+1) 9{
	if i % 3 == 0 1{
		write => f'Fizz - {i}\n'
	}
	elif i % 5 == 0 1{
		write => f'Buzz - {i}\n'
	}
	elif i % 3 == 0 and i % 5 == 0 1{
		write => f'FizzBuzz - {i}\n'
	}
}