foods=["apples",'bread','cheese','milk']


print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print('')

for food in foods:
    print(food)

    if food=='cheese':
        break


print('')
for food in foods:

    if food=='cheese':
        continue

    print(food)


print('')
for number in range(1,8):
    print(number)


print('')
for letter in "hello":
    print(letter)


print('')
count=4
while count <= 10:
    print(count)
    count=count+1

