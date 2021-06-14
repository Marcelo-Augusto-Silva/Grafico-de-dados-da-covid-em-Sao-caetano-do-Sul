import pandas as pd 
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(20,10))

dados = pd.read_csv('HIST_PAINEL_COVIDBR_Parte3_13jun2021.csv', ';')  # Impotando a BAse de dados

data_recente = dados.data >= '2021-05-01'  # selecionando somente os dados com a data depois de 2021-05-01

dados1 = dados[data_recente]     

scs = dados1[dados1.municipio == 'São Caetano do Sul']  # selecionando os dados de scs

scs.index = scs.data  # trocando o numero do index pela data 


# criando o grafico com o total de novos casos de covid por dia 
fig1 = scs[['casosNovos']].plot.bar(color='purple')
fig1.set_title('TOTAL DE NOVOS CASOS DE COVID POR DIA(SCS)',{'fontsize': 26})
fig1.set_ylabel('TOTAL DE CASOS', {'fontsize': 22})
fig1.set_xlabel('DATA', {'fontsize': 19})
fig1.tick_params(labelsize=17)

# criando o grafico de total de obitos por dia 
fig2 = scs[['obitosNovos']].plot.bar(color='blue')
fig2.set_title('TOTAL DE ÓBITOS POR DIA (SCS)',{'fontsize': 26})
fig2.set_ylabel('TOTAL DE ÓBITOS', {'fontsize': 22})
fig2.set_xlabel('DATA', {'fontsize': 19})

