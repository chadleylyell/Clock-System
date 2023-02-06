import readline,hashlib
mystring = input('Please set a password: ')
hash_object = hashlib.sha512(mystring.encode())
hex_dig = hash_object.hexdigest()
print(hash_object)
print(hex_dig)