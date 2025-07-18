import streamlit as st
import pandas as pd
import mongo_client




df = pd.DataFrame(mongo_client.listar_tabela(colecao='AccessPoint-data',filtro={}))
df['uptime'] = pd.to_timedelta(df['uptime'], unit='s')
df['uptime_str'] = df['uptime'].astype(str).str.replace('day', 'dia')
df.sort_values(by='ip', key=lambda x: x.str.split('.').apply(lambda parts: [int(p) for p in parts]), ascending=True, inplace=True)
st.write('## Access Point Table')
st.dataframe(data=df[['ip', 'name', 'mac', 'clientCount', 'model','serial','uptime_str']],
            hide_index=True,
            height=800,
            width=None,
            column_config={
                "mac": "Mac Address",
                "name": "Nome",
                'ip': "Ip Address",
                "clientCount":'Clientes',
                'model': "Modelo",
                "uptime_str" :  "Tempo Ativo",
            })