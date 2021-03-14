for (i=1, i <= 100,+1) 9{
	if i % 3 == 0 1{
		write => 'Fizz'
	}
	if i % 5 == 0 1{
		write => 'Buzz'
	}
	if i % 3 == 0 or i % 5 == 0 1{
		write => f' - {i}\n'
	}
}