def hello():
    print('hello world')

hello()


def hello(name):
    print('hello world '+ name)

hello('Ryan')


def hello(name='Person'):
    print('hello world '+ name)

hello()


def add(n1,n2):
    return n1+n2

print(add(20,1))


# def a function in one line
add = lambda n1,n2: n1+n2
print(add(20,1))