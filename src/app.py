import streamlit as st
import topico_04 as t04
import topico_05 as t05

# ==========================================
# Funções Auxiliares de Interface
# ==========================================
# Essas funções evitam a repetição de código HTML e formatação ao longo do arquivo.

def renderizar_titulo_principal(texto_titulo):
    linha_grossa = "<hr style='border: 2.5px solid #2B2B2B;'>"
    st.markdown(linha_grossa, unsafe_allow_html=True)
    st.markdown(f"# **| {texto_titulo}**")
    st.markdown(linha_grossa, unsafe_allow_html=True)

def renderizar_subtitulo(texto_subtitulo, espacos=5):
    for i in range(espacos): 
        st.write("")
    st.markdown(f"## **{texto_subtitulo}**")

def renderizar_paragrafo(texto):
    texto_formatado = f"<p style='font-size: 25px;' align='justify'>{texto}</p>"
    st.markdown(texto_formatado, unsafe_allow_html=True)


# ==========================================
# Início do Aplicativo
# ==========================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="Data Discovery", 
        page_icon="📊",
        layout="wide"
    )
  
    # Aplicação da fonte customizada do projeto
    estilos_customizados = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
    }
    </style>
    """
    st.markdown(estilos_customizados, unsafe_allow_html=True)

    # Divisão da tela para centralizar o conteúdo
    coluna_esquerda, coluna_central, coluna_direita = st.columns([1, 7, 1])

    with coluna_central:
        with st.container(border=False, horizontal_alignment="center"):
            
            # Slide inicial
            st.image("../data/DataDiscovery.png", caption="")

            # Tópico 01
            renderizar_titulo_principal("01 ) - Implementação ideal do Data Discovery")
            for i in range(5): st.write("")
            st.image("../data/Mermaid.png", caption="")

            # Tópico 02
            renderizar_titulo_principal("02 ) - Considerações na escolha da ferramenta")
            st.image("../data/02-AmplitudeDaCorbetura.png", caption="")
            st.image("../data/03-PrecisaoDaClassificacao.png", caption="")
            st.image("../data/04-VisibilidadeDeAcesso.png", caption="")
            st.image("../data/05-CapacidadeDeCorrecao.png", caption="")
            st.image("../data/06-AlinhamentoDeConformidade.png", caption="")

            # Tópico 03
            renderizar_titulo_principal("03 ) - Tipos de ferramentas")
            st.image("../data/07-FerramentasCorporativas.png", caption="")
            st.image("../data/DashBoard.png", caption="")
            st.image("../data/11-FerramentasOpenSource.png", caption="")

            # Tópico 04
            renderizar_titulo_principal("04 ) - Métodos utilizados")

            renderizar_subtitulo("4.1 ) Denylists")
            renderizar_paragrafo("Essa abordagem usa listas de palavras bloqueadas. O sistema guarda termos que precisam de censura direta. O computador apenas compara o texto com os itens salvos nessa lista. As empresas aplicam isso para proteger nomes de projetos e marcas.")
            t04.topico_4_1_denylists()

            renderizar_subtitulo("4.2 ) Regex")
            renderizar_paragrafo("Uma expressão regular ou regex funciona como um molde de texto. O programador cria uma regra e a máquina procura esse padrão exato. A técnica é muito útil para encontrar endereços de email e números de telefone.")
            t04.topico_4_2_regex()

            renderizar_subtitulo("4.3 ) Named Entity Recognition")
            renderizar_paragrafo("Esse método usa inteligência artificial para reconhecer entidades nomeadas e atende pela sigla NER. Esses modelos leem a mensagem inteira para entender o contexto da informação. O algoritmo percebe a diferença entre o nome de uma pessoa e um objeto comum analisando a frase completa.")
            t04.topico_4_3_ner()

            renderizar_subtitulo("4.4 ) Checksum")
            renderizar_paragrafo("Esse método foca na validação matemática. A tecnologia não confia apenas no formato dos números. O algoritmo faz um cálculo rápido para comprovar se um documento ou cartão de crédito é verdadeiro. A máquina descarta a informação na hora se o resultado da conta falhar.")
            t04.topico_4_4_checksum()

            renderizar_subtitulo("4.5 ) Context Words")
            renderizar_paragrafo("Esse método atua como um apoio focado no ambiente ao redor do dado. A ferramenta mapeia as palavras que aparecem perto da informação suspeita. O computador classifica o dado mais facilmente quando encontra a palavra senha escrita antes de uma sequência numérica.")
            t04.topico_4_5_context_words()


            # Tópico 05
            renderizar_titulo_principal("05 ) - Aplicação do Microsoft Presidio")

            st.image("../data/MicrosoftPresidio.png", caption="")

            renderizar_subtitulo("5.1.1 ) Tipos suportados")
            renderizar_paragrafo("O sistema reconhece diversas categorias de informações sensíveis por padrão. A tabela abaixo lista os tipos padrões de entidades que a ferramenta consegue identificar e classificar durante a leitura dos textos.")
            t05.topico_5_0_tabela_entidades()

            renderizar_subtitulo("5.1.2 ) AnalyzerEngine")
            renderizar_paragrafo("Esse componente funciona como o inspetor do sistema. A função dele é ler o texto original e procurar informações confidenciais usando as técnicas que estudamos anteriormente. O resultado gerado é um mapa indicando a posição exata de cada palavra sensível.")
            t05.analyzer_engine()

            renderizar_subtitulo("5.1.2 ) PatternRecognizer")
            renderizar_paragrafo("A biblioteca original já reconhece várias entidades globais de forma automática. O desenvolvedor utiliza essa função específica para ensinar o sistema a encontrar formatos novos que existem apenas dentro da rotina da empresa.")
            t05.pattern_recognizer()

            renderizar_subtitulo("5.1.3 ) AnonymizerEngine")
            renderizar_paragrafo("Esse componente é o responsável pela edição final do arquivo. O sistema recebe as posições encontradas pelo motor de análise e aplica as técnicas de ocultação escolhidas pelo programador.")
            t05.anonymizer_engine()

            renderizar_subtitulo("5.2.1 ) Texto em português")
            renderizar_paragrafo("Este exemplo prático aplica a nossa função de pintura sobre um texto em português. O objetivo é observar o comportamento da ferramenta identificando múltiplas entidades como nomes e locais de uma só vez.")
            t05.topico_5_1_1()

            renderizar_subtitulo("5.2.2 ) Texto em inglês")
            t05.topico_5_1_2_texto_en()

            renderizar_subtitulo("5.3.1 ) Análise base sem regras customizadas")
            renderizar_paragrafo("Em canais de suporte por e-mail os clientes costumam enviar dados pessoais para agilizar o atendimento. A varredura contínua identifica esses dados automaticamente. A ferramenta localiza números que seguem padrões de documentos e telefones. Essa prática permite que a empresa aplique regras de descarte da informação após a resolução do chamado.")
            t05.topico_5_3_1_email_base()

            renderizar_subtitulo("5.3.2 ) Adição do regex: CPF + Cartão de crédito")
            t05.topico_5_3_2_regex_cpf_cartao()

            renderizar_subtitulo("5.3.3 ) Adição do regex: Telefone")
            t05.topico_5_3_3_regex_telefone()

            renderizar_subtitulo("5.3.4 ) Riscos de falsos positivos")
            renderizar_paragrafo("A adição de regras visuais exige cuidado. O sistema pode confundir sequências numéricas comuns com dados confidenciais se o molde for muito simples. No exemplo abaixo o computador bloqueou o código da catraca acreditando ser um cartão de crédito.")
            t05.topico_5_3_4_falsos_positivos()

            renderizar_subtitulo("5.4 ) Aplicando o data discovery em tabelas CSV's")
            renderizar_paragrafo("Imagine uma empresa que exporta relatórios mensais de salários em formato CSV para auditoria. O Data Discovery automatizado garante que colunas contendo dados sensíveis, como CPF ou conta bancária, sejam identificadas antes do envio, evitando que informações financeiras circulem sem o devido controle de acesso ou criptografia.")
            t05.topico_5_4_csv()

            renderizar_subtitulo("5.5 ) Outras combinações de modelos")
            renderizar_paragrafo("A escolha ideal varia conforme a necessidade do projeto. Muitas vezes é necessário aceitar uma leve perda de exatidão para que o programa rode mais rápido.")
            st.image("../data/F2ScoresForVariusModels.png", caption="Fonte: https://www.youtube.com/watch?v=1pUEG0MZxvM&t=726s")
            st.image("../data/TrainingAndInferenceTime.png", caption="Fonte: https://www.youtube.com/watch?v=1pUEG0MZxvM&t=726s")

            renderizar_subtitulo("5.6 ) Aplicando o data discovery em imagens")
            renderizar_paragrafo('parte das informações sensíveis de uma organização está oculta em formatos não estruturados, como documentos digitalizados, recibos, fotos de identificação e exames médicos (DICOM). Sem ferramentas eficazes de OCR e análise contextual para "ler" o texto dentro dessas imagens, esses dados permanecem invisíveis à governança, criando pontos cegos críticos que impedem a conformidade com leis de privacidade (como a LGPD) e aumentam drasticamente o risco de vazamentos acidentais de informações pessoalmente identificáveis (PII).')
            t05.discovery_em_imagens()

            # Tópico 06
            renderizar_titulo_principal("06 ) - Técnicas de tratamento e anonimização")
            st.image("../data/9-DataAnonymization.png", caption="")
            st.image("../data/10-CensuraDireta.png", caption="")
            st.image("../data/11-MascaramentoParcial.png", caption="")
            st.image("../data/12-CriptografiaIrreversivel.png", caption="")
            st.image("../data/13-Pseudonimizacao.png", caption="")