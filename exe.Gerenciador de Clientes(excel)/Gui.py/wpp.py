import urllib.parse
import webbrowser  # para abrir o link automaticamente


def enviar_mensagem_whatsapp(cliente, endereco, valor, entrega, capacidade, sabores):
    mensagem = f"📦 *Novo Pedido da Dafruta CE*\n\n"
    mensagem += f"👤 Cliente: {cliente}\n"
    mensagem += f"📍 Endereço: {endereco}\n"
    mensagem += f"💰 Valor: {valor}\n"
    mensagem += f"📅 Entrega: {entrega}\n"
    mensagem += f"🧃 Capacidade: {capacidade}\n"
    mensagem += f"🍹 Sabores: {sabores}"

    mensagem_codificada = urllib.parse.quote(mensagem)

    # Substitua '5588999999999' pelo número do cliente com DDD e código do país (55 para Brasil)
    # <-- aqui você pode criar um campo na interface depois
    numero_cliente = '5585997430963'
    url_whatsapp = f"https://wa.me/{numero_cliente}?text={mensagem_codificada}"

    webbrowser.open(url_whatsapp)
