# Sistema de Restaurante

Este é um projeto de um sistema simples de restaurante, onde o cliente pode se cadastrar, fazer pedidos de comida e bebida, e realizar o pagamento com base no saldo disponível na sua conta.

## Estrutura do Projeto

O sistema é dividido em várias classes que implementam funcionalidades específicas:

- **Cliente**: Gerencia as informações do cliente, como nome, idade, CPF, endereço e saldo.
- **Cardapio**: Contém os itens disponíveis no cardápio (pratos e bebidas), exibe o cardápio e calcula os valores.
- **Pedido**: Registra os itens pedidos pelo cliente e calcula o valor total do pedido.
- **Pagamento**: Verifica se o cliente tem saldo suficiente, realiza o pagamento e emite uma nota fiscal.

## Funcionalidades

1. **Cadastro de Cliente**: O cliente fornece seus dados e o sistema valida essas informações.
2. **Escolha de Pedido**: O cliente escolhe os itens do cardápio.
3. **Pagamento**: O sistema calcula o valor total do pedido e realiza o pagamento.
4. **Nota Fiscal**: Após o pagamento, uma nota fiscal é emitida.

