# Gerador e Validador de CPF

## Descrição

Este projeto foi desenvolvido como parte do estudo pessoal em programação com Python. O programa tem duas funcionalidades principais: a geração aleatória de CPFs válidos e a verificação da validade de CPFs informados pelo usuário. Todas as validações seguem as regras oficiais da Receita Federal para os dígitos verificadores.

## Funcionalidades

* Menu inicial com duas opções: gerar ou validar CPF
* Geração aleatória de CPFs válidos
* Validação de CPFs informados manualmente (com ou sem pontuação)
* Interface em modo texto, compatível com terminal/console
* Limpeza automática da tela para melhor experiência visual

## Como Usar

1. Execute o arquivo Python no terminal.
2. Escolha a opção desejada:

   * `[1]` para gerar um CPF válido
   * `[2]` para verificar a validade de um CPF digitado
3. Siga as instruções na tela.
4. Para sair, pressione qualquer tecla diferente de 1 ou 2 no menu.

## Observações

* A validação permite entrada de CPF com ou sem formatação (ex: `123.456.789-09` ou `12345678909`)
* Não é necessário conhecimento prévio de funções ou estruturas complexas
* O código foi desenvolvido sem o uso de funções, conforme o conteúdo visto até o momento do curso
* Compatível com Windows, Linux e macOS via `os.system('cls' or 'clear')`

## Exemplo de Execução

```text
=====================
      < Menu >
=====================
Você gostaria de:
[1] Gerar um cpf
[2] Verificar a validade de um cpf
[Qualquer outra Tecla] Sair
```

## Requisitos

* Python 3 instalado no sistema
* Terminal compatível com comandos de limpeza de tela (`cls` no Windows ou `clear` no Linux/macOS)

## Autora
Lana Ramos Gomes

## Licença
MIT License
