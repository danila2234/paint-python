import pygame
import random
import shelve
import tkinter as tk
from screeninfo import *

for m in get_monitors():
    monitor_w = m.width
    monitor_h = m.height

# FPS и размер экрана:

FPS = 60
WIDTH = monitor_w
HEIGHT = monitor_h

# Цвета:

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Инициализация pygame:

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Создание блоков:

Guidance_anim = ['Sprite-Guidance.png', 'Sprite-Guidance1.png']
Iconca_1 = pygame.image.load('Sprite-Pen.png')
Iconca_2 = pygame.image.load('Sprite-Eraser.png')
Frame = pygame.image.load('Sprite-Frame.png')
Cross = pygame.image.load('Sprite-Cross.png')
index = 0
Bool = False
Guidance = pygame.image.load(Guidance_anim[0])
pos_blocks = []
color_blocks = []
Drawing = False
Erasing = False
COLOR = ['Sprite-Wooden wall.png', 'Sprite-Blue.png', 'Sprite-Red.png', 'Sprite-Green.png']
Motion = 'None'
Motion1 = False
Number = 1


# Создание ползунков:

Sprite_Polzunok = pygame.image.load('Sprite-Polzunok.png')
Sprite_Frame_Left = pygame.image.load('Sprite-Left_Frame.png')
Sprite_Frame_Right = pygame.image.load('Sprite-Right_Frame.png')
Sprite_Frame = pygame.image.load('Sprite-Frame1.png')
R = 0
G = 0
B = 0
r_mon_frame = 150
Pos = [[WIDTH - r_mon_frame, 18], [WIDTH - r_mon_frame, 36], [WIDTH - r_mon_frame, 54]]
Polzunok1 = pygame.Rect(WIDTH - r_mon_frame, 20, 8, 13)
Polzunok2 = pygame.Rect(WIDTH - r_mon_frame, 36, 8, 13)
Polzunok3 = pygame.Rect(WIDTH - r_mon_frame, 54, 8, 13)
Polzunky = [Polzunok1, Polzunok2, Polzunok3]
colors = [R, G, B]
Index = 0

def Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, PosX, PosY, Length, Range, Events, Index1, Peremnn):

	global Motion1
	global Polzunky
	global Index
	global colors
	global color

	if not Events:

		screen.blit(Sprite_Polzunok, (Polzunky[Index1].left, PosY))
		Variable_Range = (int(Polzunky[Index1].left) - (PosX - (Length / 2))) // (Length / Range)
		colors[Index1] = Variable_Range
		screen.blit(Sprite_Frame_Right, ((PosX - (Length / 2)) - 4, PosY - 2))
		screen.blit(Sprite_Frame_Left, ((PosX + (Length / 2)) + 6, PosY - 2))
		Sprite_Frame_size = pygame.transform.scale(Sprite_Frame, (Length + 4, 17))
		screen.blit(Sprite_Frame_size, ((PosX - (Length / 2)) + 2.5, PosY - 2))

		if Motion1:

			global PosCursor

			if Index == Index1:

				Polzunky[Index].left = int(PosCursor[0]) - 2.5

				if Polzunky[Index].left < (PosX - (Length / 2)):

					Polzunky[Index].left = (PosX - (Length / 2))

				if Polzunky[Index].left > (PosX + (Length / 2)):

					Polzunky[Index].left = (PosX + (Length / 2))

	if Events:

		global e

		if e.type == pygame.MOUSEBUTTONDOWN:

			for p in Polzunky:

				if (p.right - p.width) < int(PosCursor[0]) < p.right:

					if (p.bottom - p.height) < int(PosCursor[1]) <= p.bottom:

						Motion1 = True
						Index = Polzunky.index(p)
						print(Index)

		if e.type == pygame.MOUSEBUTTONUP:

			Motion1 = False


# Создание текста к слайдерам

FontK = pygame.font.Font("prstartk.ttf", 10)
Text_r = FontK.render(('r') , True, RED)
Text_g = FontK.render(('g') , True, GREEN)
Text_b = FontK.render(('b') , True, BLUE)

