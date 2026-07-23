import streamlit as st
import pandas as pd

def plotar_texto_colorido(texto, resultados):
    resultados_ordenados = sorted(resultados, key=lambda x: (x.start, -(x.end - x.start)))

    resultados_limpos = []
    ultimo_fim = 0

    for item in resultados_ordenados:
        if item.start >= ultimo_fim:
            resultados_limpos.append(item)
            ultimo_fim = item.end

    resultados_limpos.reverse()

    texto_pintado = texto

    for item in resultados_limpos:
        inicio = item.start
        fim = item.end
        etiqueta = item.entity_type
        pontuacao = f"{item.score:.2f}"

        pedaco_sensivel = texto_pintado[inicio:fim]

        if item.score >= 0.50 and item.score <= 0.75:
            marcador = f'<mark style="background-color: #fef08a; color: #854d0e; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'
        elif item.score < 0.50:
            marcador = f'<mark style="background-color: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'
        elif item.score > 0.75:
            marcador = f'<mark style="background-color: #dcfce7; color: #166534; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'

        texto_pintado = texto_pintado[:inicio] + marcador + texto_pintado[fim:]

    caixa_visual = f'<div style="font-size: 15px; line-height: 2.2; padding: 24px; background-color: #ffffff; color: #1a1a1a; border: 1px solid #e5e7eb; border-radius: 12px; white-space: pre-wrap; margin-bottom: 20px;">{texto_pintado}</div>'

    st.markdown(caixa_visual, unsafe_allow_html=True)


def plotar_tabela_colorida(dicionario_dados, resultados_analise):

    mapa_resultados = {}

    for item in resultados_analise:
        coluna = item.key

        for indice_linha, lista_resultados in enumerate(item.recognizer_results):
            chave_mapa = (coluna, indice_linha)
            mapa_resultados[chave_mapa] = lista_resultados

    colunas = list(dicionario_dados.keys())
    quantidade_linhas = len(dicionario_dados[colunas[0]])

    estilos_tabela = """
    <style>
        .tabela-presidio {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            text-align: left;
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .tabela-presidio th {
            background-color: #f8fafc;
            color: #334155;
            padding: 16px;
            border-bottom: 2px solid #e2e8f0;
            font-weight: 600;
        }
        /* Arredondamento interno do cabeçalho */
        .tabela-presidio th:first-child {
            border-top-left-radius: 11px;
        }
        .tabela-presidio th:last-child {
            border-top-right-radius: 11px;
        }
        .tabela-presidio td {
            padding: 16px;
            border-bottom: 1px solid #e2e8f0;
            color: #1e293b;
            vertical-align: middle;
        }
        .tabela-presidio tr:last-child td {
            border-bottom: none;
        }
        /* Arredondamento interno do rodapé */
        .tabela-presidio tr:last-child td:first-child {
            border-bottom-left-radius: 11px;
        }
        .tabela-presidio tr:last-child td:last-child {
            border-bottom-right-radius: 11px;
        }
        .tabela-presidio tr:hover td {
            background-color: #f1f5f9;
        }
    </style>
    """

    codigo_html = estilos_tabela
    codigo_html += '<table class="tabela-presidio">'
    codigo_html += '<thead><tr>'

    for coluna in colunas:
        codigo_html += f'<th>{coluna}</th>'
    codigo_html += '</tr></thead><tbody>'

    for indice_linha in range(quantidade_linhas):
        codigo_html += '<tr>'

        for coluna in colunas:
            valor_original = str(dicionario_dados[coluna][indice_linha])
            resultados_desta_celula = mapa_resultados.get((coluna, indice_linha), [])

            resultados_ordenados = sorted(resultados_desta_celula, key=lambda x: (x.start, -(x.end - x.start)))
            resultados_limpos = []
            ultimo_fim = 0

            for res in resultados_ordenados:
                if res.start >= ultimo_fim:
                    resultados_limpos.append(res)
                    ultimo_fim = res.end

            resultados_limpos.reverse()
            texto_pintado = valor_original

            for res in resultados_limpos:
                inicio = res.start
                fim = res.end
                etiqueta = res.entity_type
                pontuacao = f"{res.score:.2f}"

                pedaco_sensivel = texto_pintado[inicio:fim]

                if res.score >= 0.50 and res.score <= 0.75:
                    marcador = f'<mark style="background-color: #fef08a; color: #854d0e; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'
                elif res.score < 0.50:
                    marcador = f'<mark style="background-color: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'
                elif res.score > 0.75:
                    marcador = f'<mark style="background-color: #dcfce7; color: #166534; padding: 4px 8px; border-radius: 6px; text-decoration: none;">{pedaco_sensivel} [{etiqueta} : {pontuacao}]</mark>'

                texto_pintado = texto_pintado[:inicio] + marcador + texto_pintado[fim:]

            codigo_html += f'<td>{texto_pintado}</td>'

        codigo_html += '</tr>'

    codigo_html += '</tbody></table>'

    st.markdown(codigo_html, unsafe_allow_html=True)


