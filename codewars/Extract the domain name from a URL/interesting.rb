def domain_name(url)
    URI.parse(url).host.split('.').last(2)[0]
  end