import flet as ft
from Pandas_DF import salvar_excel
from wpp import enviar_mensagem_whatsapp


def main(page: ft.Page):
    page.title = 'Gerenciamento de Clientes'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#FF8C00'
    page.window_height = 720
    page.window_width = 1080

    dados = []

    # Título
    titulo = ft.Container(
        content=ft.Text(
            "👥 Sistema Dafruta CE",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLACK
        ),
        alignment=ft.alignment.center,
        padding=10,
        margin=ft.margin.only(bottom=10),
        bgcolor='#444',
        border_radius=10
    )

    cliente = ft.TextField(label='Cliente', width=220,
                           bgcolor=ft.colors.BLACK, color=ft.colors.ORANGE)
    endereco = ft.TextField(label='Endereço', width=220,
                            bgcolor=ft.colors.BLACK, color=ft.colors.ORANGE)
    valor = ft.TextField(label='Valor a ser Pago', width=220,
                         bgcolor=ft.colors.BLACK, color=ft.colors.ORANGE)
    entrega = ft.TextField(label='Data da entrega', width=220,
                           bgcolor=ft.colors.BLACK, color=ft.colors.ORANGE)

    def func_add(e):
        cliente_ = cliente.value.strip()
        endereco_ = endereco.value.strip()
        valor_ = valor.value.strip()
        entrega_ = entrega.value.strip()

        capacidade_ = dropdown_capacidade.value

        sabores_ = []
        if check.controls[0].value:
            sabores_.append("Laranja")
        if check.controls[1].value:
            sabores_.append("Uva")
        if check.controls[2].value:
            sabores_.append("Acerola")
        if check.controls[3].value:
            sabores_.append("Caja")
        if check.controls[4].value:
            sabores_.append("Caju")
        if check.controls[5].value:
            sabores_.append("Maracujá")
        if check.controls[6].value:
            sabores_.append("Tangerina")
        sabores_ = ', '.join(sabores_)  # Transformando a lista em uma string

        if not cliente_ or not endereco_ or not valor_ or not entrega_:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("⚠️ Todos os campos são obrigatórios"),
                bgcolor=ft.colors.RED
            )
            page.snack_bar.open = True
            page.update()
        else:
            novo_cliente = {
                'cliente': cliente_,
                'endereco': endereco_,
                'valor': valor_,
                'entrega': entrega_,
                'capacidade': capacidade_,
                'sabores': sabores_  # S
            }

            dados.append(novo_cliente)
            salvar_excel(dados)
            enviar_mensagem_whatsapp(
                cliente_, endereco_, valor_, entrega_, capacidade_, sabores_)

            page.snack_bar = ft.SnackBar(
                content=ft.Text("✅ Pedido registrado com sucesso!"),
                bgcolor=ft.colors.GREEN
            )
            page.snack_bar.open = True
            page.update()

    # Campos do cliente
    fields = ft.Row(
        controls=[
            cliente,
            endereco,
            valor,
            entrega
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Dropdown

    dropdown_capacidade = ft.Dropdown(
        label="Selecione uma opção",
        options=[
            ft.dropdown.Option("330ml"),
            ft.dropdown.Option("1L"),
            ft.dropdown.Option("2L"),
            ft.dropdown.Option("5L")
        ],
        width=220,
        bgcolor=ft.colors.BLACK
    )

    dropdown = ft.Column([
        ft.Text('Capacidade', size=18, weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK),
        dropdown_capacidade
    ])

    # Checkboxes
    check = ft.Column([
        ft.Text('Sabores', size=18, weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK),
        ft.Checkbox(label="Laranja"),
        ft.Checkbox(label="Uva"),
        ft.Checkbox(label="Acerola"),
        ft.Checkbox(label="Caja"),
        ft.Checkbox(label="Caju"),
        ft.Checkbox(label="Maracujá"),
        ft.Checkbox(label="Tangerina"),
    ])

    # Organização de opções (dropdown + checkboxes)
    opcoes = ft.Row(
        controls=[
            ft.Container(content=dropdown, padding=10),
            ft.Container(content=check, padding=10)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=60
    )

    # Botão
    btn = ft.Row(
        controls=[ft.ElevatedButton('📦 Registrar Pedido',  on_click=func_add)],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Layout final
    form = ft.Column(
        controls=[
            titulo,
            ft.Divider(thickness=1, color=ft.colors.BLACK),
            fields,
            ft.Divider(thickness=1, color=ft.colors.BLACK),
            opcoes,
            ft.Divider(thickness=1, color=ft.colors.BLACK),
            btn
        ],
        spacing=15,
        expand=True
    )

    page.add(form)


ft.app(target=main)
