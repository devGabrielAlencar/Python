import pandas as pd
import os


def salvar_excel(dados):
    # dados deve ser uma lista de dicionários (como você usou no Flet)

    df_novos = pd.DataFrame(dados)

    if os.path.exists("pedidos.xlsx"):
        df_existente = pd.read_excel('pedidos.xlsx', engine='openpyxl')

        df_total = pd.concat([df_existente, df_novos], ignore_index=True)
        df_total.drop_duplicates(subset='cliente', keep='last', inplace=True)
    else:
        df_total = df_novos

    df_total.to_excel("pedidos.xlsx", index=False, engine="openpyxl")
    print("✅ Dados salvos/atualizados na planilha pedidos.xlsx.")