@st.cache_resource
def carregar_motor_nlp():
    from presidio_analyzer.nlp_engine import NlpEngineProvider

    configuracao_idiomas = {
        "nlp_engine_name": "spacy",
        "models": [
            {"lang_code": "pt", "model_name": "pt_core_news_lg"},
            {"lang_code": "en", "model_name": "en_core_web_lg"}
        ]
    }
    
    provedor = NlpEngineProvider(nlp_configuration=configuracao_idiomas)
    return provedor.create_engine()


def criar_novo_analisador():
    from presidio_analyzer import AnalyzerEngine
    from presidio_anonymizer import AnonymizerEngine
    
    motor_linguagem = carregar_motor_nlp()
    
    analisador = AnalyzerEngine(
        nlp_engine=motor_linguagem, 
        supported_languages=["pt", "en"]
    )
    anonimizador = AnonymizerEngine()
    
    return analisador, anonimizador


@st.cache_data
def topico_5_0_tabela_entidades():

        dicionario_entidades = {
            "CREDIT_CARD": ["Número de cartão de crédito de 12 a 19 dígitos."],
            "CRYPTO": ["Endereço de carteira de criptomoeda. Atualmente focado em Bitcoin."],
            "DATE_TIME": ["Datas e tempos absolutos ou relativos."],
            "EMAIL_ADDRESS": ["Endereço de correio eletrônico."],
            "IBAN_CODE": ["Número internacional de conta bancária para transações globais."],
            "IP_ADDRESS": ["Endereço de protocolo de internet em formato IPv4 ou IPv6."],
            "MAC_ADDRESS": ["Identificador único para interfaces de rede física."],
            "NRP": ["Nacionalidade ou afiliação religiosa e política de uma pessoa."],
            "LOCATION": ["Nomes de locais políticos ou geográficos como cidades e países."],
            "PERSON": ["Nome completo de uma pessoa."],
            "PHONE_NUMBER": ["Número de telefone com suporte ajustável para vários países."],
            "MEDICAL_LICENSE": ["Números comuns de licenças médicas."],
            "URL": ["Endereço ou identificador único de recursos na internet."]
        }

        lista_formatada = []
        for chave, valor in dicionario_entidades.items():
            lista_formatada.append({"Categoria": chave, "Descrição": valor[0]})
            
        tabela_dados = pd.DataFrame(lista_formatada)
        
        plotar_tabela_colorida(tabela_dados.to_dict(orient="list"), [])


def topico_5_1_1():
    analisador, anonimizador = criar_novo_analisador()

    with st.echo():
        # 1. Texto de teste completo
        text_pt = """Prezada coordenação do clube esportivo. Meu nome é João Santos e moro na cidade do Rio de Janeiro. Escrevo esta mensagem para confirmar o meu cadastro de atleta. A taxa de inscrição anual foi paga no dia 17/06/2026. O endereço de rede no momento do acesso foi 192.168.1.15 por meio do portal www.clubeesportivo.com.br."""
        
        # 2. O motor analisa o texto indicando o idioma
        results_pt = analisador.analyze(text=text_pt,language="pt")

        # 3. Exibição do resultado visual colorido
        plotar_texto_colorido(text_pt, results_pt)


def topico_5_1_2_texto_en():
    analisador, anonimizador = criar_novo_analisador()

    with st.echo():
        # 1. Texto de teste em inglês
        text_en = """Dear sports club coordination. My name is Jonh Smith and I live in the city of New York. I write this message to confirm my athlete profile. The annual registration fee was paid on July 17, 2026. My network address at the time of the access was 192.168.1.15 through the portal www.sportsclub.com."""
        
        # 2. O motor analisa o texto indicando o idioma correto
        results_en = analisador.analyze(text=text_en, language="en")
        
        # 3. Exibição do resultado
        plotar_texto_colorido(text_en, results_en)


