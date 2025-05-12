def cadastrar_filmes(nome,
    descricao, 
    classificacao, 
    categoria01, 
    categoria02, 
    categoria03 ):
    lista = []
    discionario = {
        "nome" : nome, 
        "descricao" : descricao,
        "classificacao" : classificacao,
        "categorias" : [categoria01, categoria02, categoria03]
    }
    lista.append(discionario)
    return discionario

print(cadastrar_filmes("The Nightmare Before Christma", 
    "É um filme de animação stop-motion que conta a história de Jack Skellington, o rei da cidade do Halloween, que descobre a cidade do Natal e tenta trazer o espírito natalino para sua própria cidade, mas acaba causando confusão e aventura.", 
    "Livre", 
    "Animação ", 
    "Fantasia",
    "Musical"
    ))