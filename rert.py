import math
import random
import pygame
from Vec2d import Vec2d
pygame.init()

done = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
size = 800
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption("Path Following")
clock = pygame.time.Clock()


class Tree:
    def __init__(self, point, preset):
        self.nodes = [Node(point)]
        self.preset = preset

    def create_new_node(self):
        while True:
            p = Vec2d(random.randint(1, size - 1), random.randint(1, size - 1))
            got_new = True
            for node in self.nodes:
                if node.pos.distance(p) < self.preset:
                    got_new = False
                    break
            if got_new:
                break
        smallest = self.nodes[0].pos.distance(p)
        smallest_node = self.nodes[0]
        for node in self.nodes[1:]:
            if node.pos.distance(p) < smallest:
                smallest = node.pos.distance(p)
                smallest_node = node

        x = p.sub_vect(smallest_node.pos)
        x.set_mag(self.preset)
        self.nodes.append(Node(smallest_node.pos.add_vect(x)))
        smallest_node.neighbours.append(self.nodes[-1])
        self.nodes[-1].neighbours.append(smallest_node)

    def show_tree(self):
        for node in self.nodes:
            node.show_lines()


class Node:
    def __init__(self, point):
        self.pos = point
        self.neighbours = []

    def show_lines(self):
        for neighbour in self.neighbours:
            pygame.draw.line(screen, WHITE, [self.pos.x, self.pos.y], [neighbour.pos.x, neighbour.pos.y])


tree = Tree(Vec2d(random.randint(1, size-1), random.randint(1, size-1)), 20)
while not done:
    clock.tick(20)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tree.create_new_node()
    tree.show_tree()
    pygame.display.flip()

pygame.quit()