# Создание сохранения:

File = shelve.open('Save')
if not ('Position' in File):

	File['Position'] = pos_blocks

pos_blocks = File['Position']

# Создание главного цикла:

running = True

while running:

	color = (colors[0], colors[1], colors[2])

	PosCursor = pygame.mouse.get_pos()

	x_block = int(PosCursor[0] / 20)
	y_block = int(PosCursor[1] / 20)
	x_block *= 20
	y_block *= 20

	screen.fill(WHITE)

	# Отрисовка:

	Guidance = pygame.image.load(Guidance_anim[0])
	screen.blit(Guidance, (x_block - 2.5, y_block - 2.5))

	for p in pos_blocks:

		pygame.draw.rect(screen, p[2], (p[0], p[1], 20, 20))

	if Motion == 'Drawing':

		pygame.draw.rect(screen, color, (x_block, y_block, 20, 20))

	screen.blit(Frame, (197, 22))
	screen.blit(Frame, (237, 22))
	screen.blit(Frame, (157, 22))
	screen.blit(Iconca_1, (200, 25))
	screen.blit(Iconca_2, (240, 25))
	screen.blit(Cross, (160, 25))

	screen.blit(Text_r, (WIDTH - 225, 18))
	screen.blit(Text_g, (WIDTH - 225, 36))
	screen.blit(Text_b, (WIDTH - 225, 54))

	pygame.draw.rect(screen, color, (WIDTH - 60, HEIGHT - (HEIGHT - 18), 50, 50))
	
	# Создание событийного цикла:
	
	events = pygame.event.get()
	
	for e in events:
		
		# Элементы цикла:

		Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[0][0], Pos[0][1], 100, 255, True, 1, R)
		Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[1][0], Pos[1][1], 100, 255, True, 2, G)
		Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[2][0], Pos[2][1], 100, 255, True, 3, B)
		
		if e.type == pygame.QUIT:

			running = False

		if e.type == pygame.KEYDOWN:

			if e.key == pygame.K_ESCAPE:

				running = False

			if e.key in [pygame.K_LCTRL, pygame.K_s]:

				File['Position'] = pos_blocks

			if e.key in [pygame.K_LCTRL, pygame.K_d]:

				File.clear()

		if e.type == pygame.MOUSEBUTTONDOWN:

			if e.button == 1:

				if Motion == 'Drawing':

					Erasing = False
					Drawing = True

				if 197 <= e.pos[0] <= (197 + 31):

					if 22 <= e.pos[1] <= (22 + 31):

						Motion = 'Drawing'

				if 237 <= e.pos[0] <= (237 + 31):

					if 22 <= e.pos[1] <= (22 + 31):

						Motion = 'Erasing'

				if 157 <= e.pos[0] <= (157 + 31):

					if 22 <= e.pos[1] <= (22 + 31):

						Motion = 'None'
						Drawing = False
						Erasing = False

				print(Motion)

				if Motion == 'Erasing':

					Drawing = False
					Erasing = True


		if e.type == pygame.MOUSEBUTTONUP:

			if e.button == 1:

				if Motion == 'Drawing':

					Drawing = False

				if Motion == 'Erasing':

					Erasing = False

	if Drawing:

		if not ((x_block, y_block, color) in pos_blocks):

			pos_blocks.append((x_block, y_block, color))

	if Erasing:

		for p in pos_blocks:

			if (x_block, y_block, p[2]) in pos_blocks:

				pos_blocks.remove((x_block, y_block, p[2]))

	Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[0][0], Pos[0][1], 100, 255, False, 0, R)
	Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[1][0], Pos[1][1], 100, 255, False, 1, G)
	Polzunok(Sprite_Frame_Right, Sprite_Frame_Left, Sprite_Frame, Sprite_Polzunok, Pos[2][0], Pos[2][1], 100, 255, False, 2, B)

	pygame.display.update()
	clock.tick(FPS)
pygame.quit()
File.close()