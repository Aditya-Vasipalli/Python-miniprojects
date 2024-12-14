string_one='Hello World'
#define string & get index error and type error
try:
    print(string_one[100])
except IndexError:
    print('string_one[100] is indexerror')

try:
    print(string_one[0.02])
except TypeError:
    print('string_one[0.02] is typerror')

#slice string
print(string_one[2:-1:2])
print(string_one[1:5])
print(string_one[6:1:-1]+string_one[0:-1])

#converting to uppercase
print(string_one.upper())
#converting to lowercase:
print(string_one.lower())

#strip and replace
string_two=' hello world '
print(string_two.strip())
print(string_one.replace('l', 'w'))

#multiplying string
print(string_one*3+string_two*3)