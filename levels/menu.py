'''

    PROGRAMA AUXILIAR RESPONSAVEL POR MOSTRAR O MENU INICIAL DO JOGO CELL DEFENSE 1.0

    -> Conta com duas opcoes basicas:

    1. Jogar (inicia a fase 1)
    2. Tutorial (carrega janela Tutorial)
    3. Sair (finaliza o jogo)
'''

from models import utilities
from levels import State
import pyxel

#CODIGO PRINCIPAL
class Menu(State):

    def onEnter(self, game):
        #inicializando janela
        pyxel.mouse(True)
        #carregando icones do jogo
        pyxel.load("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/CELL_DEFENSE-1.0/Assets/sprites-cell_defense.pyxres")
        #carregando fonte das letras
        self.fonte = pyxel.Font("/home/hacdan/Documents/Linux/Programacao/Python/Projetos/Pyxel/CELL_DEFENSE-1.0/Assets/Fonts/helvB24.bdf")
        #declarando tilemap para decoracao da janela menu
        self.decoration = pyxel.tilemaps[0]

        #declarando e inicializando retangulos do menu (para colisao e display de mensagens)
        self.recJogar = [45, 35, 40, 20, pyxel.COLOR_GREEN]
        self.recSair = [45, 95, 40, 20, pyxel.COLOR_RED]
        #declarando flags de controle das opcoes do menu
        self.mouseOnJogar = False
        self.mouseOnSair = False

    def update(self, game):
        #checando se usuario esta com o mouse posicionado nas opcoes do menu
        if ( utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recJogar[0], self.recJogar[1], self.recJogar[2], self.recJogar[3])):
            self.mouseOnJogar = True
        elif ( utilities.checkPointOnRec(pyxel.mouse_x, pyxel.mouse_y, self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3])):
            self.mouseOnSair = True
        else:
            self.mouseOnJogar = False
            self.mouseOnSair = False

        #realizando opcoes de acordo com o clique do usuario
        if (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, hold=30)):
            if (self.mouseOnJogar):
                return "fase1"
            elif (self.mouseOnSair):
                pyxel.quit() #finalizando janela

    def draw(self, game):
        pyxel.cls(0) #limpando janela
        #desenhando tilemap
        utilities.draw_tilemapItens(pyxel, self.decoration, sprite_bank=0, LARGURA=154, ALTURA=86, TAMANHO=8, ESCALA=3, DELTAX=8, DELTAY=4)
        #desenhando menu (frases)
        #desenhando contorno nos botoes do menu caso o mouse esteja em cima deles
        if (self.mouseOnJogar):
            pyxel.rectb(self.recJogar[0], self.recJogar[1], self.recJogar[2], self.recJogar[3], pyxel.COLOR_GREEN)
        elif (self.mouseOnSair):
            pyxel.rectb(self.recSair[0], self.recSair[1], self.recSair[2], self.recSair[3], pyxel.COLOR_RED)
