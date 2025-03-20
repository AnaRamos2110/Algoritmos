# Jogo da Roleta - Mighty King Dice

Este é um simples jogo de roleta onde o jogador pode apostar em um número (de 0 a 36) ou em uma cor (Vermelho ou Preto). O código simula uma roleta com 37 números (incluindo o número 0, que representa a vitória da casa), e ao final, o programa sorteia um número e uma cor aleatoriamente para determinar se o jogador ganhou ou perdeu.

## Funcionalidades

- O jogador pode escolher entre apostar em um número ou em uma cor.
- O código sorteia um número aleatório da roleta e verifica se a aposta do jogador foi vencedora.
- Se o jogador acertar o número ou a cor, ele vence. Caso contrário, perde.
- O número "0" sempre representa a vitória da casa.

## Estrutura do Código

### 1. **Enumeração `CorRoleta`**
   - Define as cores da roleta:
     - `VERMELHO`: Números ímpares.
     - `PRETO`: Números pares.
     - `ZERO`: Representa a casa (número 0).

### 2. **Função `criarRoleta()`**
   - Cria a roleta com 37 números (0 a 36), onde:
     - O número `0` é associado à cor `ZERO` (vitória da casa).
     - Números pares (exceto 0) são associados à cor `PRETO`.
     - Números ímpares são associados à cor `VERMELHO`.
   - Retorna uma lista de tuplas contendo o número e sua respectiva cor.

### 3. **Função `sortear_numero()`**
   - Sorteia aleatoriamente um número e cor da roleta usando a função `random.choice()`.
   - Retorna o número sorteado e sua cor associada.

### 4. **Função `jogar_roleta()`**
   - Função principal do jogo. Controla a interação com o jogador, permitindo que ele escolha uma aposta (número ou cor).
   - O jogador faz sua aposta e, em seguida, o número é sorteado.
   - Dependendo da aposta (número ou cor), o programa verifica se o jogador venceu ou perdeu e exibe a mensagem correspondente.

### 5. **Execução do Jogo**
   - A função `jogar_roleta()` é chamada se o arquivo for executado diretamente (via `if __name__ == "__main__":`).
   
## Como Jogar

1. Ao iniciar o jogo, você será saudado e deverá fazer sua aposta.
2. Escolha entre:
   - **1** para apostar em um número (de 0 a 36).
   - **2** para apostar em uma cor (Vermelho ou Preto).
3. O programa sorteia um número e a cor correspondente e exibe o resultado.
4. Se você acertar o número ou a cor, você vence. Caso contrário, perde.

## Exemplo de Execução


## Observações

- O código utiliza a biblioteca `random` para o sorteio do número.
- O tipo de dado utilizado para representar as cores da roleta é um `Enum`, facilitando a manipulação e compreensão do código.
- O jogo possui uma interface simples via terminal/console.

## Requisitos

- Python 3.x ou superior

## Licença

Este projeto está licenciado sob a licença MIT.
