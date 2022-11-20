def tratar_resposta(valor):
    valor = str(valor)
    if valor in "if" or valor in "else" or valor in "elif" or valor in "condicional":
        print("Digite o número da opção:")
        print("1- O que é uma estrutura condicional?")
        print("2- Como declarar um if, if else e elif")

        opcao = input("Opção número: ")
        if opcao == "1":
            print('''
A condicional if é uma estrutura condicional que executa a afirmação, dentro do bloco, se determinada condição for verdadeira.
Se for falsa, executa as afirmações dentro de else.
Em Python, elif é a abreviação de "else if" e é usado quando a primeira instrução if não for verdadeira,
e você deseja verificar outra condição. Ou seja, as instruções elifif combinam com as instruções if e else para executar uma série de verificações.
                    ''')
        elif opcao == "2":
            print('''
Python suporta as condições lógicas usuais da matemática:

Igual a: a == b
Diferentes: a != b
Menor que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b

O Python depende do recuo (espaço em branco no início de uma linha) para definir o escopo no código.
Outras linguagens de programação costumam usar colchetes para essa finalidade.

Veja abaixo a sintaxe:
if (valor > 5) {

} else if (valor > 50) {

} else {

}
                    ''')

    return ""
