# Lista Extra 02 - Paradigmas de Programação com Python

Resolução dos 25 exercícios da Lista Extra 02, organizada em cinco grupos de acordo com o material da disciplina.

**Perfil:** [b1ellszx](https://github.com/b1ellszx)  
**Linguagem:** Python 3  
**Dependências:** apenas a biblioteca padrão do Python.

## Como executar

Baixe os arquivos em **Code > Download ZIP** e extraia a pasta, ou clone o repositório:

```bash
git clone https://github.com/b1ellszx/lista-extra-02-python.git
cd lista-extra-02-python
```

Abra um terminal nessa pasta e execute o exercício desejado:

```bash
python lista_1_listas/exercicio_01_dashboard_vendas.py
```

No Windows, se `python` não estiver disponível, use `py`. No Linux e no macOS, pode ser necessário usar `python3`.

Cada arquivo funciona de forma independente. Não é necessário instalar pacotes.

## Exercícios

### Lista 1 - Listas

| Exercício | Arquivo | Conceitos |
| --- | --- | --- |
| 1. Dashboard de vendas | [Abrir](lista_1_listas/exercicio_01_dashboard_vendas.py) | `sum`, `len`, `max` e `min` |
| 2. Gestão de estoque | [Abrir](lista_1_listas/exercicio_02_gestao_estoque.py) | `append`, `index`, `in` e `remove` |
| 3. Organização de fretes | [Abrir](lista_1_listas/exercicio_03_organizacao_fretes.py) | `sort(reverse=True)` e slicing |
| 4. Rota de entregas | [Abrir](lista_1_listas/exercicio_04_rota_entregas.py) | `extend`, índice e posição ordinal |
| 5. Atualização de preços | [Abrir](lista_1_listas/exercicio_05_atualizacao_precos.py) | `input`, listas correspondentes e atualização |

### Lista 2 - Dicionários

| Exercício | Arquivo | Conceitos |
| --- | --- | --- |
| 1. Cadastro de clientes | [Abrir](lista_2_dicionarios/exercicio_01_cadastro_clientes.py) | Atualização e inclusão de chaves |
| 2. Consulta de estoque | [Abrir](lista_2_dicionarios/exercicio_02_consulta_estoque.py) | Consulta, `in`, `strip` e `lower` |
| 3. Faturamento por região | [Abrir](lista_2_dicionarios/exercicio_03_faturamento_regioes.py) | `values`, conversão para lista, soma e média |
| 4. Média de desempenho | [Abrir](lista_2_dicionarios/exercicio_04_media_desempenho.py) | Lista como valor de um dicionário |
| 5. Limpeza de produtos | [Abrir](lista_2_dicionarios/exercicio_05_limpeza_produtos.py) | `pop` e consulta de chave |

### Lista 3 - Laços `for`

| Exercício | Arquivo | Conceitos |
| --- | --- | --- |
| 1. Contagem regressiva | [Abrir](lista_3_for/exercicio_01_contagem_regressiva.py) | `range(10, 0, -1)` |
| 2. Comissão progressiva | [Abrir](lista_3_for/exercicio_02_comissao_progressiva.py) | Condicional e acumulador |
| 3. Estoque crítico | [Abrir](lista_3_for/exercicio_03_estoque_critico.py) | Percurso de listas correspondentes |
| 4. Custos mensais | [Abrir](lista_3_for/exercicio_04_custos_mensais.py) | Comparação entre dicionários |
| 5. Reajuste de preços | [Abrir](lista_3_for/exercicio_05_reajuste_precos.py) | `input`, percentual e atualização em loop |

### Lista 4 - Funções

| Exercício | Arquivo | Conceitos |
| --- | --- | --- |
| 1. Padronização de texto | [Abrir](lista_4_funcoes/exercicio_01_padronizar_texto.py) | Parâmetro, retorno, `strip` e `title` |
| 2. Cálculo de ISS | [Abrir](lista_4_funcoes/exercicio_02_calcular_iss.py) | Retorno do imposto e condicional |
| 3. Análise de margem | [Abrir](lista_4_funcoes/exercicio_03_analisar_margem.py) | Lucro dividido pelo faturamento |
| 4. Verificação de meta | [Abrir](lista_4_funcoes/exercicio_04_quem_bateu_meta.py) | `for` dentro de uma função |
| 5. Conversão de moeda | [Abrir](lista_4_funcoes/exercicio_05_conversor_moeda.py) | Composição de funções |

### Lista 5 - Tuplas

| Exercício | Arquivo | Conceitos |
| --- | --- | --- |
| 1. Localização de entregas | [Abrir](lista_5_tuplas/exercicio_01_localizacao_entregas.py) | Unpacking de coordenadas |
| 2. Folha de pagamento | [Abrir](lista_5_tuplas/exercicio_02_calcular_folha.py) | Retorno de dois valores |
| 3. Vendas por unidade | [Abrir](lista_5_tuplas/exercicio_03_vendas_unidade.py) | Unpacking diretamente no `for` |
| 4. Vendas por filial | [Abrir](lista_5_tuplas/exercicio_04_analisar_vendas.py) | Retorno de total e média |
| 5. Chamados de suporte | [Abrir](lista_5_tuplas/exercicio_05_resumo_chamados.py) | Retorno de quantidade e máximo |

## Programas interativos

Três exercícios pedem dados ao usuário:

- **Lista 1, exercício 5:** nome do vinho e novo preço. Exemplo: `Tinto` e `275,50`.
- **Lista 2, exercício 2:** nome do produto. Exemplo: ` MONITOR `.
- **Lista 3, exercício 5:** percentual de aumento. Exemplo: `10` para 10%.

Os nomes digitados são tratados para desconsiderar maiúsculas e espaços nas extremidades. Os valores numéricos aceitam ponto ou vírgula decimal, sem separador de milhar. Preços e percentuais negativos ou entradas numéricas inválidas são rejeitados com uma mensagem.

O exercício de conversão de moeda utiliza a lista `[100, 50, 250]` e a cotação `5.20`, conforme o teste solicitado no enunciado.

## Resultados e explicações

- [Resultados de exemplo](RESULTADOS.md): saída de uma execução de cada um dos 25 programas, incluindo as entradas usadas nos interativos.
- [Guia de estudo](GUIA_DE_ESTUDO.md): explicações das operações e dos pontos que merecem atenção.

Os valores monetários são exibidos com duas casas decimais. Nos programas, o ponto é usado como separador decimal. As regras de ISS e de desconto salarial reproduzem exclusivamente os valores definidos no exercício.

## Referência

Material da disciplina: **Lista Extra 02 - Paradigmas de Programação com Python**, com oito páginas e cinco exercícios por grupo.
