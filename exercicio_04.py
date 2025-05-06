def calcular_media(numeros):
    total_soma = 0 
    quantidade = len(numeros)  
    
    for i in numeros:
        total_soma += i
    
    media = total_soma / quantidade if quantidade > 0 else 0
    return media

numeros_aleatorios = [10, 20, 30, 40, 50]
print(calcular_media(numeros_aleatorios))