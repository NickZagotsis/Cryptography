def is_generator(k, prime):
  for i in range(2, prime):
    if pow(k, i, prime) == k: #it must equal every number except itself
      return False
  return True

prime = 28151
for k in range(prime):
  if is_generator(k, prime):
    print(k)
    break