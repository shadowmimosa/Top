from timeit import timeit

print(timeit("""name="hoxis"
age=18
'%s is %s.'%(name,age)""", number=100000))
print(
    timeit(
        """name="hoxis"
age=18
'{} is {}.'.format(name,age)""", number=100000))
print(timeit("""name="hoxis"
age=18
f'{name} is {age}.'""", number=100000))
