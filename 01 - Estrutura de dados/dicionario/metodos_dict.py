# {}.clear
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"},
    "marcos@gmail.com": {"nome": "Marcos", "celular": "4444-5555", "profissao": {"atual": "Professor"}},
    "julio@gmail.com": {"nome": "Julio", "celular": "5555-6666"},
}

contato.clear()
contato # {}


# {}.copy
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

copia = contato.copy()
copia["matheus@gmail.com"] = {"nome": "Theus"}

contato["matheus@gmail.com"] # {"nome": "Matheus", "celular": "3333-4444"}
copia["matheus@gmail.com"] # {"nome": "Theus"}


# {}.fromkeys

dict.fromkeys(["nome", "celular"]) # {"nome": None, "celular": None}

dict.fromkeys(["nome", "celular"], "vazio") # {"nome": "vazio", "celular": "vazio"}

# {}.get
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato["chave"] #KeyError

contato.get("chave") # None
contato.get("chave", {}) # {}
contato.get("matheus@gmail.com", {}) # {"matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}}

# {}.items
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato.items() # dict_items(['matheus@gmail.com', {'nome': 'Matheus', 'celular': '3333-4444'})])


# {}.keys
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato.keys() # dict_keys(['matheus@gmail.com'])


# {}.pop

contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato.pop("matheus@gmail.com") # {'nome': 'Matheus', 'celular': '3333-4444'}

contato.pop("matheus@gmail.com", {})


# {}.popitem

contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato.popitem() # Remove sem passar valor e indo por sequência
contato.popitem() #KeyError quando não achar mais valores


# {}.setdefault

contato = {"nome": "Matheus", "celular": "3333-4444"}

contato.setdefault("nome", "Venicio") # "Matheus"
contato # {'nome': 'Matheus', 'celular': '3333-4444'}

contato.setdefault("idade", 22) # 22
contato # {'nome': 'Matheus', 'celular': '3333-4444', 'idade': 22}


# {}.update
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"}
}

contato.update({"matheus@gmail.com": {"nome": "Theus"}})
contato # {'matheus@gmail.com': {'nome': 'Theus'}}

contato.update({"melanie@gmail.com": {"nome": "Melanie", "celular": "3322-2121"}})
contato # {'matheus@gmail.com': {'nome': 'Theus'}, 'melanie@gmail.com': {'nome': 'Melanie', 'celular': '3322-2121'}}


# {}.values
contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"},
    "marcos@gmail.com": {"nome": "Marcos", "celular": "4444-5555", "profissao": {"atual": "Professor"}},
    "julio@gmail.com": {"nome": "Julio", "celular": "5555-6666"},
}

contato.values() # Retorna todos os valores dentro de contato



# metodo in

contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"},
    "marcos@gmail.com": {"nome": "Marcos", "celular": "4444-5555", "profissao": {"atual": "Professor"}},
    "julio@gmail.com": {"nome": "Julio", "celular": "5555-6666"},
}

resultado = "matheus@gmail.com" in contato # True
print(resultado)

resultado = "allianz@gov.com" in contato # False
print(resultado)

resultado = "celular" in contato["marcos@gmail.com"] # True
print(resultado)

resultado = "idade" in contato["julio@gmail.com"] # False
print(resultado)


# metodo Del

contato = {
    "matheus@gmail.com": {"nome": "Matheus", "celular": "3333-4444"},
    "marcos@gmail.com": {"nome": "Marcos", "celular": "4444-5555", "profissao": {"atual": "Professor"}},
    "julio@gmail.com": {"nome": "Julio", "celular": "5555-6666"},
    "allianz@gov.com": {"nome": "Allianz", "celular": "9999-0909", "bloco": "C"},
}

del contato["matheus@gmail.com"]["celular"] # Delete "celular":
del contato["allianz@gov.com"]["bloco"] # Delete "bloco":
print(contato)

