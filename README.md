# Projeto de Estatística Aplicada

## 🧑‍💻 Autores  
- Cássio José (202411250010) - cassio.mandu@academico.ifpb.edu.br


## 🎯 Tema e Motivação  
  O nosso projeto irá investigar as correlações entre os hábitos de jogo e o desempenho acadêmico dos estudantes. A pesquisa também considerará fatores socioeconômicos e o nível de escolaridade dos pais, buscando entender como esses elementos influenciam no rendimento escolar e nos comportamentos relacionados aos jogos. Através dessa análise, pretendemos identificar padrões que possam contribuir para uma melhor compreensão do impacto dos jogos eletrônicos na vida estudantil.
  
  O motivo da escolha desse projeto é que, nos últimos anos, os jogos têm se tornado cada vez mais presentes na rotina dos jovens. Por isso, consideramos importante estudar esse crescimento e entender suas possíveis consequências, especialmente no contexto educacional. A tendência é que essa presença continue aumentando no futuro, o que torna a análise ainda mais relevante do ponto de vista social e estatístico.

## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**  
  Game and Students

- **Fonte:**  
  https://www.kaggle.com/datasets/willianoliveiragibin/games-and-students/data

- **Descrição breve:**  
  Este conjunto de dados reúne informações sobre estudantes, com foco em seus hábitos de jogo, desempenho acadêmico e contexto socioeconômico. Inclui variáveis como gênero, escola, frequência e duração dos jogos, nota escolar, renda familiar e escolaridade dos pais. Embora o escopo temporal e geográfico não seja especificado, os dados permitem comparações entre escolas e perfis de alunos. Ele foi escolhido por possibilitar análises sobre a relação entre jogos eletrônicos, desempenho escolar e fatores familiares.

- **Justificativa para a escolha:**  
 Este conjunto de dados permite análises estatísticas interessantes por reunir variáveis quantitativas e qualitativas que se relacionam diretamente com o comportamento e o desempenho dos estudantes. A presença de informações sobre hábitos de jogo, desempenho escolar, renda familiar e escolaridade dos pais possibilita explorar correlações, testar hipóteses e identificar padrões.

---

## ❓ Perguntas ou Hipóteses  
Estudantes que não jogam têm melhor desempenho acadêmico?

Há diferenças nos hábitos de jogo entre escolas diferentes?

Os estudantes com mais anos de experiência em jogos também jogam mais horas por dia?

## 🔍 Metodologia  
A metodologia utilizada neste trabalho baseou-se em análise exploratória de dados.

Técnicas estastísticas aplicadas:

1 - Agrupamento de dados:

  Para agrupar os participantes de acordo com a variável “Playing Years”, criando categorias (0, 1, 2, 3+ anos de     
  experiência jogando).
  Isso permitiu analisar tendências de comportamento em relação ao tempo de experiência.
  
2 - Estatísticas descritivas:

  Média, mediana, desvio padrão, valor mínimo e máximo foram calculados para a variável “Playing Hours” em cada grupo 
  de anos jogando.
  Objetivo: descrever a distribuição das horas jogadas por semana em cada nível de experiência.
  
3 - Distribuição de frequência absoluta e relativa:

  Utilizada para encontrar os níveis mais frequentes de escolaridade dos pais (pai e mãe) entre os estudantes que 
  jogam.
  A frequência relativa (%) ajudou a interpretar a representatividade de cada nível de escolaridade dentro do grupo de 
  jogadores.
  
4 - Visualização de dados(gráficos):

  Gráficos de barras foram usados para apoiar visualmente as análises, tornando os padrões e comparações mais   
  evidentes.
## 🛠️ Ferramentas Utilizadas  
Este projeto foi realizado com o uso de ferramentas e bibliotecas da linguagem Python, focadas em análise de dados e visualização:

Principais bibliotecas utilizadas:

1 - pandas:

  Para carregamento, tratamento e análise de dados tabulares.
  
  Utilizada para:

    - Leitura do arquivo CSV com os dados.
    
    - Agrupamentos (groupby).
    
    - Cálculo de estatísticas descritivas.
    
    - Contagem de frequências.
    
    - Formatação de tabelas.

