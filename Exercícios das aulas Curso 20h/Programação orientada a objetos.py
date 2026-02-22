class Pessoa: 
    def __init__(self,nome,idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    def apresentar(self):
        print ('Olá, meu nome é',self._nome,', tenho', self._idade, 'anos e tenho', self._altura, 'de altura.')

    def get_nome(self):
        return self._nome

    def set_idade(self, nova_idade):
        if nova_idade <40:
            self._idade = nova_idade

    


""" p1 = Pessoa("João",33,"1,80")
p2 = Pessoa("Mariana",20,"1,70")

p1.apresentar ()
p2.apresentar ()

p1.set_idade (40)
p1.apresentar() """

""" print (p1.get_nome()) """

class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade,altura)
        self.matricula = matricula
    def estudante(self):
        print('A matrícula do aluno é', self.matricula)

    def apresentar(self):
        print ('Olá, meu nome é',super().get_nome(),'e minha matrícula é:', self.matricula)


aluno1 = Aluno('Pedro',30,'1,90','00929929')

aluno1.estudante()
aluno1.apresentar()