def topico_5_3_1_email_base():
    analisador, anonimizador = criar_novo_analisador()

    with st.echo():
        text_email = """Assunto: Ficha de cadastro para exame admissional\n \nOlá equipe de recursos humanos. Escrevo para enviar as informações da ficha de saúde.\n\nO meu nome completo é Eduardo Pereira Silva. Eu moro na cidade de Curitiba.\nOs meus dados físicos para o registro são noventa quilos de peso e um metro e oitenta centímetros de altura.\nVocês podem falar comigo pelo número de celular (41) 98765 1234 ou pelo endereço carlos.pereira@exemplo.com.br.\nO documento vinculado ao contrato é o CPF 123.456.789 10. O cartão de crédito é 4095 2609 9393 4932.\n\nAtenciosamente, Eduardo."""
        
        results_email = analisador.analyze(text=text_email, language="pt")
        plotar_texto_colorido(text_email, results_email)


def topico_5_3_2_regex_cpf_cartao():
    analisador, anonimizador = criar_novo_analisador()

    with st.echo():
        from presidio_analyzer import Pattern, PatternRecognizer
        
        # Novo molde para o padrão do CPF
        molde_cpf_brasileiro = r"\d{3}\.\d{3}\.\d{3}\s?\d{2}"
        padrao_busca = Pattern(name="padrao_cpf", regex=molde_cpf_brasileiro, score=0.9)
        reconhecedor_cpf = PatternRecognizer(supported_entity="CPF", patterns=[padrao_busca], supported_language="pt")
        
        # Adição da regra no motor de análise
        analisador.registry.add_recognizer(reconhecedor_cpf)

        # Novo molde para o padrão do cartão de crédito
        molde_cartao = r"\d{4}\s\d{4}\s\d{4}\s\d{4}"
        padrao_cartao = Pattern(name="padrao_cartao", regex=molde_cartao, score=0.9)
        reconhecedor_cartao = PatternRecognizer(supported_entity="CREDIT_CARD", patterns=[padrao_cartao], supported_language="pt")
        
        # Adição da regra no motor de análise
        analisador.registry.add_recognizer(reconhecedor_cartao)

        # Texto de teste e avaliação
        text_email = """Assunto: Ficha de cadastro para exame admissional\n \nOlá equipe de recursos humanos. Escrevo para enviar as informações da ficha de saúde.\n\nO meu nome completo é Eduardo Pereira Silva. Eu moro na cidade de Curitiba.\nOs meus dados físicos para o registro são noventa quilos de peso e um metro e oitenta centímetros de altura.\nVocês podem falar comigo pelo número de celular (41) 98765 1234 ou pelo endereço carlos.pereira@exemplo.com.br.\nO documento vinculado ao contrato é o CPF 123.456.789 10. O cartão de crédito é 4095 2609 9393 4932.\n\nAtenciosamente, Eduardo."""
        resultados = analisador.analyze(text=text_email, language="pt")
        plotar_texto_colorido(text_email, resultados)


def topico_5_3_3_regex_telefone():
    analisador, anonimizador = criar_novo_analisador()
    from presidio_analyzer import Pattern, PatternRecognizer
    
    padrao_cpf = Pattern(name="padrao_cpf", regex=r"\d{3}\.\d{3}\.\d{3}\s?\d{2}", score=0.9)
    analisador.registry.add_recognizer(PatternRecognizer(supported_entity="CPF", patterns=[padrao_cpf], supported_language="pt"))
    padrao_cartao = Pattern(name="padrao_cartao", regex=r"\d{4}\s\d{4}\s\d{4}\s\d{4}", score=0.9)
    analisador.registry.add_recognizer(PatternRecognizer(supported_entity="CREDIT_CARD", patterns=[padrao_cartao], supported_language="pt"))

    with st.echo():
        from presidio_analyzer import Pattern, PatternRecognizer

        # Novo molde para o padrão de telefone no Brasil
        molde_telefone_brasileiro = r"\(?\d{2}\)?\s\d{5}\s\d{4}"
        padrao_telefone = Pattern(name="padrao_telefone", regex=molde_telefone_brasileiro, score=0.9)
        reconhecedor_telefone = PatternRecognizer(supported_entity="PHONE_NUMBER", patterns=[padrao_telefone], supported_language="pt")
        
        # Adição da regra no motor de análise
        analisador.registry.add_recognizer(reconhecedor_telefone)

        # Texto de teste e avaliação
        text_email = """Assunto: Ficha de cadastro para exame admissional\n \nOlá equipe de recursos humanos. Escrevo para enviar as informações da ficha de saúde.\n\nO meu nome completo é Eduardo Pereira Silva. Eu moro na cidade de Curitiba.\nOs meus dados físicos para o registro são noventa quilos de peso e um metro e oitenta centímetros de altura.\nVocês podem falar comigo pelo número de celular (41) 98765 1234 ou pelo endereço carlos.pereira@exemplo.com.br.\nO documento vinculado ao contrato é o CPF 123.456.789 10. O cartão de crédito é 4095 2609 9393 4932.\n\nAtenciosamente, Eduardo."""
        resultados = analisador.analyze(text=text_email, language="pt")
        plotar_texto_colorido(text_email, resultados)


