def pangram?(string)
    # enter your code here
    string.gsub(/[^a-z]/i, "").gsub(/(.)(?=.*\1)/i,"").length == 26
  end