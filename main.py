from quote import Quote 

file = open('quotes.txt', 'w')
quote = Quote()
split = '\n\n\n@@@@@@@@@@@@@@@@@@@@@@@\n\n\n'

for i in range(20):
	result = quote.give()
	file.write(result['quoteText'])
	if result['quoteAuthor']:
		file.write('\n - ')
		file.write(result['quoteAuthor'])
	file.write(split)
file.close()