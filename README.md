# Bookscraper

Aplicação simples para coleta de dados do site [books.toscrape.com](https://books.toscrape.com), utilizando o framework [Scrapy](https://docs.scrapy.org/en/latest/) em Python. Ele permite extrair informações específicas de páginas web de forma eficiente e escalável.

## Ambiente Virtual

Comando para criação de um ambiente virtual python:

```bash
python -m venv venv
```

Comando para ativar ambiente virtual python:

```bash
source venv/bin/activate
```

## Comandos e configurações

Cria um projeto **Scrapy** no diretório `project_dir`. Se o diretório não for especificado, o diretório será igual ao nome do projeto.

```bash
scrapy startproject bookscraper [project_dir]
```

Cria um novo Spider na pasta atual ou na pasta spiders do projeto atual, se chamado de dentro de um projeto existente. O parâmetro `name` (**bookspider**) é definido como o nome do Spider, enquanto o `domain/URL` (**books.toscrape.com**) é usado para gerar os atributos do Spider `allowed_domains` e `start_urls`.

```bash
scrapy genspider bookspider books.toscrape.com
```

Instala [IPython](https://ipython.readthedocs.io/en/stable/) para interagir com os componentes da página via **Shell**.

```bash
pip install ipython
```

O IPython fornece uma arquitetura rica para computação interativa com:
- Um poderoso shell interativo.
- Um kernel para Jupyter.
- Suporte para visualização interativa de dados e uso de kits de ferramentas GUI.
- Intérpretes flexíveis e incorporáveis para carregar em seus próprios projetos.
- Ferramentas fáceis de usar e de alto desempenho para computação paralela.

Adiciona o parâmetro no arquivo `scrapy.cfg`.

```bash
[settings]
default = bookscraper.settings
shell = iphyton
```

O comando abaixo executa o shell interativo:

```bash
scrapy shell
```

Executa o spider criado:

```bash
bookscraper$: scrapy crawl bookspider
```

Executa o spider e insere o resultado em um arquivo CSV:

```bash
bookscraper$: scrapy crawl bookspider -O data.csv
```

Executa o spider e insere o resultado em um arquivo JSON:

```bash
bookscraper$: scrapy crawl bookspider -O data.json
```
