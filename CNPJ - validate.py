import re


def formula(digit):
    return ((11 - (digit % 11)))

def iterable_cnpj(digits, validate):
    digit = 0
    for i,j in enumerate(digits): 
        digit += (int(validate[i]) * int(j))    
    return digit

def confirm (digits,cnpj_number):

    if digits == cnpj_number:
        return print("cnpj valido")
    else:
        return print("cnpj invalido")

def cnpj_validate(cnpj):

    removed_chars = '.','/','-'
    chars = '|'.join(map(re.escape,removed_chars))
    cnpj_number = re.sub(chars, '', cnpj) 

    code_validate = cnpj_number[:-2]
    
    primary_validate = '543298765432'
    secundary_validate = '6543298765432'

    primary_digit = iterable_cnpj(code_validate,primary_validate)

    n1 = formula(primary_digit)

    code_validate = code_validate + (str(n1))
   
    secundary_digit = iterable_cnpj(code_validate,secundary_validate)
    
    n2 = formula(secundary_digit)
   
    if n2 > 9:

        n2 = 0
        code_validate= code_validate + str(n2)
        confirm(code_validate,cnpj_number)

    else: 

        code_validate = code_validate + str(n2)
        confirm(code_validate,cnpj_number)

if __name__ == "__main__":
    cnpj = "04.252.011/0001-10"
    cnpj_validate(cnpj)