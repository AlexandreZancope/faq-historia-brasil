## 1. Aplicação escolhida e objetivos
Aplicação: Sistema de Perguntas e Respostas (FAQ) sobre um tema específico (exemplo: História do Brasil).
Objetivos principais:
1. Permitir que o usuário faça perguntas livres sobre História do Brasil.
2. O modelo LLM responde de forma clara, precisa e contextualizada.
3. Usar LangChain para gerenciar a lógica de interação, recuperação de contexto e controle da conversa.
4. Criar uma interface web simples e interativa com Streamlit.

## 2. Arquitetura do aplicativo
Componentes principais:
•	Streamlit: Interface web para o usuário inserir perguntas e visualizar respostas.
•	LLM (Large Language Model): Motor de geração de texto, usando OpenAI
•	LangChain: Framework para orquestrar o fluxo de perguntas e respostas, possibilitando adicionar cadeia de raciocínio, armazenamento de contexto, etc.
Fluxo resumido:
1.	Usuário digita pergunta no app Streamlit.
2.	LangChain recebe a pergunta, aplica lógica de prompt, possivelmente consulta uma base de conhecimento (ex: documentos, embeddings).
3.	LLM gera a resposta baseada no prompt montado.
4.	Resposta é exibida na interface Streamlit.

## 3. Código-fonte e instruções
Vou usar uma implementação simples para ilustrar, considerando uso de OpenAI via LangChain.
Os códigos utilizados estão no link do GitHub:
https://github.com/AlexandreZancope/faq-historia-brasil

## 4. Execução
streamlit run app.py