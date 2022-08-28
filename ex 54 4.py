

def soma(n):
    
    if n%2 == 0:
        return print('fizz')
    elif n%5 == 0 and n%3 == 0:
        return print('FizzBuzz')
    elif n%5 == 0:
        return print('buzz')
    else:
        return print('numero invalido')

   

if __name__ == '__main__':
    n = int(input('digite o um numero '))
    soma(n)