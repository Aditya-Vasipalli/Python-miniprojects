variable_1=input('enter something')
variable_2=input('enter something again')
temp='' #empty temporary variable space
def variable_exchange():
    temp=variable_1
    variable_1=variable_2
    variable_2=temp
variable_exchange()
print("the first variable is now", variable_1)
print("second variable is now", variable_2)