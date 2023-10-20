"""
Clean the data and get a String output 'a e i o u'
"""

data="aNtEriOur\n\t>>"
print(data.lower())

new_data=data.lower()

output_data=''

for i in new_data:
    # print(i)
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        print(f"{i} found")
        output_data+=i+" "

print(output_data)