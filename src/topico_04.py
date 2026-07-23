import streamlit as st

@st.cache_data
def topico_4_1_denylists():
    with st.echo():
        # 1. Lista de palavras bloqueadas
        projetos_secretos = ["Projeto Alpha", "Servidor Zeus", "Código Delta"]

        # 2. Texto recebido pelo sistema
        frase_original = "O novo funcionário terá acesso ao Servidor Zeus amanhã."
        
        for projeto in projetos_secretos:
            if projeto in frase_original:
                frase_identificada = frase_original.replace(projeto, f":green[{projeto}]")
                frase_protegida = frase_original.replace(projeto, ":red[{CONTEUDO-BLOQUEADO}]")

    with st.container(border=True):
        st.markdown(frase_identificada)
        st.markdown(frase_protegida)


@st.cache_data
def topico_4_2_regex():

    with st.echo():
        import re

        # 1. Molde criado (Expressão Regular)
        molde_email = r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}"

        # 2. Texto recebido pelo sistema
        frase_original = "O contato do cliente é suporte@exemplo.com."

        # 3. Ação do sistema para censurar
        resultado_busca = re.search(molde_email, frase_original)
        
        if resultado_busca:
            email_encontrado = resultado_busca.group()
            frase_identificada = frase_original.replace(email_encontrado, f":green[{email_encontrado}]")
            frase_protegida = frase_original.replace(email_encontrado, ":red[{CONTEUDO-BLOQUEADO}]")

    with st.container(border=True):
        st.markdown(frase_identificada)
        st.markdown(frase_protegida)


@st.cache_data
def topico_4_3_ner():

    with st.echo():
        # 1. Textos recebidos pelo sistema
        frase_contexto_pessoa = "O cliente Leão cancelou o pedido de compra."
        frase_contexto_animal = "O leão escapou do zoológico ontem à noite."

        # 2. Simulação da detecção por Inteligência Artificial (NER)
        entidade_encontrada = "Leão"
        
        # 3. Ação do sistema nas duas situações
        identificada_pessoa = frase_contexto_pessoa.replace(entidade_encontrada, f":green[{entidade_encontrada}]")
        protegida_pessoa = frase_contexto_pessoa.replace(entidade_encontrada, ":red[{CONTEUDO-BLOQUEADO}]")
        
        # O sistema ignora a segunda frase pois o contexto trata de um animal
        identificada_animal = frase_contexto_animal.replace(entidade_encontrada.lower(), f":orange[{entidade_encontrada.lower()}]")

    with st.container(border=True):
        st.markdown(identificada_pessoa)
        st.markdown(protegida_pessoa)
        
    with st.container(border=True):
        st.markdown(identificada_animal)
        st.markdown(frase_contexto_animal)


def topico_4_4_checksum():
    with st.container(border=True, gap="small"):
        st.write("")
        simular_acerto = st.toggle("Simular cálculo válido do CPF")
        st.write("")

    with st.echo():
        # 1. Texto recebido pelo sistema
        frase_original = "O cliente enviou o documento 123.456.789-00 para cadastro."
        documento_encontrado = "123.456.789-00"

        # 2. Simulação do cálculo oficial de validação (Checksum)
        soma_dos_digitos_confere = simular_acerto
        
        # 3. Ação do sistema
        if soma_dos_digitos_confere:
            # Se a conta fosse exata o sistema aplicaria a censura
            frase_identificada = frase_original.replace(documento_encontrado, f":green[{documento_encontrado}]")
            frase_protegida = frase_original.replace(documento_encontrado, ":red[{CONTEUDO-BLOQUEADO}]")
        else:
            # O cálculo falhou e o sistema descarta o bloqueio por ser um dado falso
            frase_identificada = frase_original.replace(documento_encontrado, f":orange[{documento_encontrado}]")
            frase_protegida = frase_original

    with st.container(border=True):
        st.markdown(frase_identificada)
        st.markdown(frase_protegida)


@st.cache_data
def topico_4_5_context_words():

        with st.echo():
            # 1. Texto recebido pelo sistema
            frase_original = "O acesso ao sistema requer a senha Assembleia123 para iniciar."

            # 2. Definição da pista de contexto e do dado numérico
            palavra_pista = "senha"
            dado_suspeito = "Assembleia123"

            # 3. Ação do sistema analisando a proximidade
            if palavra_pista in frase_original:
                # A máquina encontra a pista e confirma a sensibilidade do número
                frase_identificada = frase_original.replace(palavra_pista, f":blue[{palavra_pista}]")
                frase_identificada = frase_identificada.replace(dado_suspeito, f":green[{dado_suspeito}]")
                
                frase_protegida = frase_original.replace(dado_suspeito, ":red[{CONTEUDO-BLOQUEADO}]")

        with st.container(border=True):
            st.markdown(frase_identificada)
            st.markdown(frase_protegida)