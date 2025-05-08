# 📁 Web Scraper para Página de Produto – Take-Home Coding Challenge | Infosimples

Meu objetivo neste desafio foi desenvolver um scraper para uma página web simples. Mesmo sem experiência prévia em web scraping, utilizei os exemplos e tutoriais fornecidos para construir uma solução do zero, utilizando a linguagem Python.

O desafio abordou conceitos básicos de web scraping, e busquei aplicar o que aprendi com o material de estudo, trabalhando com chamadas HTTP, seletores CSS, manipulação de texto e geração de strings JSON, para completá-lo da melhor forma possível dentro do tempo disponível.

## 📝 Sobre o Projeto

Este projeto foi desenvolvido para o Take-Home Coding Challenge da Infosimples. Trata-se de um web scraper em Python que extrai informações específicas da página de produto `https://infosimples.com/vagas/desafio/commercia/product.html`, formatando os dados em um arquivo JSON (`produto.json`).

Para isso, utilizei as bibliotecas `requests` para realizar as chamadas HTTP e `beautifulsoup4` para manipular o HTML com seletores CSS. A formatação final dos dados foi feita com a biblioteca `json`.

## 🔵 Funcionalidades Implementadas

O scraper que desenvolvi é capaz de extrair as seguintes informações da página:

* **Título do Produto:** o nome principal do produto.
* **Marca:** a marca do produto.
* **Categorias:** as categorias às quais o produto pertence (extraídas do breadcrumb).
* **Descrição:** uma breve descrição do produto.
* **SKUs (Variações):** informações sobre as diferentes variações do produto, incluindo nome, preço atual, preço antigo (se disponível), disponibilidade e SKU.
* **Propriedades:** as propriedades listadas na seção "Additional properties" da página, no formato de "label": "value".
* **Reviews:** as avaliações dos clientes, incluindo nome do avaliador, data da avaliação, pontuação (estrelas) e o texto da avaliação.
* **Nota Média das Reviews:** a média das pontuações das avaliações.
* **URL da Página:** a URL da página do produto.

## 🟣 Como Executar

1.  **Pré-requisitos:**
    * Certifique-se de ter o Python 3 instalado no seu sistema.
    * Instale as bibliotecas necessárias `requests` e `beautifulsoup4` utilizando o pip:
        ```bash
        pip install requests beautifulsoup4
        ```
2.  **Execução:**
    * Após clonar este repositório (se aplicável), navegue até a pasta do projeto no seu terminal.
    * Execute o script Python principal (nome do arquivo: `scraper.py` ou outro nome que você tenha escolhido):
        ```bash
        python scraper.py
        ```
3.  **Resultado:**
    * Um arquivo chamado `produto.json` será gerado no mesmo diretório, contendo os dados extraídos da página no formato JSON especificado pelo desafio.

## 🔴 Dificuldades Encontradas: 

** Extração da seção "Product properties":**  
Durante o desenvolvimento, enfrentei dificuldades para extrair os dados da seção "Product properties" de forma consistente. As tentativas de seleção e interpretação da estrutura da tabela não retornaram os dados esperados. Para priorizar a entrega de um JSON funcional e respeitar o prazo, optei por remover temporariamente a extração dessa seção. Atualmente, o scraper coleta apenas os dados da seção "Additional properties".


**🟡 Considerações de Performance:** para este desafio, o scraper funciona bem para uma página. Mas se precisasse pegar informações de muitas páginas ou de sites muito grandes, talvez ele precisasse ser mais eficiente para não demorar muito.

## 🟢 Próximos Passos e Melhorias

* **Investigar a fundo a extração das "Product properties":** dedicar mais tempo analisando a estrutura do HTML dessa seção para identificar um seletor confiável e corrigir a lógica de extração.

## 🦇 Autor

**Evellyn Pereira Silva**

Agradeço a oportunidade de participar deste desafio da Infosimples. Como iniciante, este projeto representa uma etapa importante na minha jornada de aprendizado. Ele demonstra minha capacidade de aplicar novos conhecimentos para resolver problemas reais, utilizando chamadas HTTP, seletores CSS, manipulação de texto e formatação em JSON.