def topico_5_3_4_falsos_positivos():
    analisador, anonimizador = criar_novo_analisador()
    from presidio_analyzer import Pattern, PatternRecognizer
    
    padrao_cartao = Pattern(name="padrao_cartao", regex=r"\d{4}\s\d{4}\s\d{4}\s\d{4}", score=0.9)
    analisador.registry.add_recognizer(PatternRecognizer(supported_entity="CREDIT_CARD", patterns=[padrao_cartao], supported_language="pt"))

    with st.echo():
        # Adicionamos um número de catraca semelhante a um cartão de crédito
        text_email = """Assunto: Ficha de cadastro para exame admissional \n\nOlá equipe de recursos humanos. Escrevo para enviar as informações da ficha de saúde.\n\nO meu nome completo é Eduardo Pereira Silva. Eu moro na cidade de Curitiba.\nOs meus dados físicos para o registro são noventa quilos de peso e um metro e oitenta centímetros de altura.\nVocês podem falar comigo pelo número de celular (41) 98765 1234 ou pelo endereço carlos.pereira@exemplo.com.br.\nO documento vinculado ao contrato é o CPF 123.456.789 10. O cartão de crédito é 4095 2609 9393 4932.\nO código de liberação da catraca do prédio é 1234 5678 9101 1121.\n\nAtenciosamente, Eduardo."""
        
        resultados = analisador.analyze(text=text_email, language="pt")
        plotar_texto_colorido(text_email, resultados)


def topico_5_4_csv():
    import pandas as pd
    from typing import List, Iterable, Optional
    from presidio_analyzer import BatchAnalyzerEngine, DictAnalyzerResult
    
    analisador_base, _ = criar_novo_analisador()

    with st.echo():
        # 1. Carregamento dos dados via CSV
        df_csv_data = pd.read_csv('https://raw.githubusercontent.com/OfAndreS/LectureOnTheLGPD/refs/heads/main/csv_data.csv')
        
        # 2. Construção da classe especializada para leitura de dados em lote (Batch)
        class CSVAnalyzer(BatchAnalyzerEngine):
            def analyze_csv(self, dados_dicionario: dict, language: str, keys_to_skip: Optional[List[str]] = None, **kwargs) -> Iterable[DictAnalyzerResult]:
                analyzer_results = self.analyze_dict(dados_dicionario, language, keys_to_skip)
                return list(analyzer_results)
        
        # 3. O motor recebe a inteligência base do aplicativo
        analyzer = CSVAnalyzer(analyzer_engine=analisador_base)
        
        # 4. Formatação e varredura da tabela
        dados_formatados = df_csv_data.to_dict(orient="list")
        analyzer_results = analyzer.analyze_csv(dados_formatados, language="en")
        
        # 5. Exibição da tabela colorida
        plotar_tabela_colorida(dados_formatados, analyzer_results)

@st.cache_data
def discovery_em_imagens():

    codigo_ex_0 = """
    !wget -qqq -O imagem.png "https://raw.githubusercontent.com/OfAndreS/LectureOnTheLGPD/main/pulmao_v2.png"
    """
    st.code(codigo_ex_0, language="bash")

    codigo_ex_1 = """
    import pydicom
    from PIL import Image
    import matplotlib.pyplot as plt
    from presidio_image_redactor import ImageAnalyzerEngine, ImagePiiVerifyEngine, DicomImagePiiVerifyEngine

    try:
        imagem = Image.open('imagem.png')
        plt.figure(figsize=(10, 6))
        plt.imshow(imagem)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        print("Verifique se o link de download está correto e aponta para o arquivo binário (raw).")

    image_analyzer_engine = ImageAnalyzerEngine()
    verify_engine = ImagePiiVerifyEngine()
    dicom_verify_engine = DicomImagePiiVerifyEngine()
    """
    st.code(codigo_ex_1, language="python")
    with st.container(border=True, horizontal_alignment="center"):
        st.image("../data/pulmao1.png", caption="Fonte: https://www.cancerimagingarchive.net/collection/pseudo-phi-dicom-data/")

    codigo_ex_2 = """
    verify_image = verify_engine.verify(imagem, display_image=True, show_text_annotation=True)
    verify_image
    """
    st.code(codigo_ex_2, language="python")
    with st.container(border=True, horizontal_alignment="center"):
        st.image("../data/pulmao2.png", caption="")

    codigo_ex_3 = """
    verify_image = verify_engine.verify(imagem, display_image=True, show_text_annotation=False)
    verify_image
    """
    st.code(codigo_ex_3, language="python")
    with st.container(border=True, horizontal_alignment="center"):
        st.image("../data/pulmao3.png", caption="")


