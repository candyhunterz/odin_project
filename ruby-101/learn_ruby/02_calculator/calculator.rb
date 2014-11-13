def add(a,b)
	a + b
end

def subtract(a,b)
	a - b
end


def sum(array)
	result = 0
	if array.length == 1
		return array[0]
	else
		array.each do |i|
			result += i
		end
	end
	return result
end
