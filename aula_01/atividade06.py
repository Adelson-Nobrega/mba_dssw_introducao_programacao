print('CÁLCULO DE QUANTIDADE DE TINTA E CUSTO PARA TANQUES CILÍNDRICOS')

PI = 3.14
preco = 50.00

r_tanque = float(input("Digite o raio da base do tanque cilíndrico: "))
alt_tanque = float(input('Digite a altura do tanque cilíndrico: '))

area_tanque = (PI * (r_tanque ** 2)) + (2 * PI * r_tanque * alt_tanque)
tot_litros = area_tanque / 3
tot_latas = round(tot_litros / 5)
custo = tot_latas * preco

print(f'A quantidade de latas de tintas necessárias é {tot_latas}')
print(f'Custo total das latas de tintas: R$ {custo:.2f}')
