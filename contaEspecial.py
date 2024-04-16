'''Ex Herança - POO- Joísa

ContaBancaria e ContaEspecial
Exercício 1: Conta Especial
Considere a classe ContaBancaria. A classe ContaBancaria encontra-se disponível no
arquivo contabancaria.py.
Escreva agora a classe ContaEspecial.
Uma conta especial é uma conta bancária que ( além de ter tudo que contabancária tem)
possui também um limite especial (limite de crédito).
Uma ContaEspecial é criada com numero, nome, senha, limite e saldo. O saldo é
opcional. Se não fornecido é 0.0, como no caso de qualquer conta bancária.
Ao ser dado um print em uma ContaEspecial, devem ser exibidos, além dos dados
básicos da conta, também o limite especial.
Na hora de fazer um saque, o saldo pode ficar negativo até -limite da conta. O limite
não muda. Por exemplo, se o saldo for 1000 e o limite 500, poderia ser feito um saque
(máximo) de 1500 reais, o saldo ficaria -500 e o limite continuaria 500.
Crie uma lista com contas normais e especiais. Exiba a lista.'''


from contabancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    def __init__(self, numero, nome, senha, limite, saldo):
        super().__init__(numero, nome, senha, saldo)
        self.limite = limite
    
    def __str__(self):
        return super().__str__(self) + '-' + self.limite
    
    def saque(self,valor,senha):
        if self.senha != senha:
            print('SENHA INCORRETA')
        else:
            saldoLimite = self.saldo+self.limite
            if valor < saldoLimite:
                self.saldo -= saldoLimite
            else:
                print('SALDO INSUFICIENTE!')
