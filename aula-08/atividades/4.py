def numero_primo(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

num = int(input('Digite um número: '))

print(numero_primo(num))
