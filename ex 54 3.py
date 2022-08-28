

def soma():
    
    n1 = int(input('digite o primeiro numero '))
    n2 = int(input('digite o segundo  numero '))
    
    soma = n1 + (n1*(n2*0.01))
    return print(soma)

if __name__ == '__main__':
    soma()