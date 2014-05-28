
"""
lsystem_2014.py

Uma versão simples de um sistema L.
As regras implementadas como um dicionário
Visualização por recurso ao módulo turtle.
"""


# Reescrita
def main(axioma,regras,passos):
	resultado=reescreve(axioma,regras,passos)
	return resultado
	
def reescreve(exp,regras,passos):
	forma = exp
	for i in range(passos):
		forma = aplica(regras,forma)
	return forma

def aplica(regras,exp):
	forma=''
	for ch in exp:
		forma = forma + regras.get(ch,ch)
	return forma

# ----------------------------------------------------------
# Simular um sistema L simples por recurso a0 módulo turtle
# ----------------------------------------------------------

from turtle import *

def inic():
	"""Inicializa o sistema."""
	reset()
	up()
	shape('turtle')
	color('red')
	speed(0)
	setheading(0)
	goto(0,0)

def desenho(seq):
	inic()
	interpreta(seq)
	mainloop()

def interpreta(comandos):
	""" Interpretador dos comandos."""
	for com in comandos:
		exec(dicio_tarta[com])
	hideturtle()

if __name__ == '__main__':
	
	# Exemplo 1
	# Parâmetros iniciais
	tam = 30
	ang = 29
	#Sistema -L
	regras={'B':'A','A':'AB'}
	axioma='B'
	# Interpretação para a tartaruga
	dicio_tarta={'A':'pd();fd(tam);pu()','B':'rt(ang)'}
	"""
	# Exemplo 2
	# Parâmetros iniciais
	tam = 10
	ang = 90
	#Sistema -L
	regras={'X':'X+YF+','Y':'-FX-Y'}
	axioma='FX'
	# Interpretação para a tartaruga
	dicio_tarta={'F':'pd();fd(tam);pu()','+':'rt(ang)', '-':'lt(ang)', 'X':'','Y':''}
	"""
	# Geral
	comandos = main(axioma,regras,11)
	desenho(comandos)
