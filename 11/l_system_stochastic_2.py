"""
l_system_stochastic_2.py

May 2014
Ernesto Costa
"""

from turtle import *
from random import randint, choice

# -----------------------------------------------------------
# Sistema de Reescrita
# As regras implementadas como um dicionário
# -----------------------------------------------------------

""" 
axioma= 'F'
regras = {'F': 'F[+F]F[-F][F]'}
tam = 5
ang = 20


axioma = 'F'
regras = {'F':'F[+F[+F]-F][-F]F'}
tam = 5
ang = 29

"""
# -----------------------------------------------------------
# Reescrita
def reescrita(axioma,regras,passos):
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
		alternativas = regras.get(ch,ch)
		escolha = choice(alternativas)
		forma = forma + escolha
	return forma


# ---------------------------------------------------------------
# Interpretador	
# Simular um sistema L simples por recurso a turtle
# ---------------------------------------------------------------



def inic():
	"""Inicializa o sistema."""
	reset()
	up()
	shape('turtle')
	color('red')
	width(1)
	setheading(90) 
	goto(0,-200)
	speed(0) 


def desenho(seq):
	inic()
	interpreta(seq)
	hideturtle()
	mainloop()

def interpreta(comandos):
	""" Interpretador dos comandos."""
	for com in comandos:
		exec(dicio_tarta[com])
# ------------------------------------------------------------------		
# gestão da pilha dos estados		
def guarda_estado(estados):
	"""guarda o estado corrente (xpos,ypos,angulo)"""
	xpos = xcor()
	ypos = ycor()
	angulo=heading()
	estados.append((xpos,ypos,angulo))
	return estados

	
def restaura_estado(estados):
	""" Restaura o estado anterior.
	"""
	xpos,ypos,angulo = estados.pop()
	goto((xpos,ypos))
	seth(angulo)
	return (xpos,ypos,angulo)

if __name__ == '__main__':
	# Parametrização
	"""
	# exemplo 1
	regras={'B':'F[-B]+B','F':'FF'} # árvore
	axioma='B'
	tam=10
	ang=50
	"""
	# exemplo 2
	axioma = 'F'
	regras = {'F':['F[+F]F[-F]F', 'F[-F]F[+F]F','F[-FF-F]F']}
	tam = 7
	ang = 29	
	passos = 4
	estados = []
	# Interpretação para a tartaruga
	dicio_tarta={'F':'pd();fd(tam);pu()','B':'pass','f':'pu();fd(tam)',
'-':'rt(ang)','+':'left(tam)','[':'guarda_estado(estados)',']':'restaura_estado(estados)'}
	comandos=reescrita(axioma,regras,passos)
	desenho(comandos)
	