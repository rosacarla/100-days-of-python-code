# Um restaurante gostaria de limitar a quantidade de cupons de desconto utilizados por noite em seu estabelecimento.
# Para tal, o dono gostaria de um aplicativo em que a recepcionista do restaurante pudesse informar toda vez que um ou mais
# clientes apresentassem o cupom na entrada, e quando o limite da noite fosse atingido, um alerta fosse emitido.
#
# Faça um algoritmo que:
# a) receba a quantidade de cupons apresentados a cada nova mesa ocupada
# b) informe a quantidade de cupons restantes até atingir o limite da noite
# c) mostre a mensagem: "Não devem mais ser aceitos cupons de desconto" quando o limite for atingido
#
# O limite pode ser fixado em 10.

limite = 10

while True:

    qtde = int(input("Quantos cupons foram apresentados pela mesa? "))

    limite = limite - qtde

    if limite > 0:
        print("Ainda temos {} cupons!".format(limite))
    else:
        print("Não devem mais ser aceitos cupons de desconto")

        # Interrompe a repetição atual
        break;

print("Fim!")
