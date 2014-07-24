def translate(word)
<<<<<<< HEAD
	if word[0] == /[aeiouAEIOU]/
		
		return word + "ay"
=======
	i = word[0]
	if word[0] =~ /[aeiouAEIOU]/
		return word + "ay"
	else
		wa = word + word[0]
		wa[0] = ''
		return wa + "ay"
>>>>>>> 0a5c8eca773003da389a99dd7eab3e387999df2c
	end
end
