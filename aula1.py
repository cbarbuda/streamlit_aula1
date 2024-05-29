

import pandas as pd
#from pandas.core.api import DatetimeTZDtype
import streamlit as st
import plotly.express as px
from datetime import datetime

df=pd.read_excel('C:\Projeto payton_web\lista\lista.xlsx')
placa=list(df['placa'].unique())
centrocusto=list(df['centrocusto'].unique())
motorista=list(df['motorista'].unique())
#codmotorista=list(df['codmotorista'].unique())


#vdata=datetime(2024,7,10)
#df['date']=pd.to_datetime(df(['date'], format='%Y-,%m-,%d'))
centrocusto=st.selectbox('cento',['TODAS']+centrocusto)
placa=st.selectbox('Escolha a placa',['Todas']+placa)
motorista=st.selectbox('Motorista',['Todos']+motorista)

litros=st.text_input('Litros') 
vr=st.text_input('vr')
st.button('Confirmar',
          use_container_width=0)


print(motorista)

#centrocusto=st.sidebar.selectbox('cento',['TODAS']+centrocusto)


if (placa!='Todas'):
    st.text('Mostrando o resultado de Todas as '+placa)
    df=df[df['placa']==placa]

if (motorista!='Todos'):
    st.text('Mostrando o resultado de Todos as '+motorista)
    df=df[df['motorista']==motorista]
   

#CDprint(vdata)
#dfshow =df.groupby('centrocusto')

#fig=px.line(dfshow,x=1,y=0)
#fig=px.line(dfshow,x=dfshow.indices,y=1)
#fig.update_layout(title='Total de abastecimentos')
#st.plotly_chart(placa,vdata,use_container_width='true')    
#st.plotly_chart(placa,vdata)    

st.sidebar.button('Cadastro',use_container_width=1)
st.sidebar.button('Monitoramento',use_container_width=1)
st.sidebar.button('Lançamentos',use_container_width=1)
st.sidebar.button('Entrada Notas',use_container_width=1)
st.sidebar.button('Distribuição',use_container_width=1)
st.sidebar.button('Relatórios',use_container_width=1)
st.sidebar.button('Siga',use_container_width=1)
st.sidebar.button('Suporte',use_container_width=1)
st.sidebar.button('Sair',use_container_width=1)




#print(df)