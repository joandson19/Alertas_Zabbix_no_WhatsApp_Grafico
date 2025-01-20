
# 🛠️ Alertas do Zabbix no WhatsApp com Gráficos

### 🚨 Pré-requisitos: Configurar o WhatsApp-Web-js
Antes de mais nada, será necessário instalar o projeto [**WhatsApp-Web-js**](https://github.com/remontti/RR-WhatsApp-API) do [Rudimar](https://blog.remontti.com.br/8109). Após criar o servidor de API WhatsApp-Web-js, siga os passos abaixo para configurar o script.

---

## 🧰 Passo a passo para configuração no servidor do Zabbix

### 1️⃣ Instalar as dependências necessárias
Execute o seguinte comando para instalar as bibliotecas Python requeridas:

```bash
sudo -H -u zabbix python3 -m pip install pyzabbix httpx loguru
```
### 2️⃣ Clonar e configurar os scripts
* Adicione o script notifica-whatsapp.py dentro de /usr/lib/zabbix/alertscripts/ e crie a pasta log.
```
# cd /tmp
# git clone https://github.com/joandson19/Alertas_Zabbix_no_WhatsApp_Grafico.git
# cd Alertas_Zabbix_no_WhatsApp_Grafico
# mv * /usr/lib/zabbix/alertscripts/
```
### 3️⃣ Configurar permissões
```
# chown zabbix:zabbix -R /usr/lib/zabbix/alertscripts/*
# chmod  +x /usr/lib/zabbix/alertscripts/notifica-whatsapp.py
```
### 4️⃣ Editar configurações do script
* Edite o arquivo notifica-whatsapp.py alterando as linha que fazem referencia a (url, login e senha)
  Importante dizer que o usuario precisa ter no minimo permissão de leitura.
```
URL_ZABBIX = "https://URL DO ZABBIX"
USER = "USUARIO DO ZABBIX"
PASS = "SENHA DO ZABBIX"
```
### 5️⃣ Formato obrigatório para mensagens
* Importante falar que o "Item ID: {ITEM.ID1}" é obrigatorio no corpo da mensagem para que o grafico funcione.
Segue um modelo de mensagem, o assunto fica live a sua escolha.
```
⏰ Inicio do problema às {EVENT.TIME} em {EVENT.DATE}
Host: {HOST.NAME}
Serveridade: {EVENT.SEVERITY}
Último valor: {ITEM.VALUE1}
Item ID: {ITEM.ID1}
```
### 6️⃣ Configurar o "Tipo de Mídia" no Zabbix
* A URL deve apontar para o servidor da API criado no início.
* Configure os detalhes do "Tipo de Mídia" conforme o exemplo:
  
![image](https://github.com/user-attachments/assets/c065f16b-97e0-4cb6-9006-73c29ddef975)


### 7️⃣ Configuração da mídia do usuário
* Configure as notificações no Zabbix para o usuário, como demonstrado abaixo:

![image](https://github.com/user-attachments/assets/f21d6955-9785-4f0f-b275-a5921c8a7ddb)


### 8️⃣ Personalizar as cores do gráfico
Você pode alterar a cor do gráfico adicionando um código de cor no formato HTML no corpo da mensagem. Exemplos:

* Vermelho: #FF0000#
* Verde: #00C800#
Adicione o código da cor entre #, como #CODIGODACOR#.

* Exemplo para incidente:
  
![image](https://github.com/joandson19/Alertas_Zabbix_no_Telegram_Grafico/assets/36518985/a6f09bb1-888d-42cb-9dad-02528d823876)
* Exemplo para resolução:
  
![image](https://github.com/joandson19/Alertas_Zabbix_no_Telegram_Grafico/assets/36518985/5ee6f68b-3212-4fe4-b51c-879448e1ff4b)

### 9️⃣ Testar as notificações no WhatsApp
* Após configurar, faça um teste para verificar as notificações no WhatsApp:

![image](https://github.com/user-attachments/assets/03a4a88b-62b5-4ef5-8991-3437dee12f36)

----------------------------------------------------
📜 Créditos

#### A integração com o WhatsApp foi possível graças ao incrível projeto WhatsApp-Web-js, desenvolvido por [Rudimar Remontti](https://blog.remontti.com.br/8109). Agradecimentos especiais ao Rudimar pelo excelente trabalho e contribuição à comunidade.
