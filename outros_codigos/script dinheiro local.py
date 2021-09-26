from decimal import Decimal
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR') 
# Aqui definimos que nosso local é Brasil 
# e isso implica a utilização do R$ para o currency
# além do uso do ponto para separar as casas de centenas, milhares etc
# e a vírgula para separar os centavos

valor = Decimal('1254897.25')
print(locale.currency(valor, grouping=True))