2 - matplotlib.pyplot

  Para construção de gráficos de barras.

  Usada para representar visualmente:

    - A média de horas jogadas por anos de experiência.
    
    - As frequências das escolaridades dos pais.

Formato dos dados:

  Arquivo CSV (Comma-Separated Values)

    - Arquivo: gameandgrade new.csv
    
    - Estrutura: contém colunas como "Playing Games", "Playing Hours", "Playing Years", "Father Education", "Mother   
    Education", entre outras
Ambiente de execução:

  Código executado em ambiente local (no computador do usuário).
  
    Exemplo de caminho do arquivo: c:\Users\cassi\Downloads\gameandgrade new.csv

## 📈 Resultados  
 Resumo dos Resultados – Visual e Interpretativo
 
1. Horas jogadas por semana vs. anos de experiência

Achado estatístico:

| Anos Jogando | Média (h/sem) | Mediana | Desvio Padrão | Mínimo | Máximo |
| ------------ | ------------- | ------- | ------------- | ------ | ------ |
| 0 anos       | 0.00          | 0.0     | 0.00          | 0      | 0      |
| 1 ano        | 1.54          | 1.0     | 0.76          | 1      | 5      |
| 2 anos       | 2.02          | 2.0     | 0.87          | 1      | 5      |
| 3 anos ou +  | 2.68          | 3.0     | 1.22          | 1      | 5      |

Interpretação:

  * Quanto mais tempo a pessoa joga, maior tende a ser o número médio de horas jogadas por semana.
  
  * A evolução da mediana e do desvio padrão também sugere maior envolvimento e diversidade de hábitos de jogo com 
  o passar dos anos.
  
  * Jogadores com 3 anos ou mais jogam em média quase 3 horas por semana, enquanto os novatos (1 ano) ficam em 
  cerca de 1,5 hora.

2. Escolaridade dos pais entre estudantes que jogam
   
      Pai – Top 3 Escolaridades:
    | Pai | Absoluto | Relativo (%) |
    | --- | -------- | ------------ |
    | 4   | 183      | 33.76%       |
    | 3   | 120      | 22.14%       |
    | 5   | 109      | 20.11%       |
    
     Mãe – Top 3 Escolaridades:
    | Mãe | Absoluto | Relativo (%) |
    | --- | -------- | ------------ |
    | 4   | 171      | 31.55%       |
    | 3   | 148      | 27.31%       |
    | 2   | 110      | 20.30%       |

  Interpretação:
  
* A escolaridade nível 4 é a mais comum tanto para mães quanto para pais entre estudantes que jogam.

* Isso pode indicar que estudantes que têm pais com escolaridade média-alta são mais propensos a jogar — ou que há uma concentração geral dessa faixa de escolaridade no conjunto de dados.

* Pode refletir fatores socioeconômicos que influenciam o acesso a jogos digitais, como renda familiar e acesso à tecnologia.



## 📌 Conclusões  

1. Aprendizado: Experiência e Engajamento Crescentes:

* O que vimos: Quanto mais anos de prática (0 → 1 → 2 → 3+), maior a média de horas jogadas por semana, passando de ~0 h para cerca de 2,7 h.

* Implicação: Programas ou conteúdos para iniciantes devem focar em retenção até a primeira marca de 1 ano — já aí o engajamento salta de 0 para ~1,5 h/sem. Para jogadores veteranos, ofereça variedade (novos desafios, modos de jogo) para acomodar perfis muito ativos e moderadamente ativos.

2. Aprendizado: Perfil Socioeducacional dos Pais:
   
* O que vimos: Os níveis de escolaridade mais frequentes entre pais e mães de gamers são os intermediários (nível 4 principalmente, seguido de 3 e 5 para pai; 3 e 2 para mãe).

* Implicação: Estratégias de comunicação com famílias podem se beneficiar de mensagens que considerem um background médio-alto de escolaridade. Além disso, pode haver barreiras de acesso em famílias com escolaridade muito baixa, sinalizando necessidade de políticas de inclusão digital (ex.: empréstimo de equipamentos, oficinas de tecnologia).

