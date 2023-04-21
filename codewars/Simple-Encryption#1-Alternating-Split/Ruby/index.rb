def encrypt(text, n)
    #your code here
    encrypted = text.clone
    count = 1
    even_indices = (0...text.length).select(&:even?)
    odd_indices = (0...text.length).select(&:odd?)
    while(count <= n)
      #get all characters whose indices are odd
      odd_characters = odd_indices.each_with_object({original_s:encrypted,encrypted:""}) {|ele,obj| obj[:encrypted] << obj[:original_s][ele]}
      even_characters = even_indices.each_with_object({original_s:encrypted,encrypted:""}) {|ele,obj| obj[:encrypted] << obj[:original_s][ele]}
      encrypted = odd_characters[:encrypted] + even_characters[:encrypted]
      count += 1
    end
    encrypted
  end
  
  def decrypt(encrypted_text, n)
      #your code here
    decrypted = encrypted_text.clone
    encrypted_text_letters = encrypted_text.chars
    count = 1
    even_indices = (0...encrypted_text.length).select(&:even?)
    odd_indices = (0...encrypted_text.length).select(&:odd?)
    while(count <= n)
      prev_even_letters = decrypted[-even_indices.length, decrypted.length]  
      prev_odd_letters = decrypted[0..((odd_indices.length) -1)]
      index = 0
      decrypt_obj = encrypted_text_letters.each_with_object({
        decrypted: decrypted,
        even: {
          current_index: 0,
          were_even_letters: prev_even_letters
        },
        odd: {
          current_index: 0,
          were_odd_letters: prev_odd_letters
        }
      }) do |ele,object|
        if index.even? then
          even_obj = object[:even]
          even_ltters = even_obj[:were_even_letters]
          object[:decrypted][index] = even_ltters[even_obj[:current_index]]
          even_obj[:current_index] += 1
        else
          odd_obj = object[:odd]
          odd_ltters = odd_obj[:were_odd_letters]
          object[:decrypted][index] = odd_ltters[odd_obj[:current_index]]
          odd_obj[:current_index] += 1
        end      
        index += 1       
      end
      
      count += 1
    end
    decrypted
  end