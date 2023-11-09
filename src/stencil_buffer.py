import pygame
from OpenGL.GL import *
from drawing import draw_sphere, draw_tetrahedron

def stencil_buffer_example():
    """
        Использует буфер трафарета для отрисовки фигуры "тетраэдр минус сфера" с помощью библиотеки Pygame и OpenGL.

        Описание:
        Функция stencil_buffer_example инициализирует буфер трафарета и устанавливает необходимые
        параметры для его использования. Затем она входит в бесконечный цикл, в котором обрабатывает
        события Pygame такие как нажатия клавиш и закрытие окна. Клавиши "стрелка влево" и "стрелка вправо"
        вращают отображаемые объекты вокруг вертикальной оси, а клавиши "стрелка вверх" и "стрелка вниз"
        вращают их вокруг горизонтальной оси. Внутри цикла происходит очистка буфера трафарета, установка
        параметров буфера трафарета и вызов функций draw_tetrahedron и draw_sphere для отрисовки тетраэдра и
        сферы соответственно. Причем сначала нарисованный тетраэдр помещается в буфер трафарета с маской 1,
        а затем нарисованная сфера помещается в буфер трафарета с маской 2. Затем с помощью буфера трафарета
        рисуется только тот объект, который находится в области с маской 1, что создает эффект "обрезания"
        тетраэдра сферой. Затем происходит обновление экрана Pygame и задержка для синхронизации кадров.

    """
    rotation_speed = 5.0
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_STENCIL_TEST)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(-rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_UP:
                    glRotatef(rotation_speed, -1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(-rotation_speed, -1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)

        glStencilFunc(GL_ALWAYS, 1, 0)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        draw_tetrahedron()

        glStencilFunc(GL_ALWAYS, 2, 0)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        draw_sphere(0.85)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glStencilFunc(GL_EQUAL, 1, 255)
        draw_tetrahedron()

        pygame.display.flip()
        pygame.time.wait(10)
