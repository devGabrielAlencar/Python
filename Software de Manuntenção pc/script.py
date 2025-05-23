import os
import subprocess
import tkinter as tk
from tkinter import filedialog


def log(texto):
    print(texto)  # Aqui você pode mudar para usar a função do log na interface gráfica


def arquivos_temp(e):
    log("\nLimpando arquivos temporários...")
    os.system("del /q /f /s %TEMP%\\*")
    os.system("del /q /f /s C:\\Windows\\Temp\\*")
    log("\n✅ Limpeza finalizada. Pressione ENTER para continuar...")


def cache_mini(e):
    log("\nLimpando cache de miniaturas...")
    os.system(
        "del /s /q /f %userprofile%\\AppData\\Local\\Microsoft\\Windows\\Explorer\\thumbcache_*.db")
    log("\n✅ Limpeza finalizada. Pressione ENTER para continuar...")


def limpeza_disco(e):
    log("\nIniciando Limpeza de disco...")
    os.system("cleanmgr")
    log("\n✅ Limpeza finalizada. Pressione ENTER para continuar...")


def scannow(e):
    log("\nInicializando o scan...")
    os.system('start cmd /k "sfc /scannow"')
    log("\n✅ Comando iniciado. Pressione ENTER para continuar...")


def instalar_programa(e):
    log("\nProgramas recomendados: // PC Manager // Driver Booster // Tweaker 4.8 //")
    log("\nAbrindo seletor de pastas...")

    root = tk.Tk()
    root.withdraw()

    pasta = filedialog.askdirectory(title="Selecione a pasta com o instalador")
    root.destroy()  # <-- Fecha o Tkinter corretamente

    if not pasta:
        log("❌ Nenhuma pasta selecionada.")
        return

    log(f"\n📁 Pasta selecionada: {pasta}")
    log("🔧 Abrindo Prompt de Comando...")

    subprocess.Popen('cmd.exe')
    log("\n✅ CMD aberto. Pressione Enter para continuar...")


def plano_alto_desempenho(e):
    os.system("powercfg -setactive SCHEME_MIN")
    log("\n✅ Plano ativado. Pressione Enter para continuar...")


def melhor_desemp(e):
    log("\n🧠 Abrindo configurações avançadas do sistema...")
    os.system("start sysdm.cpl")
    log("\n✅ Configuração aberta. Pressione Enter para continuar...")


def armazenamento(e):
    log("\n🌟 Abrindo configurações de Armazenamento...")
    os.system("start ms-settings:storagesense")
    log("\n✅ Configuração aberta. Pressione Enter para continuar...")


def segundo_plano(e):
    log("\nAbrindo apps em segundo plano...")
    os.system("start ms-settings:privacy-backgroundapps")
    log("\n✅ Configuração aberta. Pressione Enter para continuar...")


def modo_jogo(e):
    log("\nAtivar o modo de jogo...")
    os.system("start ms-settings:gaming-gamemode")
    log("\n✅ Configuração aberta. Pressione Enter para continuar...")


def apps_inicio(e):
    log("\nAbrindo apps de inicialização...")
    os.system("start ms-settings:startupapps")
    log("\n✅ Configuração aberta. Pressione Enter para continuar...")


def serviços(e):
    log("\nCriar ponto de Restauração...")
    os.system("SystemPropertiesProtection")
    log("\n✅ Painel de Restauração aberto. Pressione Enter para continuar...")

    log("\nPainel de serviços...")
    os.system("services.msc")
    log("\n✅ Painel de Serviços aberto. Pressione Enter para continuar...")

    log("""\nSERVIÇOS PARA DESATIVAR: 
            - cartão inteligente
            - configuração de área de trabalho remota
            - controle de pais
            - diagnóstico de execução de serviços
            - experiência do usuário conectado e telemetria
            - gerenciador de conexão de acesso remoto
            - logon de rede
            - política de remoção de cartão inteligente
            - registro remoto
            - serviços de biometria do windows
            - serviço de criptografia bitlocker
            - enumeração de dispositivos cartão inteligente
            - serviços de geolocalização
            - hotspot do windows
            - sensores
            - serviço de telefonia
            """)


def disco(e):
    log("\nAbrindo otimização de disco ... ")
    os.system("dfrgui")
    log("\n✅ Otimizador aberto. Pressione Enter para continuar...")


def comandos_performance(e):
    log("\nAtivando comandos de performance...")
    os.system('start cmd')
    log("""\nCOMANDOS:
        bcdedit /set useplatformtick yes
        bcdedit /set disabledynamictick yes
    """)


def mouse_teclado(e):
    log("\nAbrindo configurações do mouse...")
    os.system("start ms-settings:mousetouchpad")
    log("\n✅ Configurações do mouse abertas. Pressione Enter para continuar...")

    log("\n🧠 Abrindo propriedades do teclado...")
    os.system("control keyboard")
    log("\n✅ Configurações do teclado abertas. Pressione Enter para continuar...")


def registro(e):
    log("\nAbrindo Editor de Registro...")
    os.system("regedit")
    log("""\n📌 Caminhos sugeridos:

    🔹 HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\mouclass
        ▶️ MouseDataQueueSize = 0x28

    🔹 HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\kbdclass\\Parameters
        ▶️ KeyboardDataQueueSize = 0x28

    🔹 HKEY_CURRENT_USER\\Control Panel\\Accessibility\\MouseKeys
        ▶️ Flags = 0

    🔹 HKEY_CURRENT_USER\\Control Panel\\Accessibility\\Keyboard Response
        ▶️ Flags = 0
    """)
