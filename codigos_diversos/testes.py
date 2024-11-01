# Primieira versão tinha erro 
#nome_todo = str("Carla Edila Santos da Rosa Silveira")
#nome_todo.group(1)
# Saida: AttributeError: 'str' object has no attribute 'group'

# Segunda versão corrigida
nome_todo = str("Carla Edila Santos da Rosa Silveira")
primeiro_nome = nome_todo.split()[0]
print(primeiro_nome)  # Saída: Carla
