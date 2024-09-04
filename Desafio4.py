sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
valorTotal = sp + rj + mg + es + outros

spPorcentagem = sp * 100 / valorTotal
rjPorcentagem = rj * 100 / valorTotal
mgPorcentagem = mg * 100 / valorTotal
esPorcentagem = es * 100 / valorTotal
outrosPorcentagem = outros * 100 / valorTotal

print(f"O percentual de representação de São Paulo é {spPorcentagem:.2f}%")
print(f"O percentual de representação do Rio de Janeiro é {rjPorcentagem:.2f}%")
print(f"O percentual de representação de Minas Gerais é {mgPorcentagem:.2f}%")
print(f"O percentual de representação do Espírito Santo é {esPorcentagem:.2f}%")
print(f"O percentual de representação dos outros estados é {outrosPorcentagem:.2f}%")