import random
import os
import time

class Game:
    def __init__(self, width = 20, height = 20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    def CreateGrid(self):
        self.grid = [[random.choice([0,1]) for _ in range(self.width)] for _ in range(self.height)]

    def DisplayGrid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(" ".join(["x" if cell else "." for cell in row]))

    def neighbours(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i ==0 and j == 0:
                    continue
                nx, ny = x+i, y+j
                if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height:
                    count += self.grid[nx][ny]
        return count

    def evolution(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                sasiad = self.neighbours(x,y)
                if self.grid[x][y] == 1:
                    if sasiad in [2,3]:
                        new_grid[x][y] = 1
                else:
                    if sasiad == 3:
                        new_grid[x][y] = 1
        self.grid = new_grid

    def main(self):
        try:
            while True:
                self.DisplayGrid()
                self.evolution()
                time.sleep(1)
        except KeyboardInterrupt:
            print("Koniec")

if __name__ == '__main__':
    game = Game(20, 20)
    game.CreateGrid()
    game.main()