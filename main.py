import random
import time

class Cell:
    def __init__(self, state=0):
        self.state = state  # 0表示空，1表示活细胞
    
    def update(self, neighbors):
        # 根据邻居的状态更新当前细胞状态
        alive_neighbors = sum([n.state for n in neighbors])
        if self.state == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
            # 活细胞死亡
            return 0
        elif self.state == 0 and alive_neighbors == 3:
            # 空细胞变为活细胞
            return 1
        else:
            # 保持不变
            return self.state

class Grid:
    def __init__(self, rows, cols):
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
    
    def random_initialize(self):
        # 随机初始化网格，生成活细胞
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].state = random.choice([0, 1])

    def update_grid(self):
        # 更新整个网格状态
        new_grid = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.get_neighbors(row, col)
                new_grid[row][col].state = self.grid[row][col].update(neighbors)
        self.grid = new_grid
    
    def get_neighbors(self, row, col):
        # 获取邻居细胞
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    neighbors.append(self.grid[new_row][new_col])
        return neighbors
    
    def display(self):
        # 打印网格状态
        for row in self.grid:
            print(" ".join([str(cell.state) for cell in row]))
        print("\n" + "-" * 20 + "\n")

# 使用示例
def run_simulation(steps=10, rows=10, cols=10):
    grid = Grid(rows, cols)
    grid.random_initialize()  # 随机初始化网格
    for step in range(steps):
        print(f"Step {step + 1}:")
        grid.display()
        grid.update_grid()
        time.sleep(1)  # 暂停一秒，模拟时间流逝

# 运行模拟
run_simulation(steps=15, rows=10, cols=10)
