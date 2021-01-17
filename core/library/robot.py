import pygame
import time


class Task:
    def __init__(self, pointPos, countTiles, tilesSize, bricksPos, playerPos, paintPos):
        self.pointPos = pointPos
        self.countTiles = countTiles
        self.tilesSize = tilesSize
        self.bricksPos = bricksPos
        self.playerPos = playerPos
        self.paintPos = paintPos

class Robot:
    def __init__(self):
        self.move_items = {
            'Left': (-1, 0),
            'Right': (+1,0),
            'Up': (0,-1),
            'Down': (0,+1),
            'Paint': 'p'
        }
        self.tasks = {
            'task1' : Task(pointPos=(3,0),
                            countTiles=(4,2),
                            tilesSize=200,
                            bricksPos=[(2,1),(0,0)],
                            playerPos=(0,1),
                            paintPos=[(1,1),(1,0),(2,0)]),
            'task2' : Task(pointPos=(0,0),
                            countTiles=(7,4),
                            tilesSize=100,
                            bricksPos=[(0,1), (1,1), [2,1], [3,1], [4,1]],
                            playerPos=(1, 2),
                            paintPos=[(1,0), (2,0), (3,0), (4,0)])
        }

        self.moves = []

    def route_move(self, type_move):
        if type_move.startswith('task'):
            self.task = self.tasks[type_move]
        elif type_move == 'end':
            self.run_app()
        else:
            self.moves.append(self.move_items[type_move])

    def is_out_border(self, x_player, y_player, x_move, y_move, game_res, tile_size):
        """
        Функция возвращает, переходит ли игрок границу или стену
        """
        if x_player + x_move > game_res[0] or x_player + x_move < 0:
            return False
        elif y_player + y_move > game_res[1] or y_player + y_move < 0:
            return False
        for brickPos in self.task.bricksPos:
            if y_player + y_move == brickPos[1] * tile_size and x_player + x_move == brickPos[0] * tile_size:
                return False
        return True

    def run_app(self):
        WIDTH, HEIGHT = self.task.countTiles # количество плиток
        TILE = self.task.tilesSize # размер плитки
        GAME_RES = WIDTH * TILE, HEIGHT * TILE # разрешения экрана
        FPS = 30

        pygame.init()
        screen = pygame.display.set_mode(GAME_RES)
        pygame.display.set_caption('EquilibriumRobot')
        # отрисовка фона
        grid = [pygame.Rect(x * TILE , y * TILE, TILE, TILE ) for x in range(WIDTH) for y in range(HEIGHT)]
        clock = pygame.time.Clock()
        # позиция игрока
        x_player, y_player = self.task.playerPos[0] * TILE, self.task.playerPos[1] * TILE
        count_moves = 0
        # цвета
        player_color = (0,255,0)
        aim_color = (255,0,0)
        grid_color = (40,40,40)
        paint_color = (255, 255, 0)

        len_paints = len(self.task.paintPos)

        while True:
            pressed_keys = pygame.key.get_pressed()
            # поля
            [pygame.draw.rect(screen, grid_color, i_rect, 1) for i_rect in grid]
            # игрок
            pygame.draw.rect(screen,player_color, pygame.Rect(x_player,y_player,TILE, TILE), 0)
            # цель
            pygame.draw.rect(screen, aim_color, pygame.Rect(self.task.pointPos[0] * TILE, self.task.pointPos[1] * TILE,TILE, TILE), 0)
            # стены
            for brickPos in self.task.bricksPos:
                pygame.draw.rect(screen, (128, 128, 128),
                                 pygame.Rect(brickPos[0] * TILE, brickPos[1] * TILE, TILE, TILE), 0)
            # закраски
            for count, paint in enumerate(self.task.paintPos):
                pygame.draw.rect(screen,paint_color,
                                 pygame.Rect(paint[0] * TILE + TILE / 4, paint[1] * TILE + TILE / 4, TILE / 2, TILE / 2), 0)
                if y_player == paint[1] * TILE and x_player == paint[0] * TILE:
                    self.task.paintPos.pop(count)
                    len_paints -= 1
                    print(f'Осталось закрасить {len_paints} ячеек') if len_paints > 0 else print('Ты закрасил последнюю!\n------------------')
            pygame.display.flip()
            clock.tick(FPS)

            # проверка на цель
            if x_player == self.task.pointPos[0] * TILE and y_player == self.task.pointPos[1] * TILE:
                print('Ты выиграл!')
                exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    exit()
                if pressed_keys[pygame.K_w]:
                    try:
                        if not self.is_out_border(x_player, y_player, self.moves[count_moves][0] * TILE, self.moves[count_moves][1] * TILE, GAME_RES, TILE):
                            print('Туда нельзя!')
                        else:
                            x_player += self.moves[count_moves][0] * TILE
                            y_player += self.moves[count_moves][1] * TILE
                    except IndexError:
                        pass

                    count_moves += 1

            screen.fill((0, 0, 0))