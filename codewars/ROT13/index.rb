require 'pry'

def rot13(message)
    #your code here
    message.codepoints.each_with_object("") do |codepoint, str|      
        
        if( (65..90).include?(codepoint) || (97..122).include?(codepoint))
            decoded = codepoint + 13
            if(decoded.between?(91, 103) || decoded.between?(123, 135))                
                decoded = decoded - 26
            end
            next str << decoded.chr
        end
        str << codepoint.chr
    end
       
end
puts rot13 "This is my first ROT13 excercise!"
