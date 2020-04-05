demoList=[1,'hello',1.34,True,[1,2,3]]
myList= list((1,2,3,4)) # list constructor - receives a tuple as parameter
print(myList)

r=list(range(1,10))
print(r)

print(dir(list)) # methods and operations for lists

print(r[2]) # item in position 2
print (3 in r)

colors =["red", "green", "blue"]
print(colors)

colors[1]="yellow"
print(colors)

colors.append("violet")
colors.append(("black", "pink"))
print(colors)

# ['red', 'yellow', 'blue', 'violet', ('black', 'pink')]
# devuelve black y pink dentro de una tupla

#para que queden como valores de la lista hay que usar el metodo extend
colors =["red", "green", "blue"]
colors.extend(("yellow", "black"))
print(colors)


colors.insert(1,"dark blue") # insert in position 1
colors.insert(len(colors), "dark violet") # insert at the end
print(colors)


colors.pop() # remove last item
print(colors)

colors.remove('green') # remove by element
colors.pop(1) # remove by index
print(colors)

colors.clear()

# sort
colors =["red", "green", "blue"]
colors.sort()
colors.sort(reverse=True)
print (colors)

print (colors.index('red'))

colors.append('red')
print(colors.count('red'))

