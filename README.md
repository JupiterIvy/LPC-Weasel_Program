# Programa da doninha de Dawkins
- Trata-se de uma proposição feita no livro “A origem das espécies”, do naturalista britânico Charles Darwin.

- O programa da doninha de Dawkins ou Dawkins’ weasel program é um experimento ilustrado por simulações computacionais. Seu objetivo é demonstrar que o processo que impulsiona sistemas evolutivos(combinação de mudanças aleatórias com seleção não aleatória) é diferente do puro acaso.

- Assim como o teorema matemático do macaco infinito, o programa da doninha de Dawkins se baseia na reprodução de várias sequências de caracteres até que se forme a sequência desejada predefinida.

## Exemplo de algoritmo:
 
1) Inicie com uma sequência aleatória de 28 caracteres (frase).

2) Faça 100 cópias da sequência inicial de caracteres (reprodução).

3) Para cada caracteres, em cada uma das 100 cópias, substitua (mutação), com uma probabilidade de 5%, o caracteres por um novo caracter aleatório.

4) Compare cada nova sequência de caracteres com a frase alvo "METHINKS IT IS LIKE A WEASEL", e dê a cada cópia gerada uma pontuação (número de letras na sequência e na posição correta).

5) Se alguma das novas sequências de caracteres (frases) tiver uma pontuação perfeita (28, todas as letras na sequência e posição corretas), pare. Caso contrário, pegue a frase de maior pontuação e recomece da etapa 2.

## Executando o código

É necessário possuir instalado Python 3.8 ou maior em sua máquina, você pode instalar [aqui](https://www.python.org/downloads/).

```bash
# Mac/Linux/Windows 
python --version
```

Com Python3 configurado, configure suas variáveis de git (sem as chaves do exemplo):

```bash
# Git config (https)
git config --global user.email [seu e-mail] 
git config --global user.name [seu nickname] 
```

Clone o repositório em uma pasta vazia (recomendado) e acesse a pasta do repo:

```bash
# Git clone (https)
git clone https://github.com/JupiterIvy/LPC-Weasel_Program
cd LPC-Weasel_Program
```

E por fim, execute o código .py 

```bash
# Executando o arquivo
py weasel.py
```
