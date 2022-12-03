# Programa da doninha de Dawkins
- Trata-se de uma proposição feita no livro “A origem das espécies”, do naturalista britânico Charles Darwin.

- O programa da doninha de Dawkins ou Dawkins’ weasel program é um experimento ilustrado por simulações computacionais. Seu objetivo é demonstrar que o processo que impulsiona sistemas evolutivos(combinação de mudanças aleatórias com seleção não aleatória) é diferente do puro acaso.

## Exemplo de algoritmo:
 
1) Inicie com uma sequência aleatória de 28 caracteres (frase).

2) Faça 100 cópias da sequência inicial de caracteres (reprodução).

3) Para cada caracteres, em cada uma das 100 cópias, substitua (mutação), com uma probabilidade de 5%, o caracteres por um novo caracter aleatório.

4) Compare cada nova sequência de caracteres com a frase alvo "METHINKS IT IS LIKE A WEASEL", e dê a cada cópia gerada uma pontuação (número de letras na sequência e na posição correta).

5) Se alguma das novas sequências de caracteres (frases) tiver uma pontuação perfeita (28, todas as letras na sequência e posição corretas), pare. Caso contrário, pegue a frase de maior pontuação e recomece da etapa 2.
