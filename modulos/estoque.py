from core.dados import estoque


#=======BUSCAR PRODUTO=======
def buscar_produto():
    busca = input("Buscar produto: ").lower()

    for produto in estoque:
        if busca in produto:
            print(produto, estoque[produto])