# Sistema de Recomendação de Filmes
Neste projeto, construí meu próprio sistema de recomendação de filmes. O sistema foi feito a partir de dados sobre filmes coletados da base de dados do TMDB, através de sua API. O TMDB é uma vasta base de dados com informações sobre filmes, séries, curtas e animações. Lá é possível encontrar as mais diversas informações sobre os filmes, como elenco, orçamento, equipe de produção, atores, e um dos aspectos mais importantes para o projeto: notas de avaliação dos usuários. O projeto foi feito usando a linguagem python, mais especificamente os pacotes pandas, matplotlib, seabonr, requests e o pacote tmdbv3api para usar a API. 


### Coleta dos Dados
A fase de coleta de dados foi separada em dois momentos: Primeiro, baixei o dataset "TMDB Movies Metadata" no kaggle. Esse dataset agrupa de forma organizada a maior parte das informações necessárias para a construção do modelo. O único problema desse dataset é que ele contem informações sobre os filmes somente até o ano de 2017. Então comecei a segunda etapa da coleta, que foi listar os nomes filmes lançados em cada ano (2018 a 2022) para puxar o resto das informações necessárias via API do TMDB. Os dados coletados sobre os filmes foram os seguintes:

* budget: Orçamento do Filmes em Dólares
* genres: Lista de Dicionários com todos os gêneros associados ao filme
* homepage: Site oficial do filme
* id: Identificação (ID) do filme
* keywords: Palavras chaves associadas ao filme
* original_language: Idioma original do filme
* original_title: Título original do filme
* overview: Breve descrição do filme
* popularity: Pontuação dada pelo TMDB
* production_companies: Produtoras envolvidas na produção do filme
* release_data: Data de Lançamento do Filme
* revenue: Receita Total do filme em dólares
* runtime: Tempo de execução do filme em minutos
* spoken_language: Idiomas falados no filme
* status: Status do filme (lançado, para ser lançado, anunciado, etc)
* tagline: Tagline do filme
* title: Título oficial do filme
* vote_average: Avaliação média do filme	
* vote_count: Número de votos contabilizados pelo TMDB
* cast: Elenco do filme
* crew: Equipe Técnica


### Analisando os dados

Uma vez coletas os dados, parti para a análise exploratória. Comecei exploran do as estatísticas descritivas do modelo, e verificando quantos dados faltantes e duplicados haviam. Como n~çao foram encontrados muitos dados faltantes relevantes e os valores numéricos pareciam estar normais, segui a exploração. A tabela abaixo mostra a frequencia de dados faltantes para cada variável: Uma coluna totalmente cinza representa uma variável sem dados faltantes, ao passo que uma as linhas em branco representam os registros em falta.

![image](https://user-images.githubusercontent.com/77032413/183269174-06b80ec6-d664-4231-955d-0e226c57564b.png)
 
 Em seguida, foquei em investigar o estado de algumas das variáveis e fazer ajustes ede formatação para as colunas que seriam importantes para o sistema de recomendação. Essa etapa foi realizada usando as funções do pacote pandas para manipular os dados nas colunas. Também fiz uso de gráficos para investigar a disposição de algumas das varipaveis numéricas. O interessante dessa etapa eé que algumas alterações precisam ser feitas para visualizar os dados melhor. Por exemplo, no caso dos idiomas falados nos filmes: A maioria absoluta dos filmes da base de dados é em inglês, para observar melhor a proporção dos outros idiomas, foi necessário excluir o ingles do gráfico, como pode ser visto abaixo:

![image](https://user-images.githubusercontent.com/77032413/183269263-80c10ab2-537f-436b-885b-05af83884e07.png)

Para a composição do modelo, algumas variáveis são consideradas imprescindíveis. É o caso das sinopses dos filmes. Através das informações contidas nas sinopses disponibilizadas no site do TMDB é possível treinar o modelo para que ele compare a sinopse dos filmes e avalie sua similaridade para entregar as recomendações. O wordcloud abaixo foi feito a partir das informações extraidas de toda a amostra.

![image](https://user-images.githubusercontent.com/77032413/183269378-e73e36db-ffd0-49c2-b416-c9f127f59918.png)

Vale mencionar a variável "voto dos usuários". Apesar dessa variável não ser incluída na composição do modelo, é considerado um termômetro confiável da impressão do público a respeito de um filme. Como mostra o gráfico abaixo, a média de votos se concentra entre as notas 6 e 7.

![image](https://user-images.githubusercontent.com/77032413/183269431-4a769294-67f7-4b1d-a757-cdf92b63fc20.png)

Através da análise exploratória também foi possível conferir em quais meses ocorriam mais lançamentos de filmes. è interessante ver como o número de filmes lançados aumenta até setembro, e tem uma queda em novembro.

![image](https://user-images.githubusercontent.com/77032413/183269489-7866e9d7-399a-406b-9748-a9b060c1522d.png)

Uma vez que compreendemos um pouco melhor a natureza dos dados utilizados, é hora de partir para a implementação do sistema propriamente dito.

### Implementando o Sistema

##### Referências
- TMDB Movies metadata: https://www.kaggle.com/tmdb/tmdb-movie-metadata
