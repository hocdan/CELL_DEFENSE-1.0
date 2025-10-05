'''
    -> ARQUIVO RESPONSAVEL POR DECLARAR AS CLASSES RESPONSAVEIS PELAS
    ESTRUTURAS DE DEFESA DO JOGO

    -> Contem uma classe mae chamada CELULA e suas derivacoes:
    1. Neutrofilo
    2. 

'''
import pyxel

class Celula:
    #inicializacao dos atributos
    def __init__(self, posX, posY, tipo, nivel, alcance, dano, frame):
        self.posX = posX #posicao inicial no eixo X
        self.posY = posY #posicao inicial no eixo Y
        self.tipo = tipo #tag para distinguir as diferentes estruturas
        self.nivel = nivel #usado para verificar upgrades e custos
        self.alcance = alcance #valor dado por R = raio do circulo de alcance
        self.dano = dano #quantidade de dano causado por disparo das estruturas
        self.frame = frame #flag usada para registrar em qual sprite a estrutura vai ser desenhada
    
    #metodo para visualizar o alcance da torre (circulo delineado em branco)
    def mostrarAlcance(self):
        #desenhando circulo referente ao alcance da torre
        pyxel.circb(self.posX+8, self.posY+8, self.alcance, pyxel.COLOR_WHITE)

class Neutrofilo(Celula):
    super.__init__(tipo="Neutrofilo")

    def realizarAnimacao(self, escala):
        if (self.frame == 1):
            pyxel.blt(
                self.posX, #coordenada X na janela onde a sprite sera desenhada
                self.posY, #coordenada Y na janela onde a sprite sera desenhada
                0, #sprite_bank da animacao do neutrofilo == 0
                16, #tamanho de pixels na largura
                16, #tamanho de pixels na altura
                0, #coordenada X do sprite_bank
                48, #coordenada Y do sprite_bank
                scale=escala #escalando o tamanho da imagem
            )
            #atualizando flag frame para a proxima animacao
            self.frame += 1
        elif (self.frame == 2):
            pyxel.blt(
                self.posX, #coordenada X na janela onde a sprite sera desenhada
                self.posY, #coordenada Y na janela onde a sprite sera desenhada
                0, #sprite_bank da animacao do neutrofilo == 0
                16, #tamanho de pixels na largura
                16, #tamanho de pixels na altura
                0, #coordenada X do sprite_bank
                64, #coordenada Y do sprite_bank
                scale=escala #escalando o tamanho da imagem
            )
            #atualizando flag frame para a proxima animacao
            self.frame += 1
        elif (self.frame == 3):
            pyxel.blt(
                self.posX, #coordenada X na janela onde a sprite sera desenhada
                self.posY, #coordenada Y na janela onde a sprite sera desenhada
                0, #sprite_bank da animacao do neutrofilo == 0
                16, #tamanho de pixels na largura
                16, #tamanho de pixels na altura
                0, #coordenada X do sprite_bank
                80, #coordenada Y do sprite_bank
                scale=escala #escalando o tamanho da imagem
            )
            #atualizando flag frame para a proxima animacao
            self.frame = 1 #resetando para a sprite inicial
