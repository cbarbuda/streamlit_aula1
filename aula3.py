import pandas as pd
import streamlit as st

df=pd.read_excel('abs.xlsx')
ccustos = list(df['centrocusto'].unique())
placas = list(df['placa'].unique())
motoristas = list(df['motorista'].unique())

st.sidebar.button('Cadastros',use_container_width=1)
st.sidebar.button('Monitoramento',use_container_width=1)
st.sidebar.button('Lançamentos',use_container_width=1)
st.sidebar.button('Entrada de Notas',use_container_width=1)
st.sidebar.button('Distribuição de Notas',use_container_width=1)
st.sidebar.button('Siga',use_container_width=1)
st.sidebar.button('Relatórios',use_container_width=1)
st.sidebar.button('Sair',use_container_width=1)
st.header('Lançando Abastecimentos')
ccusto=st.selectbox('Centro de Custo',['TODOS']+ccustos)
placa=st.selectbox('Placa',['TODAS']+placas)
motorista=st.selectbox('Motorista',['TODOS']+motoristas)

litros=st.text_input('Litros')
valor=st.text_input('Valor')
st.button('Confirmar',use_container_width=0)