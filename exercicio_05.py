from exercicio_04 import calcular_media


def cadastrar_aluno(nome, email, serie, nota01, nota02, nota03):
    
    lista_alunos = []
    notas = nota01, nota02, nota03
    aluno = {
        'nome': nome,
        'email': email,
        'serie': serie,
        'notas' : notas, 
        "media" : calcular_media(notas)
    }
    
    lista_alunos.append(aluno)
    
    return lista_alunos
print(cadastrar_aluno('Angela Gon', 'angela.gon@gmail.com', '2ª ano'))