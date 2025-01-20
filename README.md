
# Alertas_Zabbix_no_WhatsApp_Grafico

### 🚨 Antes de mais nada será necessário instalar o projeto WhatsApp-Web-js do Rudimar disponivel no https://github.com/remontti/RR-WhatsApp-API 🚨
### Após criar o servidor de API WhatsApp-Web-js no link acima poderá seguir o passos abaixo.

* Instale as dependencias para o script
```
# sudo -H -u zabbix python3 -m pip install pyzabbix httpx loguru
```
* Adicione o script notifica-whatsapp.py dentro de /usr/lib/zabbix/alertscripts/ e crie a pasta log.
```
# cd /tmp
# git clone https://github.com/joandson19/Alertas_Zabbix_no_WhatsApp_Grafico.git
# cd Alertas_Zabbix_no_WhatsApp_Grafico
# mv * /usr/lib/zabbix/alertscripts/
```
* dê as permissões necessárias
```
# chown zabbix:zabbix -R /usr/lib/zabbix/alertscripts/*
# chmod  +x /usr/lib/zabbix/alertscripts/notifica-whatsapp.py
```
* Edite o arquivo notifica-whatsapp.py alterando as linha que fazem referencia a (url, login e senha)
  Importante dizer que o usuario precisa ter no minimo permissão de leitura.
```
URL_ZABBIX = "https://URL DO ZABBIX"
USER = "USUARIO DO ZABBIX"
PASS = "SENHA DO ZABBIX"
```
* Importante falar que o "Item ID: {ITEM.ID1}" é obrigatorio no corpo da mensagem para que o grafico funcione.
Segue um modelo de mensagem, o assunto fica live a sua escolha.
```
⏰ Inicio do problema às {EVENT.TIME} em {EVENT.DATE}
Host: {HOST.NAME}
Serveridade: {EVENT.SEVERITY}
Último valor: {ITEM.VALUE1}
Item ID: {ITEM.ID1}
```
* Segue abaixo modo que tem que ficar o "Tipo de Mídia"
* A URL é a do servidor da API que você criu no inicio.
  
![image](https://github.com/user-attachments/assets/c065f16b-97e0-4cb6-9006-73c29ddef975)


* Segue configuração de Midia do Usuario!

![image](https://github.com/user-attachments/assets/f21d6955-9785-4f0f-b275-a5921c8a7ddb)


* Segue exemplo para incidente
  Caso queira mudar a cor do grafico e só por no corpo da mensagem #FF0000# para vermelho ou #00C800# paraverde. Ou também poderá 
  adicionar qualquer outra cor colocando entre ## como #CODIGODACOR# no formato html!
#
  
![image](https://github.com/joandson19/Alertas_Zabbix_no_Telegram_Grafico/assets/36518985/a6f09bb1-888d-42cb-9dad-02528d823876)
* Segue exemplo para resolvido
  
![image](https://github.com/joandson19/Alertas_Zabbix_no_Telegram_Grafico/assets/36518985/5ee6f68b-3212-4fe4-b51c-879448e1ff4b)

* Testando as notificações no WhatsApp

![image](https://github.com/user-attachments/assets/8f6b19e8-ec13-4c2c-b248-20dfcbf0a6be)





