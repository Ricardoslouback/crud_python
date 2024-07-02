import mysql.connector #conexão criada 

conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdyoutube',

)

cursor=conexao.cursor()

#crud
#create
#nome_produto = "fone aplle"
#valor =789
#comando = f'INSERT INTO vendas(nome_produto,valor) Values ("{nome_produto}",{valor})'
#print(cursor.rowcount, f"registro:{nome_produto} inserido:{valor}.")
#cursor.execute(comando)
#conexao.commit()# edita um banco de dados 


#################################################
# read 
selecionar_tabela=f'SELECT * FROM Vendas'
cursor.execute(selecionar_tabela)
resultado = cursor.fetchall()#ler o banco de dados 

print(resultado)



#update
#produto="camisa"
#valor=35
#update=f'UPDATE vendas set valor = {valor} WHERE nome_produto = "{produto}"'
#cursor.execute(update)
#conexao.commit()

#############################################################################
#Delete
#produto = "tenis"

#deletar_produto =f'DELETE FROM vendas WHERE nome_produto ="{produto}"'
#cursor.execute(deletar_produto)
#conexao.commit()
#print(deletar_produto)

cursor.close()

conexao.close()