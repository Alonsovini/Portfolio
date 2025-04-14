# Projeto para criar o meu portfolio pessoal

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Portfólio", page_icon="🤖", layout="wide")

# CSS personalizado para o cabeçalho e cartões
st.markdown("""
<style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #4b5a66;
        color: white;
        position: sticky;
        top: 0;
        z-index: 1000;
        margin-bottom: 40px
    }
    .header a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    .header a:hover {
        text-decoration: underline;
    }
    .social-links {
        display: flex;
        gap: 10px;
    }
    .sobre-mim {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .sobre-mim img {
        border-radius: 10px;
        max-width: 300px;
    }
    .stApp {
        background: linear-gradient(135deg, #9fa5d5, #e8f5c8);
        background-attachment: fixed;
        background-size: cover;
    }
    .card {
        background: #4b5a66;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .card h3 {
        margin-top: 0;
    }
    .card a {
        color: #0078d4;
        text-decoration: none;
    }
    .card a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("""
<div class="header">
    <div>
        <a href="#sobre-mim">Home</a>
        <a href="#meus-projetos">Meus Projetos</a>
        <a href="#dashboards">Dashboards Em Power BI</a>
        <a href="#contato">Contato</a>
    </div>
    <div class="social-links">
        <a href="https://github.com/Alonsovini" target="_blank">
            <img src="https://img.icons8.com/ios-filled/30/ffffff/github.png" alt="GitHub">
        </a>
        <a href="http://linkedin.com/in/vinicius-alonso-04252219a" target="_blank">
            <img src="https://img.icons8.com/ios-filled/30/ffffff/linkedin.png" alt="LinkedIn">
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Seção de Introdução
st.markdown("<a id='sobre-mim'></a>", unsafe_allow_html=True)
st.header("Sobre Mim")

# Layout em colunas para texto e imagem
col1, col2 = st.columns([3, 1])  # A primeira coluna é 2x maior que a segunda

with col1:
    st.write("""
    Sou um profissional apaixonado por automações e análise de dados, transformando processos manuais em soluções eficientes. \n
    Meu portfólio reúne projetos que otimizam fluxos de trabalho e geram insights estratégicos com Power BI. \n
    Sempre buscando inovação, utilizo tecnologia para simplificar e potencializar resultados.
    - **Nome**: Vinicius Alonso
    - **Cargo**: Analista de Dados
    - **Localização**: São Paulo, Brasil
    - **Habilidades**: Python, Power BI, SQL, Java, AWS Cloud e Análise de Dados.
    """)

    # Botão para baixar currículo
    with open("Curriculo.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label="Baixar Currículo",
        data=PDFbyte,
        file_name="Curriculo.pdf",
        mime="application/pdf",
    )

with col2:
    st.image("Eu.png", width=200)  # width como tamanho máximo
    st.write("")  # Espaçador vazio
    st.write("")  # Adicione mais se necessário

# Seção de Projetos
st.markdown("<a id='meus-projetos'></a>", unsafe_allow_html=True)
st.header("Meus Projetos")
st.write("Aqui estão alguns dos meus projetos em Python:")

# Layout em colunas para os projetos
col3, col4 = st.columns(2)  # Duas colunas para os projetos

with col3:
    st.markdown("""
    <div class="card">
        <h3>PDF Merge</h3>
        <p>Aplicativo desenvolvido em Python com PyQt5 para unificar e editar arquivos PDF de forma visual e intuitiva. 
        Permite selecionar, visualizar, reorganizar, remover páginas e unir múltiplos PDFs em um único arquivo.</p>
        <a href="https://github.com/Alonsovini/PDF_Merge" target="_blank">Ver no GitHub</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>Processamento de Extratos Financeiros</h3>
        <p>Aplicação em Python com PyQt5 que automatiza a conversão e filtragem de extratos financeiros, 
        gerando arquivos .csv prontos para o sistema LBC, com interface gráfica e processamento assíncrono..</p>
        <a href="https://github.com/Alonsovini/Conciliacao_Financeiro" target="_blank">Ver no GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# Seção de Dashboards do Power BI
st.markdown("<a id='dashboards'></a>", unsafe_allow_html=True)
st.header("Dashboards Em Power BI")
st.write("Aqui estão alguns dos meus dashboards criados no Power BI:")

# Layout em colunas para os dashboards
col5, col6 = st.columns(2)  # Duas colunas para os dashboards

with col5:
    st.markdown("""
        <div class="card">
            <h3>Dashboard 1: Projeto Sistema</h3>
            <p>Tarefas Do Projeto de Implantação de Sistema.</p>
            <a href="https://app.powerbi.com/links/uCEglpxYqa?ctid=bbd39cf5-702a-4dcd-866c-1839d1b857cb&pbi_source=linkShare" target="_blank">Abrir no Power BI</a>
        </div>
        """, unsafe_allow_html=True)
    st.image("dashboard1.jpg", use_container_width=True, output_format="JPEG")

with col6:
    st.markdown("""
    <div class="card">
        <h3>Dashboard 2: Controle de Equipamentos</h3>
        <p>Projeto Que Mostra Todas As Informações Referente Aos Equipamentos Das Empresas.</p>
        <a href="https://app.powerbi.com/links/uZXxTBOgBr?ctid=bbd39cf5-702a-4dcd-866c-1839d1b857cb&pbi_source=linkShare" target="_blank">Abrir no Power BI</a>
    </div>
    """, unsafe_allow_html=True)
    st.image("dashboard2.jpg", use_container_width=True, output_format="JPEG")

# Adicionar mais dashboards abaixo (se necessário)
col7, col8 = st.columns(2)

with col7:
    st.markdown("""
    <div class="card">
        <h3>Dashboard 3: Chamados!</h3>
        <p>Uma Forma de Visualizar Todos Os Chamados Do Departamento.</p>
        <a href="https://app.powerbi.com/links/24oYbfCLL8?ctid=bbd39cf5-702a-4dcd-866c-1839d1b857cb&pbi_source=linkShare&bookmarkGuid=6e758a21-7f8d-40f1-ac57-d1b43824ab47" target="_blank">Abrir no Power BI</a>
    </div>
    """, unsafe_allow_html=True)
    st.image("dashboard3.jpg", use_container_width=True, output_format="JPEG")

with col8:
    st.markdown("""
        <div class="card">
            <h3>Dashboard 4: Levantamento Com Projeções</h3>
            <p>Projeto Para Visualizar Os Gastos Com Sistemas E Projeção De Gastos Para Os Próximos Meses.</p>
            <a href="https://app.powerbi.com/links/giKHaNpP-u?ctid=bbd39cf5-702a-4dcd-866c-1839d1b857cb&pbi_source=linkShare" target="_blank">Abrir no Power BI</a>
        </div>
        """, unsafe_allow_html=True)
    st.image("dashboard4.jpg", use_container_width=True, output_format="JPEG")

# Seção Contato
st.markdown("<a id='contato'></a>", unsafe_allow_html=True)
st.header("Contato")
st.write("""
Se você quiser entrar em contato comigo, aqui estão minhas informações:
- **E-mail**: vinicius_alonso@outlook.com.br
- **LinkedIn**: http://linkedin.com/in/vinicius-alonso-04252219a
- **GitHub**: https://github.com/Alonsovini

Portfólio Desenvolvido 100% Em Python.
""")