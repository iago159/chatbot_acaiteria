# Processamento de Linguagem Natural: Chatbot para Açaiteria

# Sobre o projeto

Com o avanço do poder de processamento dos computadores, nos últimos anos o deep learning ganhou extrema notoriedade no campo da inteligência artificial, especialmente quando se fala em Processamento de Linguagem Natural.

Uma das principais bibliotecas para o aprendizado profundo no Python é o Pytorch, que, quando trabalhada em conjunto a outras bibliotecas como o SpaCy, possibilita a criação de uma enorme quantidade de aplicações, dentre as quais há uma que se destaca por estar ganhando espaço no nosso cotidiano: o Chatbot.

Pensando nisso desenvolvi a Bia, uma inteligência artificial feita para uma açaiteria fictícia que te ajuda na sua compra, respondendo perguntas comuns como o tempo de entrega, sabores, preços e até mesmo contando piadas.

Para uma melhor experiência do usuário, foi desenvolvida uma interface gráfica utilizando a biblioteca Tkinter, deixando bem intuitivo e agradável a utilização do programa.

Em um primeiro momento, a aplicação foi desenvolvida removendo as stopwords - palavras do texto consideradas irrelevantes - fornecidas pela biblioteca NLTK. Contudo, com essa remoção o modelo não apresentou uma boa precisão. Analisando, cheguei a conclusão que isso se deve a dois fatores: a base de dados pequena e o fato de que os próprios textos em linguagem natural são pequenos, o que faz os textos sem as stopwords ficarem bem parecidos entre si. Ao não fazer uso dessa técnica, o modelo melhorou consideravelmente, e, mesmo com uma base de dados pequena, consegue entender e responder as principais perguntas feitas pelo usuário.

# Principais Tecnologias Utilizadas

- Python
- Pytorch
- SpaCy
- Tkinter
- Re (Expressões Regulares)

# Principais Técnicas de Pré-Processamento Utilizadas

- Remoção de acentuações
- Remoção de pontuações
- Remoção de espaços duplos
- Lemmatization
- Word2vec (word embedding)

# Interface

![Interface](https://github.com/iago159/chatbot_acaiteria/blob/main/chatbot_interface.jpg)

# Autor

Iago Alves Brito

https://www.linkedin.com/in/iagobrito/

