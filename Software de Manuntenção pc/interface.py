import flet as ft
# Importando as funções de manutenção do arquivo manutencao.py
from script import *


def main(page: ft.Page):
    page.title = "Sistema de Manutenção - Agência Alencar"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1400
    page.window_height = 900
    page.window_resizable = False
    page.scroll = ft.ScrollMode.AUTO

    log_output = ft.Text(value="", selectable=True, size=12)

    def log(texto, status="success"):
        # Atualiza o log dentro da interface gráfica
        img_path = '/mnt/data/success_img.png' if status == "success" else '/mnt/data/error_img.png'
        log_output.value += f"> {texto}\n"
        page.controls.append(ft.Row([ft.Image(src=img_path), ft.Text(texto)]))
        page.update()

    # Função para aguardar o pressionamento de ENTER
    def wait_for_enter(e):
        log("Aperte ENTER para continuar...")
        # Criamos o botão para continuar a execução quando o usuário pressionar ENTER
        continue_button = ft.ElevatedButton(
            "Continuar", on_click=continue_execution)
        page.add(continue_button)
        page.update()

    def continue_execution(e):
        log("Continuando a execução...")
        # Aqui podemos colocar a lógica para continuar a execução da função
        # Você pode chamar uma próxima função ou seguir com o código normalmente
        pass

    # Envolvendo as funções com log para capturar a saída e exibir no console
    def wrap(func):
        def handler(e):
            log(f"Executando: {func.__name__}")
            try:
                resultado = func(e)
                log("✔️ Concluído.", "success")
            except Exception as err:
                log(f"❌ Erro: {err}", "error")
        return handler

    def botao(label, func):
        return ft.Container(
            content=ft.ElevatedButton(label, on_click=wrap(func)),
            height=60,
            alignment=ft.alignment.center,
            expand=True
        )

    def coluna_botoes(botoes, total_linhas=7):
        while len(botoes) < total_linhas:
            botoes.append(ft.Container(height=60))
        return ft.Column(controls=botoes, spacing=10, expand=True)

    titulos = ft.Row([  # Títulos das seções
        ft.Container(ft.Text("🧹 Limpeza Geral", size=16, weight=ft.FontWeight.BOLD),
                     expand=True, alignment=ft.alignment.center),
        ft.Container(ft.Text("💾 InputLag", size=16, weight=ft.FontWeight.BOLD),
                     expand=True, alignment=ft.alignment.center),
        ft.Container(ft.Text("🚀 Otimização", size=16, weight=ft.FontWeight.BOLD),
                     expand=True, alignment=ft.alignment.center),
        ft.Container(ft.Text("📴 Serviços", size=16, weight=ft.FontWeight.BOLD),
                     expand=True, alignment=ft.alignment.center),
    ], spacing=40)

    coluna1 = coluna_botoes([  # Botões da coluna 1
        botao("Arquivos Temporários", arquivos_temp),
        botao("Limpeza de Thumbs.db", cache_mini),
        botao("Limpeza de Disco", limpeza_disco),
        botao("Scannow", scannow),
        botao("Otimizar Disco", limpeza_disco)
    ])

    coluna2 = coluna_botoes([  # Botões da coluna 2
        botao("Comandos de performance", comandos_performance),
        botao("Mouse + Teclado", mouse_teclado),
        botao("Registro", registro)
    ])

    coluna3 = coluna_botoes([  # Botões da coluna 3
        botao("Apps de Inicialização", apps_inicio),
        botao("Plano Alto Desempenho", plano_alto_desempenho),
        botao("Ajustar Melhor Desempenho", melhor_desemp),
        botao("Ajustar Armazenamento", armazenamento),
        botao("Apps em Segundo Plano", segundo_plano),
        botao("Modo Jogo", modo_jogo),
    ])

    coluna4 = coluna_botoes([  # Botões da coluna 4
        botao("Desativar Serviços", serviços),
        botao("Apps de Inicialização", apps_inicio)
    ])

    botoes = ft.Row([  # Agrupamento das colunas
        ft.Container(content=coluna1, expand=True),
        ft.Container(content=coluna2, expand=True),
        ft.Container(content=coluna3, expand=True),
        ft.Container(content=coluna4, expand=True),
    ], spacing=40)

    titulo = ft.Text("🛠️ Software de Manutenção 🛠️",
                     size=24, weight=ft.FontWeight.BOLD)

    page.add(
        titulo,
        ft.Divider(),
        titulos,
        ft.Divider(),
        botoes,
        ft.Divider(),
        ft.Text("📋 Log de Execução", weight=ft.FontWeight.BOLD, size=16),
        ft.Container(log_output, bgcolor=ft.colors.BLACK12,
                     padding=10, height=200, expand=True, border_radius=10),
    )
    page.update()


ft.app(target=main)
