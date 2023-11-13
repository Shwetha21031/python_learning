def hello(name):
    print(f'hello {name}')

def goodMorning(name):
    print(f'good morning {name}')

def hi():
    print('hiiii')


print('executed anyway')
hi()

if __name__ == '__main__':
    hello('')
    goodMorning('')
    print('executed when invoked directly')
else:
    hello('maria')
    goodMorning('rose')
    print('executed when imported')
