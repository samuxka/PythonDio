pessoa = {"nome": "samuel", "idade": 16}

pessoa = dict(nome = "samuel", idade = 16)

pessoa["telefone"] = "75988098306"

#captura de dados
dados = {"nome": "Samuel", "idade": 16, "telefone": "75988098306"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "maria"

dados["idade"] = 21

dados["telefone"] = "75988098306"

print(dados)

contatos = {
    "samukactto@gmail.com" : {"nome": "samuel", "telefone": "75988098306"},
    "gameoverbr425@gmailcom" : {"nome": "igor", "telefone": "7598812345"},
    "markindupray@gmail.com" : {"nome": "marcos", "telefone": "75988098306"},
    "juanizio@gmail.com" : {"nome": "joao", "telefone": "759885498"},
    "extra": {'a': 1}
}

telefone = contatos["samukactto@gmail.com"]["telefone"]

print(telefone)

extra = contatos["extra"]["a"]
print(extra)

#for chave in contatos:
#    print(chave, contatos[chave])

#for chave, valor in contatos.item():
#    print(chave, valor)

