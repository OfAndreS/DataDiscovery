import os
import streamlit as st
import topico_04 as t04
import topico_05 as t05

# ==========================================
# Funções Auxiliares de Interface
# ==========================================
# Essas funções evitam a repetição de código HTML e formatação ao longo do arquivo.

def obter_caminho_imagem(nome_arquivo):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(diretorio_atual, "..", "data", nome_arquivo)

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
            st.image(obter_caminho_imagem("DataDiscovery.png"), caption="")

            # Tópico 01
            renderizar_titulo_principal("01 ) - Implementação ideal do Data Discovery")
            for i in range(5): st.write("")
            st.image(obter_caminho_imagem("Mermaid.png"), caption="")

            # Tópico 02
            renderizar_titulo_principal("02 ) - Considerações na escolha da ferramenta")
            st.image(obter_caminho_imagem("02-AmplitudeDaCorbetura.png"), caption="")
            st.image(obter_caminho_imagem("03-PrecisaoDaClassificacao.png"), caption="")
            st.image(obter_caminho_imagem("04-VisibilidadeDeAcesso.png"), caption="")
            st.image(obter_caminho_imagem("05-CapacidadeDeCorrecao.png"), caption="")
            st.image(obter_caminho_imagem("06-AlinhamentoDeConformidade.png"), caption="")

            # Tópico 03
            renderizar_titulo_principal("03 ) - Tipos de ferramentas")
            st.image(obter_caminho_imagem("07-FerramentasCorporativas.png"), caption="")
            st.image(obter_caminho_imagem("DashBoard.png"), caption="")
            st.image(obter_caminho_imagem("11-FerramentasOpenSource.png"), caption="")

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

            st.image(obter_caminho_imagem("MicrosoftPresidio.png"), caption="")

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
            st.image(obter_caminho_imagem("F2ScoresForVariusModels.png"), caption="Fonte: https://www.youtube.com/watch?v=1pUEG0MZxvM&t=726s")
            st.image(obter_caminho_imagem("TrainingAndInferenceTime.png"), caption="Fonte: https://www.youtube.com/watch?v=1pUEG0MZxvM&t=726s")

            renderizar_subtitulo("5.6 ) Aplicando o data discovery em imagens")
            renderizar_paragrafo('parte das informações sensíveis de uma organização está oculta em formatos não estruturados, como documentos digitalizados, recibos, fotos de identificação e exames médicos (DICOM). Sem ferramentas eficazes de OCR e análise contextual para "ler" o texto dentro dessas imagens, esses dados permanecem invisíveis à governança, criando pontos cegos críticos que impedem a conformidade com leis de privacidade (como a LGPD) e aumentam drasticamente o risco de vazamentos acidentais de informações pessoalmente identificáveis (PII).')
            t05.discovery_em_imagens()

            # Tópico 06
            renderizar_titulo_principal("06 ) - Técnicas de tratamento e anonimização")
            st.image(obter_caminho_imagem("9-DataAnonymization.png"), caption="")
            st.image(obter_caminho_imagem("10-CensuraDireta.png"), caption="")
            st.image(obter_caminho_imagem("11-MascaramentoParcial.png"), caption="")
            st.image(obter_caminho_imagem("12-CriptografiaIrreversivel.png"), caption="")
            st.image(obter_caminho_imagem("13-Pseudonimizacao.png"), caption="")

            # Tópico 07
            renderizar_titulo_principal("07 ) - Casos de aplicação no mercado")

            renderizar_subtitulo("7.1 ) Mascaramento dinâmico em consultas SQL")
            
            texto_explicativo = "O usuário entra no sistema com uma credencial de acesso. A plataforma recebe o pedido e executa a busca no banco de dados. O computador avalia o nível de permissão do funcionário antes de entregar o resultado. A máquina exibe os dados reais se a credencial for de alto nível. O sistema aciona a ferramenta de anonimização e mascara os campos sensíveis se a permissão for restrita. Essa técnica protege a privacidade sem impedir o trabalho das equipes de apoio."
            renderizar_paragrafo(texto_explicativo)
            
            # Construção do diagrama visual usando a linguagem Mermaid
            diagrama_fluxo = """
            ```mermaid
            graph TD
                A[Funcionário acessa o portal] --> B[Sistema executa a busca SQL]
                B --> C{Validação de Credencial}
                C -->|Acesso Direto| D[Exibe dados originais na tabela]
                C -->|Acesso Restrito| E[Motor de Anonimização intercepta o texto]
                E --> F[Exibe dados mascarados na tabela]
                
                style A fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px,color:#334155
                style B fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px,color:#334155
                style C fill:#e0f2fe,stroke:#94a3b8,stroke-width:2px,color:#0f172a
                style D fill:#dcfce7,stroke:#86efac,stroke-width:2px,color:#166534
                style E fill:#fef08a,stroke:#fde047,stroke-width:2px,color:#854d0e
                style F fill:#fee2e2,stroke:#fca5a5,stroke-width:2px,color:#991b1b
            ```
            """
            
            # O Streamlit renderiza o diagrama automaticamente dentro de um container
            with st.container(border=True):
                st.markdown(diagrama_fluxo)

            renderizar_subtitulo("7.2 ) Proteção de dados no uso de Inteligência Artificial")
            
            texto_llm = "A popularidade dos modelos de linguagem criou um risco novo. Os funcionários costumam colar textos com informações de clientes dentro de ferramentas como o ChatGPT. A empresa pode configurar o sistema de varredura para atuar como um filtro de segurança. O pipeline lê a mensagem do usuário e oculta os nomes e documentos antes de enviar a pergunta para a nuvem. O robô responde a dúvida normalmente. O sistema interno recebe a resposta e devolve os dados originais para a tela do funcionário. A inteligência artificial externa nunca chega a ver o dado real."
            renderizar_paragrafo(texto_llm)

            diagrama_llm = """
            ```mermaid
            graph TD
                A[Texto do Usuário] --> B[Motor de Anonimização]
                B -->|Texto Mascarado| C((API do ChatGPT))
                C -->|Resposta Mascarada| D[Motor de Restauração]
                D -->|Resposta Original| E[Tela do Usuário]
                
                style A fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px
                style B fill:#fef08a,stroke:#fde047,stroke-width:2px
                style C fill:#e0f2fe,stroke:#94a3b8,stroke-width:2px
                style D fill:#dcfce7,stroke:#86efac,stroke-width:2px
                style E fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px
            ```
            """
            with st.container(border=True):
                st.markdown(diagrama_llm)


            renderizar_subtitulo("7.3 ) Limpeza de dados para equipes de análise")
            
            texto_datalake = "As empresas guardam oceanos de informações nos chamados Data Lakes. Esse termo representa um grande armazém central de arquivos brutos. Os cientistas de dados precisam acessar esse armazém para criar gráficos e encontrar oportunidades de negócio. Eles precisam saber a idade e os hábitos de consumo dos clientes para gerar relatórios. Eles não precisam saber o nome ou o endereço exato dessas pessoas. O pipeline atua na porta de entrada desse armazém. O computador substitui os dados diretos por códigos falsos. A equipe de análise consegue trabalhar com os números totais sem violar a privacidade de ninguém."
            renderizar_paragrafo(texto_datalake)

            diagrama_datalake = """
            ```mermaid
            graph TD
                A[(Bancos de Dados Originais)] --> B[Pipeline de Data Discovery]
                B --> C{Motor de Anonimização}
                C --> D[(Data Lake Seguro)]
                D --> E[Cientista de Dados]
                D --> F[Painel de Gráficos]
                
                style A fill:#fee2e2,stroke:#fca5a5,stroke-width:2px
                style B fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px
                style C fill:#fef08a,stroke:#fde047,stroke-width:2px
                style D fill:#dcfce7,stroke:#86efac,stroke-width:2px
            ```
            """
            with st.container(border=True):
                st.markdown(diagrama_datalake)


            renderizar_subtitulo("7.4 ) Higienização de arquivos de registro de sistema")
            
            texto_logs = "Todo programa de computador gera um arquivo de texto para anotar o que acontece no dia a dia. Esse arquivo de registro recebe o nome de log. O problema acontece quando o sistema anota acidentalmente uma senha ou um número de cartão de crédito que o cliente digitou errado. O motor de anonimização funciona como um vigia antes da gravação do arquivo. A ferramenta lê o texto do erro e troca os dados sensíveis por asteriscos. Isso impede que os desenvolvedores tenham acesso a informações perigosas quando forem consertar uma falha no sistema."
            renderizar_paragrafo(texto_logs)

            diagrama_logs = """
            ```mermaid
            graph TD
                A[Erro no Aplicativo] --> B[Geração do Texto de Log]
                B --> C[Motor de Anonimização]
                C --> D[Servidor de Armazenamento]
                D --> E[Equipe de Programação]
                
                style A fill:#fee2e2,stroke:#fca5a5,stroke-width:2px
                style B fill:#f8fafc,stroke:#e2e8f0,stroke-width:2px
                style C fill:#fef08a,stroke:#fde047,stroke-width:2px
                style D fill:#dcfce7,stroke:#86efac,stroke-width:2px
            ```
            """
            with st.container(border=True):
                st.markdown(diagrama_logs)