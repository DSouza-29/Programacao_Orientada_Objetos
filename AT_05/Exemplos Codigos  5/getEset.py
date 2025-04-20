class Pessoa():
    def __init__(self,nome) -> None:
        self.__nome = nome
        self._numero_atualizacoes = 0

    #getter
    @property
    def nome(self):
        return self.__nome

    #setter
    @nome.setter
    def nome(self, nome):
        self._numero_atualizacoes+=1
        self.__nome = nome

    @property
    def numero_atualizacoes(self):
        return self._numero_atualizacoes

    def diga_oi(self):
        print(f"Oi {self.__nome}.")
        print(f"O nome foi alterado {self._numero_atualizacoes} vezes.")

pessoa = Pessoa("Kaio")
pessoa.diga_oi()

pessoa.__nome = "mudei" #Assim não consegue mudar
pessoa.diga_oi()

#x=Pessoa("Roberto")
#x._Pessoa__nome = "mudou" #mudando mesmo protegido
#x.diga_oi()

#pessoa.nome="Kaio Jonathas"
#pessoa.diga_oi()
