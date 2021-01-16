import pygame


class Robot:
    def __init__(self):
        self.move_items = {
            'Left': (-1, 0),
            'Right': (+1,0),
            'Up': (0,-1),
            'Down': (0,+1),
            'Paint': 'p'
        }

        self.moves = []

    def route_move(self, type_move):
        if type_move == 'end':
            self.run_app()
        self.moves.append(self.move_items[type_move])

    def run_app(self):
        W, H = 10, 10
        TILE = 75
        GAME_RES = W * TILE, H * TILE
        FPS = 5

        pygame.init()
        screen = pygame.display.set_mode(GAME_RES)
        pygame.display.set_caption('EquilibriumRobot')
        grid = [pygame.Rect(x * TILE , y * TILE, TILE, TILE ) for x in range(W) for y in range(H)]
        clock = pygame.time.Clock()
        x, y = 0, 675

        while True:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    exit()

            [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in grid]
            pygame.draw.rect(screen,(0,255,0), pygame.Rect(x,y,75,75), 1)

            pygame.display.flip()
            clock.tick(FPS)

            for count, move in enumerate(self.moves):
                x += move[0] * TILE
                y += move[1] * TILE
                self.moves.pop(count)


            screen.fill((0, 0, 0))




