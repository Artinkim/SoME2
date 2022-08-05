from manim import *
import numpy as np
from utils import ChangingMatrix
# size = (2, 2)
#         bounds = (-10, 10)
#         iterations = 100
#         arr = [[[np.round(bounds[0]+(bounds[1]-bounds[0])*np.random.random(), decimals=2) for y in range(size[1])] for x in range(size[0])] for _ in range(iterations)]
        
#         m = arr.pop()
#         eq = MathTex("trace(M) = " + str(np.round(np.trace(m), decimals=2)))
#         mg = Group(MathTex("M = "), Matrix(m, h_buff=1.6))

#         g = Group(mg.arrange(), eq).arrange(direction=DOWN)
#         self.add(g)
        
#         eq2 = MathTex("det(M) = " + str(np.round(np.linalg.det(m), decimals=2))).move_to(eq)
#         self.play(TransformMatchingShapes(eq, eq2))
#         g = Group(mg.arrange(), eq2).arrange(direction=DOWN)
        
#         total, n = np.round(np.linalg.det(m), decimals=2), 1
#         averageEq = MathTex("Average = " + str(np.round(total/n, decimals=2)))

#         g2 = Group(Group(MathTex("M = "), Matrix(m, h_buff=1.6)).arrange(), eq2.copy(), averageEq.copy()).arrange(direction=DOWN)
#         self.remove(eq2, mg)
#         self.play(TransformMatchingShapes(g, g2))
#         self.remove(g2)
        
#         # ensemble = [Group]
#         for i in range(10):
#             self.wait(0.5)
#             self.remove(g2)
#             m = arr.pop()
#             eq2 = MathTex("det(M) = " + str(np.round(np.linalg.det(m), decimals=2)))
#             total += np.round(np.linalg.det(m), decimals=2)
#             n += 1
#             averageEq = MathTex("Average = " + str(np.round(total/n, decimals=2)))
#             g2 = Group(Group(MathTex("M = "), Matrix(m, h_buff=1.6)).arrange(), eq2, averageEq).arrange(direction=DOWN)
#             self.add(g2)
        
#         # t = ValueTracker(0)
#         # g = Group()
#         # self.add(g)
#         # g.add_updater(lambda g: g.become(ensemble[int(t.get_value())]))
#         # self.play(t.animate.set_value(9))
        
#         self.wait(5)



class EnsembleAverage(Scene):
    def construct(self):
        size, bounds = (2, 2), (-10, 10)
        iterations = 100
        matricies = [np.round(bounds[0]+(bounds[1]-bounds[0])*np.random.rand(size[0], size[1]), decimals=2) for _ in range(iterations)]
        t = ValueTracker(0)
        matrix = ChangingMatrix(matricies,t)

        matrixLabel = MathTex("M = ").next_to(matrix, direction=LEFT)
        self.add(matrix, matrixLabel)
        
        matrix_21 = matrix.nums[1][0]
        eq = MathTex("M_{21} = ").next_to(matrix, direction=DOWN)
        self.add(eq)
        self.play(matrix_21.copy().move_to(matrix_21).animate.next_to(eq))



        self.wait(5)