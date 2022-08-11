from manim import *
from functools import partial

# links:
# https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf

class Functor:
    x: int
    y: int
    matrix: np.array
    vt: ValueTracker
    
    def __init__(self, x, y, matrix, vt):
        self.x, self.y, self.matrix, self.vt = x, y, matrix, vt
    
    def __call__(self, d):
        d.set_value(self.matrix[int(self.vt.get_value())][self.x][self.y])

class ChangingMatrix(MobjectMatrix):
    def __init__(self, matrix, vt):
        self.size = [len(matrix[0]),len(matrix[0][0])]
        self.nums = [[DecimalNumber() for x in range(self.size[1])] for y in range(self.size[0])]      
         
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                # self.nums[x][y].add_updater(partial(lambda d: d.set_value(matrix[int(vt.get_value())][x][y]), x, y, matrix, vt))
                self.nums[x][y].add_updater(Functor(x, y, matrix, vt))

        super().__init__(self.nums, h_buff=2)
        self.update()