3. Aprendizado: Variabilidade dentro dos Grupos:

* O que vimos: O desvio-padrão das horas jogadas cresce com a experiência — veteranos têm hábitos de jogo mais heterogêneos (alguns jogam muito, outros pouco).

* Implicação: Não há “um só tipo” de jogador veterano. Campanhas de engajamento devem ser segmentadas: por exemplo, ofertas de pacotes de horas intensivas para “hardcore gamers” vs. eventos ocasionais para jogadores casuais.

## ⚠️ Limitações e Trabalhos Futuros  

Limitações e Trabalhos Futuros: 

A análise efetuada neste estudo possui algumas limitações importantes que devem ser consideradas. Em primeiro lugar, o conjunto de dados é limitado a um único arquivo CSV, provavelmente com um número restrito de participantes e proveniente de um único contexto (escola, região, etc.), o que compromete a representatividade da amostra. Como apontam as referências, resultados obtidos em amostras muito restritas dificilmente podem ser generalizados para populações mais amplas.

* Além disso, o estudo utilizou apenas estatísticas descritivas (médias, desvios, gráficos de barras, etc.) sem empregar testes estatísticos inferenciais. Estatísticas descritivas caracterizam apenas a amostra em questão e não permitem inferências sobre outras populações.

* Em outras palavras, sem testes de hipótese, correlações ou modelos preditivos, não é possível confirmar se as relações observadas (por exemplo, entre horas de jogo e nota) seriam estatisticamente significativas em um universo maior. Outro fator limitante é o caráter transversal do estudo: todas as informações foram coletadas em um único momento temporal. Como ressaltado em estudos metodológicos, desenhos transversais não permitem estabelecer relações de causa e efeito nem acompanhar mudanças ao longo do tempo.

* Por fim, o conjunto de variáveis utilizado foi bastante reduzido – focando apenas em horas/jogos jogados, anos de experiência e escolaridade dos pais – e deixou de fora fatores potencialmente relevantes (motivação para jogar, tipo de jogo, qualidade do sono, apoio dos colegas/professores, entre outros). Essa ausência de variáveis complementares dificulta compreender aspectos qualitativos e contextuais que podem influenciar o desempenho acadêmico. Em vista dessas limitações, diversos trabalhos futuros podem ser conduzidos para ampliar e aprofundar os resultados. Uma primeira sugestão é incluir novas variáveis que capturem melhor o contexto dos alunos: por exemplo, medir a motivação ou satisfação dos estudantes com os jogos, distinguir gêneros de jogos (educativos, competitivos, violentos etc.), além de coletar indicadores acadêmicos mais detalhados (médias de matérias específicas ou provas padronizadas) e dados sobre hábitos de estudo ou saúde (sono, alimentação). Em seguida, seria importante aplicar testes estatísticos inferenciais para quantificar relações entre as variáveis. Por exemplo, testes de correlação (Pearson ou Spearman) podem revelar se as horas de jogo se associam significativamente às notas, e modelos multivariados (regressão linear/logística) ou técnicas de aprendizado de máquina poderiam ser usados para prever o desempenho escolar a partir de fatores de jogo e socioeconômicos. Estudos anteriores de modelagem preditiva sugerem justamente explorar diferentes bases de dados e algoritmos para aumentar a robustez dos achados.

* Além disso, o uso de dados longitudinais (coleta de informações repetidas ao longo do tempo) permitiria investigar dinamicamente como mudanças nos hábitos de jogo afetam o rendimento escolar, superando a limitação do desenho transversal. Finalmente, recomenda-se ampliar a amostra: envolver alunos de múltiplas escolas, regiões ou até países diferentes, o que aumentaria a diversidade dos dados e a validade externa das conclusões. Como observado em estudos correlatos, incluir dados de diversas origens geográficas e testar diferentes modelos (classificadores ou regressões) é um caminho promissor para trabalhos futuros.

* Essas iniciativas tornariam as análises mais abrangentes e permitiriam inferir conclusões mais seguras sobre a relação entre hábitos de jogo e desempenho acadêmico.

---
