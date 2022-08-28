string = '123456789123456789123456789123456789123456789123456789'
lista = [string [i:i+9] for i in range(0,len(string),9)]
new_string = '.'.join(lista)

print(new_string)