# Guia de estudo

Este guia acompanha os códigos e explica como cada solução atende ao enunciado. Os exemplos completos de saída estão em [RESULTADOS.md](RESULTADOS.md).

## Lista 1 - Listas

1. **Dashboard de vendas:** `sum(vendas)` produz o total de 9000. A média é esse total dividido pelos cinco dias, resultando em 1800. `max` encontra 3500 e `min` encontra 800.
2. **Gestão de estoque:** `append` adiciona a webcam ao final. `index` encontra o teclado, permitindo alterar seu nome. A expressão `"impressora" in estoque` retorna `False`. `remove` exclui o mouse.
3. **Organização de fretes:** `sort(reverse=True)` modifica a própria lista para a ordem `[150, 80, 50, 40, 20]`. O fatiamento `fretes[:2]` cria a lista `[150, 80]`.
4. **Rota de entregas:** `extend` acrescenta os elementos de `novas_cidades` à rota. Sorocaba está no índice 3. Como os índices começam em zero, sua posição na contagem é a quarta cidade.
5. **Atualização de preços:** as listas de nomes e preços representam os mesmos produtos nos mesmos índices. Depois de encontrar o índice do vinho, o programa troca apenas o preço correspondente. O tratamento de entradas evita procurar um nome inexistente ou converter um texto inválido para número.

## Lista 2 - Dicionários

1. **Cadastro de clientes:** `clientes["Alon"] += 1500` acumula a nova compra, em vez de substituir o faturamento por 1500. Alon passa a ter 4500, e a atribuição à chave Marcos adiciona o novo cliente com 2000.
2. **Consulta de estoque:** `strip().lower()` remove espaços externos e padroniza letras. A verificação `produto in estoque` evita acessar uma chave ausente. Um produto existente tem sua quantidade exibida.
3. **Faturamento por região:** `list(vendas_regiao.values())` cria uma lista com os quatro faturamentos. O total é 80000 e a média é 20000.
4. **Média de desempenho:** o acesso `desempenho["Paula"]` retorna `[10, 9, 10]`. A soma é 29 e a média é `29 / 3`, apresentada como 9.67 com duas casas decimais.
5. **Limpeza de produtos:** `pop("radio")` remove a chave e retorna seu valor, 200. A presença do celular é verificada com `in`, que retorna `True`.

## Lista 3 - Laços `for`

1. **Contagem regressiva:** `range(10, 0, -1)` gera dez valores: 10, 9, 8, 7, 6, 5, 4, 3, 2 e 1. O zero é o limite excluído. O programa apenas simula os lembretes no console.
2. **Comissão progressiva:** a taxa é escolhida para cada venda. As comissões são 100, 500, 50, 800 e 150; o acumulador chega a 1600. Uma venda de exatamente 4000 pertence à faixa de 5%.
3. **Estoque crítico:** o mesmo índice é usado nas duas listas. A condição é `quantidade < 8`, portanto somente monitor, com 5, e mouse, com 2, geram alertas. O headset tem exatamente 8 e não deve gerar alerta.
4. **Custos mensais:** cada gasto é comparado à meta do mesmo mês. Janeiro e março ficam dentro do orçamento. Fevereiro ultrapassa a meta em `1350 - 1200 = 150`. Igualar a meta ainda conta como estar dentro do orçamento.
5. **Reajuste de preços:** um percentual de 10 é convertido no fator `1 + 10 / 100 = 1.10`. A atualização altera os valores das chaves existentes. Depois, um segundo loop exibe o catálogo, com preços de 1650, 2750 e 5500 para um aumento de 10%.

## Lista 4 - Funções

1. **Padronização de texto:** `padronizar_texto` devolve `texto.strip().title()`. `strip` remove espaços das extremidades; `title` coloca as palavras em formato de título. Assim, `" aIrPoDs Pro"` vira `"Airpods Pro"`, seguindo a regra do exercício, sem preservar a grafia comercial da marca.
2. **Cálculo de ISS:** `calcular_iss` devolve apenas o imposto. Uma nota de 8000 usa 5%, produzindo 400. Uma nota de 2000 usa 3%, produzindo 60. Exatamente 5000 ainda usa 3%, porque a primeira condição exige um valor maior que 5000.
3. **Análise de margem:** o lucro é `faturamento - custo`; a margem é `lucro / faturamento`. Para 10000 e 6000, a margem é 0.40, ou 40%, e a classificação é `Margem Saudável`. Exatamente 30% também é saudável. Faturamento zero ou negativo é rejeitado, evitando uma divisão inválida ou sem sentido nesse contexto.
4. **Verificação de meta:** a função percorre `vendedores.items()` e imprime apenas quando o faturamento é maior ou igual à meta. João, Ricardo e Fernanda atendem à meta de 10000. Ricardo é incluído porque igualou a meta.
5. **Conversão de moeda:** `converter_para_real` multiplica um preço pela cotação. `processar_lista_precos` percorre a lista e chama essa função para cada preço. Com a cotação 5.20, os valores em reais são 520, 260 e 1300. A cotação é o dado do enunciado, sem consulta externa.

## Lista 5 - Tuplas

1. **Localização de entregas:** `latitude, longitude = coordenadas` desempacota os dois elementos da tupla nas variáveis correspondentes, na mesma ordem.
2. **Folha de pagamento:** `calcular_folha` retorna `desconto, salario_liquido`, formando uma tupla. Para 5000, os valores são 500 e 4500. A chamada desempacota os dois retornos.
3. **Vendas por unidade:** `for produto, preco_unitario, quantidade in vendas_dia` desempacota cada tupla diretamente no loop. A multiplicação do preço pela quantidade produz 1800 para Monitor, 750 para Teclado e 800 para Mouse.
4. **Vendas por filial:** `analisar_vendas` retorna total e média. A Matriz tem total de 45000 e média de 15000. A Filial Sul tem total de 12000 e média de 6000. Para uma lista vazia, foi adotado o retorno `(0, 0)` como proteção adicional.
5. **Chamados de suporte:** `len` fornece a quantidade, 5; `max` fornece o maior tempo, 120 minutos. A função retorna os dois valores, e o programa os desempacota para mostrar o resumo e o alerta. Para uma lista vazia, o retorno adotado é `(0, 0)`.

## Estrutura dos arquivos

Cada programa usa `main()` para agrupar sua execução. O bloco `if __name__ == "__main__":` chama essa função quando o arquivo é executado diretamente. Isso também permite importar as funções dos exercícios sem disparar os exemplos ou solicitar entradas ao usuário.
