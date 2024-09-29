class Cell:
    def __init__(self, state=0):
        self.state = state  # 细胞的状态，0表示空，1表示活细胞
    
    def update(self, neighbors):
        # 依据邻居细胞的状态更新当前细胞状态
        alive_neighbors = sum([n.state for n in neighbors])
        if self.state == 1 and alive_neighbors < 2:  # 模拟孤立死亡
            return 0
        elif self.state == 1 and alive_neighbors > 3:  # 模拟过度拥挤死亡
            return 0
        elif self.state == 0 and alive_neighbors == 3:  # 模拟自复制或繁殖
            return 1
        else:
            return self.state  # 保持原状态

class Grid:
    def __init__(self, rows, cols):
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
    
    def update_grid(self):
        new_grid = [[Cell() for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                # 获取当前细胞的邻居
                neighbors = self.get_neighbors(row, col)
                new_grid[row][col].state = self.grid[row][col].update(neighbors)
        self.grid = new_grid
    
    def get_neighbors(self, row, col):
        # 返回当前细胞的邻居
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0]):
                    neighbors.append(self.grid[new_row][new_col])
        return neighbors
    
    def display(self):
        for row in self.grid:
            print(" ".join([str(cell.state) for cell in row]))

# 使用示例
grid = Grid(5, 5)  # 创建5x5的网格
grid.grid[2][2].state = 1  # 初始化一个活细胞
grid.update_grid()  # 更新网格状态
grid.display()  # 显示网格
