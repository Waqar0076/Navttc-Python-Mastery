data = 'hello'

# strings Method
print(data.upper())
print(data.lower())
print(data.capitalize())
print(data.title())

print(data.count('l'))
print(data.find('world'))
print(data.index('h'))

print(data.startswith('d'))
print(data.endswith('!'))

print(data.isalnum())
print(data.isalpha())

print(data.isascii())

print(data.isdecimal())
print(data.isprintable())

print(data.replace("world","brother"))
print(data.split())

print(data.isspace())
print(data.isidentifier())

# check ascii code
ascii_codes = [ord(char) for char in data]
print(ascii_codes)