# Dados iniciais
USUARIOS = {
    "gerente": {
        "senha": "162526",
        "perfil": "gerente"
    },
    "vendedor": {
        "senha": "102030",
        "perfil": "vendedor"
    }
}

# Permissões por perfil
PERMISSOES = {
    "gerente": ["estoque_view", "estoque_add", "estoque_edit", "vendas", "registro", "financeiro"],
    "vendedor": ["estoque_view", "vendas"]
}