import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ===================
# Model Data
# ===================
Cube_Vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

Cube_Edges = (
    (0,1), (0,3), (0,4),
    (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7),
    (5,1), (5,4), (5,7)
)

Cube_Surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

Pyramid_Vertices = (
    (1, -1, 1),
    (-1, -1, 1),
    (0, -1, -1),
    (1, 1, 0.5)
)

Pyramid_Edges = (
    (0,1), (0,2), (0,3),
    (2,1), (2,3), (3,1)
)

Pyramid_Surfaces = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
)

Prism_Vertices = (
    (-1, -1, 1),
    (1, -1, 1),
    (0, 1, 1),
    (-1, -1, -1),
    (1, -1, -1),
    (0, 1, -1)
)

Prism_Edges = (
    (0,1), (0,2), (1,2),
    (3,4), (3,5), (4,5),
    (0,3), (1,4), (2,5)
)

Prism_Surfaces = (
    (0, 1, 2),
    (3, 5, 4),

    (0, 1, 4, 3),
    (1, 2, 5, 4),
    (2, 0, 3, 5)
)

# ==========================
# Store models in order
# ==========================
models = [
    ("Cube", Cube_Vertices, Cube_Edges, Cube_Surfaces),
    ("Pyramid", Pyramid_Vertices, Pyramid_Edges, Pyramid_Surfaces),
    ("Prism", Prism_Vertices, Prism_Edges, Prism_Surfaces),
]

current_model_index = 0
render_mode = 0
texture_id = None

# ============================================================
# QUESTION 4 STARTS HERE – TEXTURE SUPPORT (OpenGL.org., 2023; Pygame Community, 2024).
# ============================================================
def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", True)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGB,
        width,
        height,
        0,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        texture_data
    )

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

# ==========================
# Drawing function (sentdex, 2014).
# ==========================
def draw_model(vertices, edges, surfaces):
    # ============================================================
    # QUESTION 4 – TEXTURE MODE (OpenGL.org., 2023; Pygame Community, 2024).
    # ============================================================
    if render_mode == 2:

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        tex_coords = [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)
        ]

        for surface in surfaces:

            if len(surface) == 4:
                glBegin(GL_QUADS)
            else:
                glBegin(GL_TRIANGLES)

            for i, vertex_index in enumerate(surface):
                glTexCoord2fv(tex_coords[i % 4])
                glVertex3fv(vertices[vertex_index])

            glEnd()

        glDisable(GL_TEXTURE_2D)

    # =======================
    # Question 3 (sentdex, 2014).
    # =======================
    elif render_mode == 1:

        colors = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (0, 1, 1),
        ]

        for i, surface in enumerate(surfaces):

            glColor3fv(colors[i % len(colors)])

            # Decide drawing mode based on number of vertices (OpenGL.org., 2023; Pygame Community, 2024).
            if len(surface) == 4:
                glBegin(GL_QUADS)
            elif len(surface) == 3:
                glBegin(GL_TRIANGLES)

            for vertex_index in surface:
                glVertex3fv(vertices[vertex_index])

            glEnd()

    # ============================================================
    # QUESTION 5 – TINTED TEXTURE MODE (OpenGL.org., 2024; Pygame Community, 2024).
    # ============================================================
    elif render_mode == 3:

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        colors = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (0, 1, 1),
        ]

        tex_coords = [
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1)
        ]

        for i, surface in enumerate(surfaces):

            # Tint colour applied to texture (OpenGL.org., 2024; Pygame Community, 2024).
            glColor3fv(colors[i % len(colors)])

            if len(surface) == 4:
                glBegin(GL_QUADS)
            else:
                glBegin(GL_TRIANGLES)

            for j, vertex_index in enumerate(surface):
                glTexCoord2fv(tex_coords[j % 4])
                glVertex3fv(vertices[vertex_index])

            glEnd()

        glDisable(GL_TEXTURE_2D)

    # =======================
    # Question 1 (OpenGL.org., 2023; Pygame Community, 2024).
    # =======================
    glColor3f(1, 1, 1)
    glLineWidth(2.0)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# ==========================
# Main (OpenGL.org., 2023; Pygame Community, 2024).
# ==========================
def main():
    global current_model_index
    global render_mode
    global texture_id

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Q1 - 3D Model Display")

    # Perspective camera (sentdex, 2014).
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # Move camera backwards so it is NOT inside model (sentdex, 2014).
    glTranslatef(0.0, 0.0, -6)

    glEnable(GL_DEPTH_TEST)

    # Load texture
    texture_id = load_texture("img/playboy_frontv.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # Press SPACE to cycle models (OpenGL.org., 2023; Pygame Community, 2024).
                if event.key == pygame.K_SPACE:
                    current_model_index += 1
                    if current_model_index >= len(models):
                        current_model_index = 0

                # =======================
                # Question 2 (sentdex, 2014).
                # =======================
                if event.key == pygame.K_a:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_d:
                    glTranslatef(1, 0, 0)

                if event.key == pygame.K_w:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_s:
                    glTranslatef(0, -1, 0)

                if event.key == pygame.K_q:
                    glTranslatef(0, 0, 1)
                if event.key == pygame.K_e:
                    glTranslatef(0, 0, -1)

                # =======================
                # Question 3 & Question 4 – Toggle render mode (OpenGL.org., 2023; Pygame Community, 2024).
                # =======================
                if event.key == pygame.K_c:
                    render_mode += 1
                    if render_mode > 3:
                        render_mode = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Optional slight rotation for visibility (sentdex, 2014).
        glRotatef(0.5, 2, 1, 0.5)

        name, vertices, edges, surfaces = models[current_model_index]
        draw_model(vertices, edges, surfaces)

        pygame.display.flip()
        pygame.time.wait(10)

main()

"""
    Reference List
    
    OpenGL with PyOpenGL tutorial Python and PyGame p.1 - Making a rotating Cube Example - sentdex. 2014.
    YouTube video, added by sentdex. [online]. Available at: https://youtu.be/R4n4NyDG2hI?si=nUSB8ODfZW_sKL_2
    [Accessed 26 February 2026].
    
    OpenGL with PyOpenGL Python and PyGame p.2 - Coloring Surfaces - sentdex. 2014.
    YouTube video, added by sentdex. [online]. Available at: https://youtu.be/D57J48UAQCs?si=865-fPSR2E7iyyfb
    [Accessed 27 February 2026].
    
    OpenGL with PyOpenGL Python and PyGame p.3 - Movement and Navigation - sentdex. 2014.
    YouTube video, added by sentdex. [online]. Available at: https://youtu.be/cK30eDwVIOI?si=3oLlaF4rt920ohP5
    [Accessed 29 February 2026].
    
    Pygame Community. 2024 Pygame documentation. [online]. Available at: https://www.pygame.org/docs/
    [Accessed 26 February 2026].
    
    OpenGL.org. 2023 PyOpenGL documentation. Available at: http://pyopengl.sourceforge.net/documentation/
    [Accessed 26 February 2026].
    
    OpenGL.org. 2024 Texture mapping. Available at: https://www.opengl.org/wiki/Texture_Mapping
    [Accessed 29 February 2026].   
"""