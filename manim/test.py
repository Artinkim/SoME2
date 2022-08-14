from manim import *

class Test(Scene):
    def construct(self):
        np.random.seed(1)
        size=(5,5)
        bounds=(-10,10)
        array1 = np.random.uniform(*bounds,size=size)
        array2 = np.random.uniform(*bounds,size=size)
        array1 = np.tril(array1.T) + np.triu(array1, 1)
        array2 = np.tril(array2.T,-1) + np.triu(array2*-1, 1)
        symetric_conj = [[str(int(array1[x][y]))+("+"*(int(array2[x][y])>=0)+str(int(array2[x][y]))+"i")*(x!=y) for y in range(size[1])] for x in range(size[0])]
        complex_symetric_matrix = Matrix(symetric_conj, h_buff = 2.6).shift(DOWN).scale(0.5)
        #self.play(Wiggle(complex_symetric_matrix.get_entries()[2]))
        prob_info1 = MathTex("a+bi")
        prob_info2 = MathTex(" \sim P(M_{ij})").next_to(prob_info1,RIGHT)
        eigen_list = MathTex("(\\lambda_{1}, \\lambda_{2}, \\ldots, \\lambda_{N})").next_to(prob_info1,DOWN).shift(LEFT*2)
        energy_lsit = MathTex(" \sim (E_{1}/S_{1}, E_{2}/S_{2}, \\ldots, E_{N}/S_{N})").next_to(eigen_list,RIGHT)
        self.play(Write(prob_info1))
        self.wait(1)
        self.play(Write(prob_info2))
        self.wait(1)
        self.play(Write(eigen_list))
        self.wait(1)
        self.play(Write(energy_lsit))
        self.wait(1)
        