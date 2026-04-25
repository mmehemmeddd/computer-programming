# import pygame
# import random
# import sys
# pygame.init()
# screen = pygame.display.set_mode((400, 600))
# pygame.display.set_caption("Quw oyunu")
# clock = pygame.time.Clock()
# def reset_game():
#     return 300, 0, [[400, random.randint(200, 500)]], 0, False
#
#
# bird_y, bird_velocity, pipes, score, game_over = reset_game()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             if game_over:
#                 bird_y, bird_velocity, pipes, score, game_over = reset_game()
#             else:
#                 bird_velocity = -8
#
#     screen.fill((135, 206, 250))
#
#     if not game_over:
#         bird_velocity += 0.5
#         bird_y += bird_velocity
#         bird_rect = pygame.Rect(50, int(bird_y), 30, 30)
#         pygame.draw.ellipse(screen, (255, 215, 0), bird_rect)
#
#         if bird_y > 600 or bird_y < 0:
#             game_over = True
#
#         for pipe in pipes:
#             pipe[0] -= 4
#             top_pipe = pygame.Rect(pipe[0], 0, 50, pipe[1] - 150)
#             bottom_pipe = pygame.Rect(pipe[0], pipe[1], 50, 600 - pipe[1])
#             pygame.draw.rect(screen, (34, 139, 34), top_pipe)
#             pygame.draw.rect(screen, (34, 139, 34), bottom_pipe)
#
#             if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
#                 game_over = True
#
#             if pipe[0] == 46:
#                 score += 1
#
#         if pipes[-1][0] < 200:
#             pipes.append([400, random.randint(200, 500)])
#         if pipes[0][0] < -50:
#             pipes.pop(0)
#
#         font = pygame.font.SysFont(None, 60)
#         score_text = font.render(str(score), True, (255, 255, 255))
#         screen.blit(score_text, (200 - score_text.get_width() // 2, 50))
#     else:
#         font_large = pygame.font.SysFont(None, 60)
#         font_small = pygame.font.SysFont(None, 36)
#         text_game_over = font_large.render("Oyun Bitdi!", True, (255, 0, 0))
#         text_restart = font_small.render("Yeniden baslamaq ucun SPACE bas", True, (0, 0, 0))
#         text_score = font_small.render(f"Xal: {score}", True, (0, 0, 0))
#
#         screen.blit(text_game_over, (200 - text_game_over.get_width() // 2, 200))
#         screen.blit(text_score, (200 - text_score.get_width() // 2, 260))
#         screen.blit(text_restart, (200 - text_restart.get_width() // 2, 320))
#
#     pygame.display.update()
#     clock.tick(60)
import math
def kub_are(a):
    return a**3