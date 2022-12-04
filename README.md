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
py dawkins.py
```

# COLABORADORES

<table>
<tr>
    <td align="center"><a href="https://github.com/gabrielrejtman"><img src="https://media-exp1.licdn.com/dms/image/C5603AQHu_N3qvTsMzg/profile-displayphoto-shrink_800_800/0/1641293498560?e=1675900800&v=beta&t=jeaOcNltgrHOpBuWRzhi5gY3ZxwVXNhq2RHBRZ2L-sI" width="100px;" alt=""/><br /><sub><b>Gabriel Rejtman</b></sub></a><br /></td> 
    <td align="center"><a href="https://github.com/JupiterIvy"><img src="https://media-exp1.licdn.com/dms/image/C4D03AQEG-wsIUgywOQ/profile-displayphoto-shrink_800_800/0/1628275051792?e=1675900800&v=beta&t=r2o-HH0YrChIX1pe1ykr7kFwAQ_gGuX8ZO29WWqFALA" width="100px;" alt=""/><br /><sub><b>Evelyn Bessa</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/dinglem"><img src="https://user-images.githubusercontent.com/65917017/205512227-0997b11a-99a7-43ae-a3e8-560e0fcf5951.jpg" width="100px;" alt=""/><br /><sub><b>Gabriel Machado</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/haidao01"><img src="https://media-exp1.licdn.com/dms/image/D4D03AQGFYWK0_MCdEA/profile-displayphoto-shrink_800_800/0/1669254739271?e=1675900800&v=beta&t=viKQEinfQfKI7L79GK2YhUp1gebf2fOh_upgaIuVzmA" width="100px;" alt=""/><br /><sub><b>Francisco Neto</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sweilos"><img src="https://media-exp1.licdn.com/dms/image/D4D03AQH2n5r7yK2Mkg/profile-displayphoto-shrink_800_800/0/1669242202565?e=1675900800&v=beta&t=Qo5smfHoOd43m7yOA3dZd9rVMu3J7955vlbAy09nG7o" width="100px;" alt=""/><br /><sub><b>Yago Nunes</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/End-009"><img src="https://media-exp1.licdn.com/dms/image/C4E03AQGVuKyd3pPOFA/profile-displayphoto-shrink_800_800/0/1635445369531?e=1675900800&v=beta&t=nEASP9lZeybgLi2-BVV2BbOPQmR3KOYqKzCrzxh-ZPQ" width="100px;" alt=""/><br /><sub><b>Endrique Silva</b></sub></a><br /></td>
</table>
