def caesar_cipher(s, f)
	n = 0
	a = ('a'..'z').to_a + ('A'..'Z').to_a
	if f == 0
		return s
	else
		s.each_char do |x|
		    if x == " "
		        n = 0
		   
		    else
			    n = a.index(x) + f
			    if n > 26
			        n = n % 26
			    end
			    s.gsub!(x, a[n])
			end
		end
		return s
	end
end

puts caesar_cipher("asdf eFg",0)

puts caesar_cipher("b",2)

#caesar_cipher("What a string!", 5)
# "Bmfy f xywnsl!"

