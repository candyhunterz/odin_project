def translate(word)

	if word[0] == /[aeiouAEIOU]/
		
		return word + "ay"

	i = word[0]
	if word[0] =~ /[aeiouAEIOU]/
		return word + "ay"
	else
		wa = word + word[0]
		wa[0] = ''
		return wa + "ay"

	end
end

print translate("hello")
