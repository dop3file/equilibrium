import pygame


class Robot:
    def __init__(self):
        self.move_items = {
            'Left': 'l',
            'Right': 'r',
            'Up': 'u',
            'Down': 'd',
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
        FPS = 30

        pygame.init()
        screen = pygame.display.set_mode(GAME_RES)
        pygame.display.set_caption('EquilibriumRobot')
        grid = [pygame.Rect(x * TILE , y * TILE, TILE, TILE ) for x in range(W) for y in range(H)]
        clock = pygame.time.Clock()

        while True:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
                    exit()

            [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in grid]
    
            pygame.display.flip()
            clock.tick(FPS)


