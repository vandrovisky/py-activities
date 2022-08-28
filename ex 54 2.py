

from tkinter import N


def soma():
    
    n1 = int(input('digite o primeiro numero '))
    n2 = int(input('digite o segundo  numero '))
    n3 = int(input('digite o terceiro numero '))
    
    soma = n1+n2+n3
    return soma



if __name__ == '__main__':
    print(soma())