# Teste Técnico - Data Science - Cognitivo.AI
> Previsão do preço de estadia pelo airbnb

A partir do dataset disponível em http://insideairbnb.com/get-the-data.html, foi realizada uma análise exploratória dos dados para identificar as variáveis que impactam no preço da estadia, bem como o desenvolvimento de um modelo preditivo baseado em machine learning para prever o preço da estadia.


## Getting started

Para utilização do código, é necessário realizar o download do arquivo lib.py e listings.csv.


## Como foi a definição da sua estratégia de modelagem?

A estratégia de modelagem foi baseada em algorítmos de machine learning.

Um aumento da capacidade computacional desde os anos 90 permitiu treinar grandes redes neurais em um período razoável de tempo.

Além disso, a alta capacidade das redes neurais de generalização (produzir
saídas adequadas para entradas que não estavam presentes durante o
treinamento do modelo) premite a resolução de problemas
de grande escala.


## Como foi definida a função de custo utilizada?


No treinamento desta rede neural, foi utilizado o algorítmo de backpropagation Adam.

A diferença entre a saída proporcionada pela rede neural e a saída real é calculada através de uma função de custo. Esta função informa o nível de precisão da rede neural em suas previsões para uma determinada entrada. O processo de calcular essa precisão (erro) é repetido diversas vezes até que a função de custo seja minimizada, ou seja, o erro seja minimizado. 

Geralmente ele é calculado através do método do gradiente descendente. O algorítmo Adam é baseado nele.

O principal desafio passa a ser como localizar o mínimo global e não "ficar preso" em mínimos locais. As redes neurais são boas em evitar mínimos locais e se aproximam ao máximo da melhor solução (metaheurísticas).


## Qual foi o critério utilizado na seleção do modelo final?


Os métodos empíricos e de pesquisa de grade (grid search) foram utilizados
para obter o conjunto apropriado de hiperparâmetros neste projeto. O grid
search é uma ferramenta que realiza uma busca exaustiva nos valores dos
parâmetros especificados para um estimador.

Uma prática comum adotada pelos cientistas de dados na escolha de número
de neurônios é formar camadas ocultas com cada vez menos neurônios, em
geral, aumentar o número de camadas é melhor do que aumentar o número de
neurônios por camadas. A abordagem adotada foi inicializar o processo de
treinamento com uma camada, até verificação de sobreajuste.


## Qual foi o critério utilizado para validação do modelo?

Mean Squared Error - MSE e Mean Absolute Error - MAE


## Por que escolheu utilizar este método?

Para avaliar o desempenho dos modelos, foi utilizado o MSE, por ser uma medida típica de desempenho para problemas de regressão. Ele dá uma ideia da quantidade de erros gerados pelo sistema em suas previsões, com um peso maior para grandes erros.

Uma vez que essa métrica eleva o erro ao quadrado, predições muito distantes do real aumentam o valor da medida muito facilmente, o que a torna uma métrica de avaliação excelente para problemas nos quais grandes erros não são tolerados.

Já o MAE, pelo fato de não elevar as diferenças ao quadrado, torna-se uma opção não tão ideal para lidar com problemas delicados. 
Contudo, é uma métrica sólida e indicada para preços além de sua interpretação ser mais intuitiva, com a mesma unidade dos valores trabalhados.

Por isso optou-se por analisar ambas as métricas.


## Quais evidências você possui de que seu modelo é suficientemente bom?

Embora todos os modelos tenham sido desenvolvidos com base nos critérios do MSE, para fazer um melhor julgamento sobre eles, o MAE também foi determinado. Um bom modelo deve ter valores MAE e MSE próximos de 0.

Para seleção do melhor modelo, o conjunto de dados foi testado 30 vezes utilizando validação cruzada com 10 folds (método dos 30 testes). 

Em cada um dos 30 testes, a semente geradora (parâmetro random state) variou de 1 a 30. Este parâmetro afeta a ordem dos índices e controla a aleatoriedade de cada
fold.

Em um futuro trabalho, seria importante aprimorar o modelo, fazer novas análises no banco de dados, e comparações com outros algorítmos. 


Os testes de Friedman e Nemenyi podem ser utilizados para provar estatisticamente que um algoritmo supera o outro.


## Links

- Repositório: https://github.com/karinassini/price_airbnb_prevision/



