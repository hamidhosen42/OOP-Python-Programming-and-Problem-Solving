"""
Encrypt the follwing code so that no one can get your strategy
"""

data='firebaby'
shift = 4
output =''

for character in data:
    output+=chr((ord(character)+shift-97) % 26 + 98)

print(output)