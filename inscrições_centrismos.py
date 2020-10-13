# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:00:03 2020

@author: same_
"""

import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

dados = pd.read_excel("seletivo_centrismos.xlsx")

#-------lista de informações pessoais--------
nomes= list(dados['Nome completo'].str.title())  # formata os nomes 
emails = list(dados['E-mail'])
idade = list(dados['Idade'])
estado = list(dados['Estado'])
telefone = list(dados['Telefone'])
#-------end----------
dados['Nome completo'] = nomes

#-----idiomas-------
ing = dados['idiomas [Inglês]'].value_counts()
esp=dados['idiomas [Espanhol]'].value_counts()
ale=dados['idiomas [Alemão]'].value_counts()
fra=dados['idiomas [Francês]'].value_counts()
ita=dados['idiomas [Italiano]'].value_counts()
#-------end------------


#print(dados['Estado'].value_counts())


#-----Tabelas de cada setor------

grafico = dados[dados['Setor Gráfico']=='Sim']
editor = dados[dados['Setor Edição']=='Sim']
academico = dados[dados['Setor Acadêmico']=='Sim']
tecnico = dados[dados['Setor Técnico']=='Sim']

#------end-------

#-----Setor academico por assuntos------



for i in academico['Assuntos'].index:
    academico["Assuntos"][i]=academico["Assuntos"][i].split(',')



lista_index_econ = []
lista_index_dir = []
lista_index_pol = []
lista_index_fil = []
lista_index_polex = []
lista_index_ecol = []
lista_index_hum = []
lista_index_geo = []

for i in academico['Assuntos'].index:
    for j in range(len(academico['Assuntos'][i])):
        
        # if academico['Assuntos'][i][j][0] == ' ':
        #     academico['Assuntos'][i][j] = academico['Assuntos'][i][j].replace(academico['Assuntos'][i][j][0],'')
        
        if academico['Assuntos'][i][j] == 'Economia':
            lista_index_econ.append(i)
        if academico['Assuntos'][i][j] == 'Política' :
            lista_index_pol.append(i)
        if academico['Assuntos'][i][j] == 'Direito':
            lista_index_dir.append(i)
        if academico['Assuntos'][i][j] == 'Política externa':
            lista_index_polex.append(i)
        if academico['Assuntos'][i][j] == 'Filosofia e filosofia política':
            lista_index_fil.append(i)
        if academico['Assuntos'][i][j] == 'Ecologia':
            lista_index_ecol.append(i)
        if academico['Assuntos'][i][j] == 'Ciências sociais e humanidades':
            lista_index_hum.append(i)
        if academico['Assuntos'][i][j] == 'Geografia':
            lista_index_geo.append(i)
    
#-----Visualizar o setor academico por area de interesse

# academico.loc[lista_index_dir,:]
# academico.loc[lista_index_econ,:]
# academico.loc[lista_index_pol,:]
# academico.loc[lista_index_polex,:]
# academico.loc[lista_index_ecol,:]
# academico.loc[lista_index_geo,:]
# academico.loc[lista_index_hum,:]
# academico.loc[lista_index_fil,:]


#------end------


#--------Setor Tecnico--------

for i in tecnico['Setor Técnico (função)'].index:
    tecnico['Setor Técnico (função)'][i]=tecnico['Setor Técnico (função)'][i].split(',')
    

lista_index_prog = []
lista_index_dados = []

for i in tecnico['Setor Técnico (função)'].index:
    for j in range(len(tecnico['Setor Técnico (função)'][i])):
        
        # if academico['Assuntos'][i][j][0] == ' ':
        #     academico['Assuntos'][i][j] = academico['Assuntos'][i][j].replace(academico['Assuntos'][i][j][0],'')
        
        if tecnico['Setor Técnico (função)'][i][j] == 'Programação':
            lista_index_prog.append(i)
        if tecnico['Setor Técnico (função)'][i][j] == ('Ciência de dados'):
            lista_index_dados.append(i)
        
    


            

#------------


#-----Abrir redes sociais----------

#--- este loop abre os perfis do twitter e instagram dos inscritos

# for i in dados.Twitter.dropna().index:
#     webbrowser.open_new_tab('https://twitter.com/'+dados.Twitter[i])
    
# for i in dados.Instagram.dropna().index:
#      webbrowser.open_new_tab('https://instagram.com/'+dados.Instagram[i])

#---------end----------


#------Visualização dos dados-------

# dados.Estado.value_counts().plot(x = 'Estados',kind='bar')

# plt.bar(dados.Estado.value_counts().index,dados.Estado.value_counts().values)
# plt.title('Distribuição por estados')


# plt.pie(ing.values,labels = ing.index,autopct= '%1.1f%%')
# plt.title('Nivel de ingles')





