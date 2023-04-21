def encrypt(text, n)
    return text if n <= 0
    encrypt(text.scan(/(.)(.)?/).transpose.reverse.join, n-1)
  end
  
  def decrypt(text, n)
    return text if n <= 0
    c, s = text.chars, text.size/2
    decrypt(c.drop(s).zip(c.take s).join, n-1)
  end