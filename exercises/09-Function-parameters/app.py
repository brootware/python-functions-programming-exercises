# Your code goes here:
def render_person(name,bd,color,age,sex):
    param = "{} is a {} years old {} born in {} with {} eyes".format(name,age,sex,bd,color)
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))