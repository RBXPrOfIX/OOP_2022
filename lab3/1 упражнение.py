import pygame
# Инициализирую pygame
pygame.init()

# Устанавливаю размеры окна
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Злой смайлик')

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Размеры и позиции
face_x, face_y = screen_width // 2, screen_height // 2
face_radius = 100
eye_radius = 15
eye_offset_x, eye_offset_y = 30, 30
eye_brow_length = 50
eye_brow_thickness = 5
mouth_length = 60
mouth_thickness = 10  

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Закрашиваю фон
    screen.fill(WHITE)

    # Рисую лицо
    pygame.draw.circle(screen, YELLOW, (face_x, face_y), face_radius)

    # Рисую глаза
    pygame.draw.circle(screen, RED, (face_x - eye_offset_x, face_y - eye_offset_y), eye_radius)
    pygame.draw.circle(screen, RED, (face_x + eye_offset_x, face_y - eye_offset_y), eye_radius)
    pygame.draw.circle(screen, BLACK, (face_x - eye_offset_x, face_y - eye_offset_y), eye_radius // 2)
    pygame.draw.circle(screen, BLACK, (face_x + eye_offset_x, face_y - eye_offset_y), eye_radius // 2)

    # Рисую брови
    pygame.draw.line(screen, BLACK, (face_x - eye_offset_x - eye_brow_length / 2, face_y - eye_offset_y - eye_brow_thickness * 4),
                     (face_x - eye_offset_x + eye_brow_length / 2, face_y - eye_offset_y - eye_brow_thickness * 2), eye_brow_thickness)
    pygame.draw.line(screen, BLACK, (face_x + eye_offset_x - eye_brow_length / 2, face_y - eye_offset_y - eye_brow_thickness * 2),
                     (face_x + eye_offset_x + eye_brow_length / 2, face_y - eye_offset_y - eye_brow_thickness * 4), eye_brow_thickness)

    # Рисую рот
    pygame.draw.rect(screen, BLACK, (face_x - mouth_length // 2, face_y + eye_offset_y + mouth_thickness // 2,
                                     mouth_length, mouth_thickness))

    # Обновляю экран
    pygame.display.update()

# Закрываю pygame
pygame.quit()


