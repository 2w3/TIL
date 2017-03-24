functions = []
for i in range(5):
    functions.append( lambda : print(i) )

for func in functions:
    func()
