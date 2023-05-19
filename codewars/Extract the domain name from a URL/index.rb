def domain_name(url)
    # return just the domain name
    new_url = url.gsub(/(?:https?:\/\/)?(?:www.)?/,"")  
    /\A(?<domain>[a-z0-9-]+)(?=\.)/ =~ new_url
    domain
  end
# apparently when u use the =~ if there are any named captures,
# the names will be turned to variables with value being the matched str