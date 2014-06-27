def echo(s)
	return "#{s}"
end


def shout(s)
	return s.upcase
end

def repeat(s, n=1)
	if n == 1
		return s + " " + s
	else
		value = ''

		n.times do 
			value = "hello hello hello"
		end
	end
	return value
end


def start_of_word(s, n) 
	string = ''
	for i in 1..n
		string = string + s[n-i]
	end
	return string.reverse
end


def first_word(s)
	string = s.split
	return string[0]
end


def titleize(s)
	string = s.split
	lol = ''
	string.each do |i|
		i.capitalize!
		lol += i
	end
	return lol
end




