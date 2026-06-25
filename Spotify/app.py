import streamlit as st



musicas = {
    "MC Kevin":{ 
    "sentimentos":"https://www.youtube.com/watch?v=fL1V7yOiV7U",
    "uma luta por dia":"https://www.youtube.com/watch?v=s-PwNH3BgkY&list=RDs-PwNH3BgkY&start_radio=1&pp=ygUgbWMga2V2aW4gbXVzaWNhIHVtYSBsdXRhIHBvciBkaWGgBwE%3D"
    },
    "NandaTsunami":{
     "Pq Vc Não Me Liga?":"https://www.youtube.com/watch?v=GFwBaWtPCrA&pp=ygUebmFuZGF0c3VuYW1pIHBxIHZjIG5hbyBtZSBsaWdh",
     "segredo e feitiço":"https://www.youtube.com/watch?v=lmkFZm6bKYM&pp=ygUebmFuZGF0c3VuYW1pIHBxIHZjIG5hbyBtZSBsaWdh"
    },
    "Anitta":{
    "Ritimo perfeito":"https://www.youtube.com/watch?v=Y1rxJ5NPw00&list=RDY1rxJ5NPw00&start_radio=1&pp=ygUWYW5pdHRhIHJpdG1vIHBlcmZlaXRvIKAHAdIHCQk-CwGHKiGM7w%3D%3D",
    "Cravo e canela":"https://www.youtube.com/watch?v=32_of3wNAMM&list=RD32_of3wNAMM&start_radio=1&pp=ygUVYW5pdHRhIGNyYXZvIGUgY2FuZWxhoAcB"
    }, 
    "Luiz do Lins":{
    "A musica mais triste do ano":"https://www.youtube.com/watch?v=t5SEyQ-Lqps&list=RDt5SEyQ-Lqps&start_radio=1&pp=ygUlbHVpeiBsaW5zIGEgbXVzaWNhIG1haXMgdHJpc3RlIGRvIGFub6AHAQ%3D%3D",
    "Saudades":"https://www.youtube.com/watch?v=IfVqba_ey54&list=RDIfVqba_ey54&start_radio=1&pp=ygUTbHVpeiBsaW5zIHNhdWRhZGVzIKAHAQ%3D%3D"
    },
    "Brocasito":{
    "Miami":"https://www.youtube.com/watch?v=v13TknABICc&list=RDv13TknABICc&start_radio=1&pp=ygUPYnJvY2FzaXRvIG1pYW1poAcB",
    "Suvage":"https://www.youtube.com/watch?v=AoWeelwT1Io&list=RDAoWeelwT1Io&start_radio=1&pp=ygUQYnJvY2FzaXRvIHNhdmFnZaAHAQ%3D%3D"
    }
}

st.sidebar.image("Logo.png")
artista = st.sidebar.selectbox("Selecione o artista", musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)
for musica in musicas_artista.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)
  