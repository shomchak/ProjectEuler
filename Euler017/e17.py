def numToString(numString):
	digits = len(numString)
	word = ''
	words =	{1:'one',
			2:'two',
			3:'three',
			4:'four',
			5:'five',
			6:'six',
			7:'seven',
			8:'eight',
			9:'nine',
			10:'ten',
			11:'eleven',
			12:'twelve',
			13:'thirteen',
			14:'fourteen',
			15:'fifteen',
			16:'sixteen',
			17:'seventeen',
			18:'eighteen',
			19:'nineteen',
			20:'twenty',
			30:'thirty',
			40:'forty',
			50:'fifty',
			60:'sixty',
			70:'seventy',
			80:'eighty',
			90:'ninety',
			100:'hundred',
			1000:'thousand'}
	if(digits == 4):
		word = words[1].__add__(words[1000])
		return word
	elif(digits == 3):
		if(numString[1] != '0' or numString[2] != '0'):
			hundreds = words[ord(numString[0])-48].__add__('hundred')
			hundreds_and = hundreds.__add__('and')
			rest = numString[1].__add__(numString[2])
			word = hundreds_and.__add__(numToString(rest))
			return word
		else:
			hundreds = words[ord(numString[0])-48].__add__('hundred')
			return hundreds
	elif(digits == 2):
		if(numString[0] == '0'):
			rest = numString[1]
			word = numToString(rest)
			return word
		elif(numString[0] == '1'):
			tens = (ord(numString[0]) - 48)*10
			ones = ord(numString[1]) - 48
			word = words[tens+ones]
			return word
		else:
			tens_num = (ord(numString[0]) - 48)*10
			tens = words[tens_num]
			rest = numString[1]
			word = tens.__add__(numToString(rest))
			return word
	elif(digits == 1):
		if(numString == '0'):
			return ''
		else:
			word = words[ord(numString)-48]
			return word

def sumNumsTo(limit):
	total = 0
	for n in range(1,limit+1):
		numLength = len(numToString(str(n)))
		total += numLength
	return total

print sumNumsTo(1000)
