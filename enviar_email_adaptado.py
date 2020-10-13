# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:59:55 2020

@author: same_
"""

import smtplib
from email.mime.text import MIMEText
import pandas as pd
import numpy as np

 # importação dos dados dos inscritos

inscritos = pd.read_excel('teste_formulario.xlsx')

n_inscritos = inscritos.shape[0]   #qnt de inscritos

lista_email = list(inscritos.email)

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'samelius1@gmail.com'
password = '34972574'


# definição da função de envio
def envio (username,password):
    
       
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    
    server.login(username, password)
    server.sendmail(remetente, destinatario, message.as_string())
    server.quit()
    

# fim da função

for i in range(n_inscritos):
    
    
    remetente = 'Centrismo'
    destinatario = inscritos["email"][i]
    lista_email = list()
    lista_email.append(destinatario)

    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    
    # OBS: Falta colocar o loop
    for i in range()
    
    message = MIMEText(f'Bom dia { inscritos["Nome"][i]} voce foi convidado para participar no nosso grupo. Voce nos informou que tem { inscritos["idade"][i] } anos e atua na area de {inscritos["area"][i]}' )
    message['subject'] = 'Processo Seletivo'
    message['from'] = remetente
    message['to'] =', '.join(lista_email)
    
    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    
    envio(username, password)   #chama a função envio para cada linha do dados
    
