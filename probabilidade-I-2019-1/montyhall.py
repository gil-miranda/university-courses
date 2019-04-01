import numpy as np

def run(m, switch):
	win = 0
	loss = 0
	txt = "ao não trocar de porta"
	for i in range(m):
  		p, d = np.random.randint(low = 0, high = 3, size = 2)
  		if p == d: win += 1
  		elif p != d: loss += 1
	if switch == 1:
		a = win
		b = loss
		win = b
		loss = a
		txt = "ao trocar de porta"

	print("Foram simulados um total de "+ str(m) + " cenários \n")	
	print("Simulações feitas " + txt + " quando eliminada uma: \n")
	print("O jogador venceu em " + str(win) + " e perdeu em " + str(loss) + " a taxa de vitórias foi de " + str(win/m * 100) + "% \n")
