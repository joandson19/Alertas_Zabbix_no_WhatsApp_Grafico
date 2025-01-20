#!/usr/bin/python3

import sys
import re
from datetime import datetime
from loguru import logger
import httpx
from pyzabbix import ZabbixAPI

# Configurações
WHATSAPP_API_URL = sys.argv[1] # recebe a Url da api do whatsapp
WHATSAPP_RECIPIENTS = sys.argv[2]  # recebe o número ou a lista de destinatários separados por vírgula
URL_ZABBIX = "https://URL_DO_SEU_ZABBIX"
USER = "USER_DO_ZABBIX_COM_PERMISSÕES"
PASS = "SENHA_DO_ZABBIX_COM_PERMISSÕES"
log_file = '/usr/lib/zabbix/alertscripts/zabbix_whatsapp.log'
max_log_size = 10 * 1024 * 1024
log_count = 1

WIDTH = "800"
HEIGHT = "250"
DRAW_TYPE = "5"
PERIOD = "3600"
NOW = datetime.now()

logger.add(log_file, rotation=max_log_size, retention=log_count)

def get_cookie():
    with httpx.Client() as client:
        response = client.get(
            f"{URL_ZABBIX}/index.php?login=1&name={USER}&password={PASS}&enter=Enter"
        )
        return response.cookies

def extract_item_id(mensagem):
    match = re.search(r'Item ID:\s*(\d+)', mensagem)
    if match:
        return match.group(1)
    return None

def get_image(item_id, item_name, color_code):
    with httpx.Client() as client:
        response = client.get(
            f"{URL_ZABBIX}/chart3.php?name={item_name}&period={PERIOD}&items[0][itemid]={item_id}&items[0][drawtype]={DRAW_TYPE}&items[0][color]={color_code}&width={WIDTH}&height={HEIGHT}",
            cookies=get_cookie()
        )
        return response.content

def send_to_whatsapp(recipients, message, image_data):
    try:
        files = {"file": ("zabbix_graph.jpg", image_data, "image/jpeg")}
        data = {"recipients": recipients, "message": message}
        with httpx.Client(timeout=60) as client:  # Timeout de 60 segundos:
            response = client.post(WHATSAPP_API_URL, data=data, files=files)
            response.raise_for_status()
            logger.info(f"Mensagem enviada para {recipients}")
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem para WhatsApp: {e}")

async def main():
    try:
        assunto = sys.argv[3]
        mensagem = sys.argv[4]
        item_id = extract_item_id(mensagem)

        color_code_match = re.search(r'#(.*?)#', mensagem)
        if color_code_match:
            color_code = color_code_match.group(1)
            mensagem = mensagem.replace(color_code_match.group(0), "")
        else:
            color_code = "00C800"

        if item_id:
            zapi = ZabbixAPI(URL_ZABBIX)
            zapi.session.verify = False
            zapi.login(USER, PASS)
            item = zapi.item.get(filter={"itemid": item_id})

            if item:
                item_name = item[0]["name"]
                image_data = get_image(item_id, item_name, color_code)
                mensagem_completa = f"{assunto}\n\n{mensagem}"
                send_to_whatsapp(WHATSAPP_RECIPIENTS, mensagem_completa, image_data)
            else:
                logger.error(f"Item ID '{item_id}' não encontrado no Zabbix.")
        else:
            logger.error("Item ID não encontrado na mensagem.")
    except Exception as e:
        logger.exception("Ocorreu um erro:", exc_info=e)

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
