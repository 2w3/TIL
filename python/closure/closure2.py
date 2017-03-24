from functools import partial
functions = []
for i in range(5):
    functions.append( partial(print, i) )

for func in functions:
    func()
