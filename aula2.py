import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_excel('teste.xlsx')

nomes=list(df['NOME'].unique())
sexos=list(df['SEXO'].unique())

df['DATA']=pd.to_datetime(df['DATA'],format='%y-%m-%d')

nome=st.sidebar.selectbox('Escola o cliente',['TODOS']+nomes)
sexo=st.sidebar.selectbox('Escola o sexo',['TODOS']+sexos)
#st.text('Cliente',nome)


if (nome !='TODOS'):  
    st.header('Mostrando resultado de '+nome)
    df=df[df['NOME']==nome]
else:
   st.header('Mostrando todos os clientes')


if (sexo !='TODOS'):  
    st.subheader('Mostrando resultado de sexo '+sexo)
    df=df[df['SEXO']==sexo]
else:
   st.subheader('Mostrando todos os sexos')

dfshow=df.groupby(by=['DATA']).sum()

#st.text(dfshow)


fig = px.line(dfshow,x=dfshow.index,y='PESO')
#fig.update_layout(title='grafico')
st.plotly_chart(fig,use_container_width=True)








