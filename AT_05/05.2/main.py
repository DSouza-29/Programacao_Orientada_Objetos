from pagamentos import CartaoCredito, BoletoBancario, Pix, MetodoPagamento

if __name__ == "__main__":
    valor = float(input("Digite o valor da compra: R$"))

    print("\nEscolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto Bancário")
    print("3 - PIX")

    escolha = input("Digite o número da opção: ")

    pagamento: MetodoPagamento 

    if escolha == "1":
        pagamento = CartaoCredito(valor)
    elif escolha == "2":
        pagamento = BoletoBancario(valor)
    elif escolha == "3":
        pagamento = Pix(valor)
    else:
        print("Opção inválida")
        exit()

    print("\n--- Comprovante ---")
    pagamento.pagar()

   
    # Com o uso do polimorfismo, foi possível usar uma única referência (pagamento) do tipo MetodoPagamento
    # para lidar com diferentes tipos de pagamento. Cada classe implementa o método pagar() de forma única,
    # mas a chamada é feita de forma genérica, facilitando a manutenção, legibilidade e expansão do sistema.

    
    # A interface (classe abstrata) garante que todas as formas de pagamento terão um método pagar(),
    # o que padroniza a lógica do sistema. Isso facilita a adição de novos métodos de pagamento no futuro
    # e evita erros por implementação incompleta.
