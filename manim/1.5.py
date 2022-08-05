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
        
        test = -1
        while test < 0:
            matrix = ChangingMatrix(matricies,t)
            test = matrix.nums[1][1].get_value()
        numsV = [[matrix.nums[x][y].get_value() for y in range(len(matrix.nums[0]))] for x in range(len(matrix.nums))]

        matrixLabel = MathTex("M = ").next_to(matrix, direction=LEFT)
        self.add(matrix, matrixLabel)
        nums = [[MathTex(str(matrix.nums[x][y].get_value())).move_to(matrix.nums[x][y]) for y in range(len(matrix.nums[0]))] for x in range(len(matrix.nums))]
        
        entryEq = MathTex("M_{11} = ").next_to(matrix, direction=DOWN).shift(LEFT*2.5)
        self.play(nums[0][0].animate.next_to(entryEq), FadeIn(entryEq, scale=1.5))
        self.wait(1)

        traceEq = MathTex("trace(M) = ").move_to(entryEq, aligned_edge=LEFT)
        tracePlus = MathTex(" + ").next_to(nums[0][0].copy().next_to(traceEq))
        self.play(nums[0][0].animate.next_to(traceEq), nums[1][1].animate.next_to(tracePlus), Transform(entryEq, traceEq), FadeIn(tracePlus, scale=1.5))
        self.wait(0.5)
        trace = MathTex(str(np.round(np.trace(numsV), decimals=2))).next_to(traceEq)
        traceRight = Group(nums[0][0], tracePlus, nums[1][1])
        self.play(Transform(traceRight, trace))
        self.wait(1)
        self.remove(entryEq)

        detEq = MathTex("det(M) = ").move_to(entryEq, aligned_edge=LEFT)
        nums = [[MathTex(str(matrix.nums[x][y].get_value())).move_to(matrix.nums[x][y]) for y in range(len(matrix.nums[0]))] for x in range(len(matrix.nums))]
        detRight = MathTex("(", nums[0][0].get_tex_string(), "*", nums[1][1].get_tex_string(), ") - (", nums[0][1].get_tex_string(), "*", nums[1][0].get_tex_string(), ")").next_to(detEq)
        self.play(FadeOut(traceRight, scale = 0.5), Transform(traceEq, detEq), TransformMatchingTex(Group(*nums[0], *nums[1]), detRight))
        self.wait(0.5)
        det = MathTex(str(np.round(np.linalg.det(numsV), decimals=2))).next_to(detEq)
        self.play(Transform(detRight, det))

        self.wait(5)