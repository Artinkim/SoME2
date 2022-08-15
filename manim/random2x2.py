from manim import *
import numpy as np
class RadomMatrix(MobjectMatrix):
    
    def __init__(self, size, bounds, precision, vt):
        self.size = size
        self.bounds = bounds
        self.precision = precision
        self.nums = [[DecimalNumber() for _ in range(self.size[1])] for __ in range(self.size[0])]
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.nums[x][y].add_updater(lambda d: d.set_value(np.round(vt.get_value()*0+self.bounds[0]+(self.bounds[1]-self.bounds[0])*np.random.random(), decimals=self.precision)))

        super().__init__(self.nums, h_buff=2, element_alignment_corner=DR)
class Intro(Scene):
    def construct(self):
        vt = ValueTracker(0)
        self.add(RadomMatrix((3,3),(-5,5),2,vt))
        self.play(vt.animate.set_value(1),run_time=5)