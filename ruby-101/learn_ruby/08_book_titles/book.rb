class Book	
	attr_accessor :title

	def title
		return @title.gsub(/\w+/, &:capitalize)
	end
		

end