@st.cache_data
def analyzer_engine():

    analisador, anonimizador = criar_novo_analisador()
    texto_exemplo = "My name is Jonh Lennon and my number is 11999998888"
    resultados = analisador.analyze(text=texto_exemplo,language="pt")

    codigo = """
    from presidio_analyzer import AnalyzerEngine

    motor_analise = AnalyzerEngine()

    texto_exemplo = "My name is Jonh Lennon and my number is 11999998888"

    resultados = motor_analise.analyze(
            text=texto_exemplo,
            language="pt"
    )

    print(resultados)
    """

    st.code(codigo, language="python")
    with st.container(border=True):
        st.write(resultados)


def pattern_recognizer():

    from presidio_analyzer import PatternRecognizer, Pattern

    analisador, anonimizador = criar_novo_analisador()

    molde_ticket = Pattern(
        name="regra_ticket_suporte",
        regex="TICKET-[0-9]{4}",
        score=0.9
    )
    
    # Adicionamos o idioma suportado para garantir que a regra funcione em português
    reconhecedor_customizado = PatternRecognizer(
        supported_entity="TICKET_ATENDIMENTO",
        patterns=[molde_ticket],
        supported_language="pt"
    )
    
    analisador.registry.add_recognizer(reconhecedor_customizado)

    texto_exemplo = "O cliente relatou uma falha de acesso no TICKET-4598 hoje de manhã."
    resultados = analisador.analyze(text=texto_exemplo, language="pt")

    codigo = """
    from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern

    motor_analise = AnalyzerEngine()

    molde_ticket = Pattern(
        name="regra_ticket_suporte",
        regex="TICKET-[0-9]{4}",
        score=0.9
    )

    # O parâmetro supported_language avisa o sistema em qual língua essa regra deve rodar
    reconhecedor_customizado = PatternRecognizer(
        supported_entity="TICKET_ATENDIMENTO",
        patterns=[molde_ticket],
        supported_language="pt"
    )

    motor_analise.registry.add_recognizer(reconhecedor_customizado)

    texto_exemplo = "O cliente relatou uma falha de acesso no TICKET-4598 hoje de manhã."
    resultados = motor_analise.analyze(text=texto_exemplo, language="pt")

    print(resultados)
    """

    st.code(codigo, language="python")
    with st.container(border=True):
        st.write(resultados)

def anonymizer_engine():
    from presidio_anonymizer.entities import OperatorConfig

    analisador, anonimizador = criar_novo_analisador()
    texto_exemplo = "Meu número de telefone é (11) 988675440."

    # Executa a análise inicial
    resultados = analisador.analyze(text=texto_exemplo, language="pt")

    # Aplica a máscara real nos bastidores usando um dicionário para os parâmetros
    configuracao_operadores = {
        "PHONE_NUMBER": OperatorConfig("mask", {"chars_to_mask": 9, "masking_char": "*", "from_end": True})
    }

    texto_seguro = anonimizador.anonymize(
        text=texto_exemplo,
        analyzer_results=resultados,
        operators=configuracao_operadores
    )

    codigo = """
    from presidio_analyzer import AnalyzerEngine
    from presidio_anonymizer import AnonymizerEngine
    from presidio_anonymizer.entities import OperatorConfig

    motor_analise = AnalyzerEngine()
    motor_anonimizacao = AnonymizerEngine()

    texto_exemplo = "Meu número de telefone é (11) 988675440."
    resultados = motor_analise.analyze(text=texto_exemplo, language="pt")

    # Os parâmetros da máscara devem ser passados como um dicionário
    configuracao_operadores = {
        "PHONE_NUMBER": OperatorConfig("mask", {"chars_to_mask": 4, "masking_char": "*", "from_end": True})
    }

    texto_seguro = motor_anonimizacao.anonymize(
        text=texto_exemplo,
        analyzer_results=resultados,
        operators=configuracao_operadores
    )

    print(texto_seguro.text)
    """

    st.code(codigo, language="python")
    with st.container(border=True):
        st.write(texto_seguro.text)
    