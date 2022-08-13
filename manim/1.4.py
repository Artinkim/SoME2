from functools import cache
from manim import *
import numpy as np
import string

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
        
def fade_lower_triangle(matrix):
    n2 = len(matrix.get_entries())
    n = int(n2**(1/2))
    entries = [matrix.get_entries()[i:i+n] for i in range(0,n2,n)]
    for i in range(n):
        for j in range(n):
            if i>j:
                entries[i][j].set_opacity(0.25)
    return matrix

class RandomMatrix(Scene):
    totalChanges = 10

    def construct(self):
        np.random.seed(1)
        vt = ValueTracker(0)
        
        m = []
        size = (2, 2)
        bounds = (1, 10)
        m.append(MobjectMatrix([[DecimalNumber(np.round(np.random.uniform(*bounds), decimals=2)) for y in range(size[1])] for x in range(size[0])], h_buff = 1.6))
        m.append(MobjectMatrix([[MathTex("Gaussian(\mu,\sigma)") for y in range(size[1])] for x in range(size[0])], h_buff = 3.5))
        m.append(MobjectMatrix([[MathTex("Uniform (a,b)") for y in range(size[1])] for x in range(size[0])], h_buff = 3.5))
        signs = [" + ", " - "]
        m.append(MobjectMatrix([[MathTex(str(int(m[0][0][size[1]*x+y].get_value()))+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"i") for y in range(size[1])] for x in range(size[0])], h_buff = 2.6))
        m.append(MobjectMatrix([[MathTex(m[-1][0][size[1]*x+y].tex_string+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"j"+np.random.choice(signs)+str(np.random.randint(low=bounds[0], high=bounds[1]))+"k") for y in range(size[1])] for x in range(size[0])], h_buff = 4.6))
        m.append(MobjectMatrix([[MathTex(m[-1][0][size[1]*x+y].tex_string+np.random.choice(signs)+"...") for y in range(size[1])] for x in range(size[0])], h_buff = 5.4))
        m.append(MobjectMatrix([
            [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1P}")],
            [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2P}")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NP}")]], h_buff = 1.6))
        m.append(MobjectMatrix([
            [MathTex("M_{11}"), MathTex("M_{12}"), MathTex("..."), MathTex("M_{1N}")],
            [MathTex("M_{21}"), MathTex("M_{22}"), MathTex("..."), MathTex("M_{2N}")],
            [MathTex(), MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("M_{N1}"), MathTex("M_{N2}"), MathTex("..."), MathTex("M_{NN}")]], h_buff = 1.6))
        size = (5, 5)
        bounds = (-10, 10)
        m.append(DecimalMatrix(np.round(np.random.uniform(*bounds,size=size), decimals=2), h_buff = 1.6))
        m.append(RadomMatrix(size=size, bounds=bounds, precision=2, vt=vt))
        
        # scale matricies then add first matrix to the scene
        for x in m:
            x.scale(0.5)
        a = m[0].copy()
        self.add(a)
        self.wait(1)
        
        # # initialize axis and graphs for the two distributions
        axes1 = Axes(x_range=[-5,6,1], y_range=[0,1.1, 0.2]).scale(0.5).add_coordinates().scale(0.5).move_to(UL*2+LEFT*2)
        axes1.add(Tex("0").scale(0.4).next_to(axes1.x_axis.n2p(0), DOWN*0.5))
        guas = axes1.plot(lambda x: np.exp(-(x/3)**2),color=BLUE)
        guas_area = axes1.get_area(guas)
        axes2 = axes1.copy().next_to(axes1)
        uniform = axes2.plot(lambda x: 1 if x>-3 and x<3 else 0, discontinuities=[-3,3], color=GREEN)
        uniform_area = axes2.get_area(uniform)

        # # play chaning the matrix and showing distributions
        self.play(Transform(a, m[1]),Create(axes1),Create(guas),run_time=1)
        self.play(FadeIn(guas_area))
        self.wait(1)
        self.play(Transform(a, m[2]),Transform(axes1,axes2,rate_function=lingering),Create(uniform,rate_func=rush_into),run_time=1)
        self.play(FadeIn(uniform_area))
        self.wait(1)
        
        # # create list of element types matrix can hold
        element_types = VGroup(
            MathTex("a"),
            MathTex("a + bi"),
            MathTex("{\displaystyle a+b\ \mathbf {i} +c\ \mathbf {j} +d\ \mathbf {k} }"),
            MathTex("{\displaystyle a+b\ \mathbf {i} +c\ \mathbf {j} +d\ \mathbf {k} }","...")
        ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.75).next_to(axes1)

        # # play changing the matrix and showing element types
        self.play(Transform(a, m[0]), FadeOut(axes1), FadeIn(element_types[0]))
        self.wait(1)
        self.play(Transform(a, m[3]), FadeIn(element_types[1]))
        self.play(Transform(a, m[4]), FadeIn(element_types[2]))
        self.play(Transform(a, m[5]), FadeIn(element_types[3]))
        self.wait(1)

        # # shows sizes of matrices 
        b = Brace(m[6])
        b1tex, b2tex = b.get_tex("N\\text{x}P"), b.get_tex("N\\text{x}N") 
        self.play(Transform(a, m[6]),FadeIn(b,b1tex))
        self.wait(1)
        self.play(Transform(a, m[7]), Transform(b1tex, b2tex))
        self.wait(1)
        
        # # show specific case of matrix 5x5 (-10,10)
        axes3 = Axes(x_range=[-12,13,2], y_range=[0,1.1, 0.2]).scale(0.5).add_coordinates().scale(0.5).move_to(UL*2+LEFT)
        axes3.add(Tex("0").scale(0.4).next_to(axes3.x_axis.n2p(0), DOWN*0.5))
        uniformN = axes3.plot(lambda x: 1 if x>-10 and x<10 else 0, discontinuities=[-10,10], color=GREEN)
        uniform_areaN = axes3.get_area(uniformN)
        integer_tex = element_types.submobjects[0]
        integer_texN = integer_tex.copy().next_to(axes3).shift(RIGHT)
        element_types.remove(integer_tex)
        self.play(
            Transform(a, m[8]),
            FadeOut(guas,guas_area,b,b1tex),
            ReplacementTransform(uniform,uniformN),
            ReplacementTransform(uniform_area,uniform_areaN),
            FadeIn(axes3),
            FadeOut(*element_types.submobjects),
            ReplacementTransform(integer_tex,integer_texN),
        )
        integer_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(1.8,0.8),color=YELLOW)
        entry_equals_tex = MathTex("M_{ij} = ").scale(0.5).next_to(integer_texN,LEFT)
        self.play(Create(integer_arrow))
        self.play(Create(entry_equals_tex))
        self.wait(1)

        # # cycles through random matricies, moving arrow along distribution
        self.remove(a)
        a = m[9].copy()
        self.add(a)
        integer_arrow_copy = integer_arrow.copy()
        left_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(-10,0.8),color=YELLOW)
        right_arrow = CurvedArrow(integer_texN.get_center(),axes3.c2p(10,0.8),color=YELLOW)
        self.play(vt.animate.set_value(0.3), ReplacementTransform(integer_arrow,left_arrow), run_time=2)
        self.play(vt.animate.set_value(0.6), ReplacementTransform(left_arrow,right_arrow), run_time=2)
        self.play(vt.animate.set_value(1), ReplacementTransform(right_arrow,integer_arrow_copy), run_time=2)
        self.play(FadeOut(integer_arrow_copy))

        # show creation of 3 matricies then puts into row
        self.remove(a) 
        m_group = VGroup()
        original_vals = np.round(np.random.uniform(*bounds,size=(3,*size)), decimals=2)
        for i in range(3):
            temp = DecimalMatrix(original_vals[i], h_buff = 1.6).scale(0.5)
            self.add(temp)
            self.wait(0.25)
            self.play(temp.animate.scale(0.4).move_to(LEFT * 2*(1-i) + DOWN * 1.5))
            self.wait(0.25)
            m_group.add(temp)

        # show ensemble as collection of 3 previously created matricies
        m_sub = m_group.submobjects
        left_brace, right_brace = MathTex("\\{").scale(1.7), MathTex("\\}").scale(1.7)
        ensemble = VGroup(MathTex("ensemble: "), left_brace, m_sub[0].copy(), m_sub[1].copy(), MathTex("..."), m_sub[2].copy(), right_brace).arrange(RIGHT)
        self.play(TransformMatchingShapes(m_group, ensemble)) # tries tranforming all submobjects to ones in other group that match??? tranforming matching shapes does not work like normal transfrom method
        self.wait(1)

        # transform ensemble into single decimal matrix
        a = DecimalMatrix(original_vals[0], h_buff = 1.6).scale(0.5)
        self.play(TransformMatchingShapes(ensemble,a))
        self.wait(1)
        

        #transform matrix into list on entries then back
        entries = a.copy().get_entries()
        left_brace, right_brace = MathTex("["), MathTex("]")
        decimal_list = VGroup(*[left_brace,*entries[:3], MathTex("..."), *entries[-2:],right_brace]).arrange(RIGHT)
        self.play(TransformMatchingShapes(a,decimal_list))
        self.wait(1)
        self.play(TransformMatchingShapes(decimal_list,a))
        
        #cycle through entries and show that they are drawn independently from the distribution 
        independent_tex1 = MathTex("p(M)","=","p(M_{11})p(M_{12})...p(M_{NN})").scale(0.5).next_to(a,RIGHT)
        independent_tex2 = MathTex("p(M)","=","\prod_{ij=1}^{N} M_ {ij}").scale(0.5).next_to(a,RIGHT)
        dependent_tex = MathTex("p(M)","\\neq","\prod_{ij=1}^{N} M_{ij}").scale(0.5).next_to(a,RIGHT)
        symetric_tex =  MathTex("p(M)","=","\prod_{indep ij} M_{ij} = \prod_{i} M_{ii}\prod_{i>j} M_{ij}").scale(0.5).next_to(a,RIGHT)
        prev_arrow = Mobject()
        for i in range(25):
            curr_arrow = CurvedArrow(a.get_entries()[i].get_center(),axes3.c2p(a.get_entries()[i].get_value(),0.8),color=YELLOW)
            self.play(
                ShowPassingFlash(SurroundingRectangle(a.get_entries()[i]),time_width=1),
                FadeOut(prev_arrow),
                Create(curr_arrow), 
                run_time = 0.1 if 2<i and i<22 else 0.5)
            prev_arrow = curr_arrow
            if i == 2:  
                self.play(Write(independent_tex1),run_time=0.5)
            if i == 22:
                self.play(TransformMatchingTex(independent_tex1,independent_tex2),run_time=0.5)
        self.play(FadeOut(prev_arrow))

        # show physical system is not independent
        ps = Tex("PYS SYSTM").move_to(LEFT*3)
        self.play(FadeIn(ps),run_time=0.5)
        self.play(TransformMatchingTex(independent_tex2,dependent_tex))
        self.play(Indicate(dependent_tex.get_part_by_tex("\\neq"), scale_factor=3, color=RED),FadeOut(entry_equals_tex,integer_texN))
        self.wait(1)
        self.play(FadeOut(ps),run_time=0.5)

        # show defenition of symetric matrix with two matching entries
        entries = [a.get_entries()[i:i+5] for i in range(0,25,5)]
        rect1_start = SurroundingRectangle(entries[0][0])
        rect1_middle = SurroundingRectangle(entries[0][3])
        rect1_end = SurroundingRectangle(entries[1][3])

        rect2_start = SurroundingRectangle(entries[0][0])
        rect2_middle = SurroundingRectangle(entries[3][0])
        rect2_end = SurroundingRectangle(entries[3][1])
        
        self.play(Create(rect1_start))
        self.play(ReplacementTransform(rect1_start,rect1_middle))
        self.play(ReplacementTransform(rect1_middle,rect1_end))

        self.play(Create(rect2_start))
        self.play(ReplacementTransform(rect2_start,rect2_middle))
        self.play(ReplacementTransform(rect2_middle,rect2_end))

        changed_num = entries[3][1].copy().set_value(entries[1][3].get_value())
        self.play(Transform(entries[3][1],changed_num),Transform(rect2_end,SurroundingRectangle(changed_num)))
        self.wait(1)
        
        # transform into fully systmetric matrix
        sysmetric_matrix = DecimalMatrix(np.tril(original_vals[0].T) + np.triu(original_vals[0], 1)).scale(0.5)
        self.play(ReplacementTransform(a,sysmetric_matrix),TransformMatchingTex(dependent_tex,symetric_tex),FadeOut(rect1_end,rect2_end))
        self.wait(1)

        # fadeout symetric entry values (lower triangular section)
        sysmetric_matrix_faded = fade_lower_triangle(sysmetric_matrix.copy())
        self.play(ReplacementTransform(sysmetric_matrix,sysmetric_matrix_faded))
        self.wait(1)

        # show vector of random variables and covariance between then in matrix
        x_list = MathTex("X"," = ","(","x_{1}",",","x_{2}",",","x_{3}",",","...",",","x_{N}",")").next_to(a,UP).shift(UP)
        C_def = MathTex("C_{ij}(X) "," \equiv ","cov(x_i,x_j)").next_to(x_list,DOWN)
        self.play(Write(x_list),FadeOut(axes3,uniform_areaN,uniformN))
        self.wait(1)
        cov_matrix = MobjectMatrix([
            [MathTex("C(x_{1},x_{1})"), MathTex("C(x_{1},x_{2})"), MathTex("C(x_{1},x_{3})"), MathTex("..."), MathTex("C(x_{1},x_{N})")],
            [MathTex("C(x_{2},x_{1})"), MathTex("C(x_{2},x_{2})"),MathTex("C(x_{2},x_{3})"), MathTex("..."), MathTex("C(x_{2},x_{N})")],
            [MathTex("C(x_{3},x_{1})"), MathTex("C(x_{3},x_{2})"), MathTex("C(x_{3},x_{3})"), MathTex("..."), MathTex("C(x_{3},x_{N})")],
            [MathTex(), MathTex(),MathTex(), MathTex("\ddots"), MathTex()],
            [MathTex("C(x_{N},x_{1})"), MathTex("C(x_{N},x_{2})"), MathTex("C(x_{N},x_{3})"), MathTex("..."), MathTex("C(x_{N},x_{N})")]
            ], h_buff = 2.5).scale(0.5)
        self.play(Write(C_def),ReplacementTransform(sysmetric_matrix_faded,cov_matrix),symetric_tex.animate.next_to(C_def,RIGHT))
        self.wait(1)

        # show covariance has symetric property with CurvedArrows
        arrow1 = CurvedArrow(x_list.submobjects[3].get_center(),x_list.submobjects[7].get_center(),color=YELLOW)
        arrow2 = CurvedArrow(x_list.submobjects[7].get_center(),x_list.submobjects[3].get_center(),color=YELLOW)
        self.play(
            ShowPassingFlash(SurroundingRectangle(cov_matrix.get_entries()[2]),time_width=0.5),
            Create(arrow1,rate_func=lingering),
            run_time=2)
        self.play(FadeOut(arrow1))
        self.play(
            ShowPassingFlash(SurroundingRectangle(cov_matrix.get_entries()[10]),time_width=0.5),
            Create(arrow2,rate_func=lingering),
            run_time=2)
        self.play(FadeOut(arrow2))
        self.wait(1)

        # write equivalency tex 
        equivalent1 = MathTex("cov(a,b) = cov(b,a)").next_to(a,DOWN)
        equivalent2 = MathTex("X_{ij} = X_{ji}").next_to(equivalent1,DOWN)
        self.play(Write(equivalent1))
        self.wait(0.5)
        self.play(ReplacementTransform(equivalent1.copy(),equivalent2))

        # fadeout covariance entry values (lower triangular section)
        cov_matrix_faded = fade_lower_triangle(cov_matrix.copy())
        self.play(ReplacementTransform(cov_matrix,cov_matrix_faded),FadeOut(equivalent1),equivalent2.animate.move_to(equivalent1))
        self.wait(1)

        # change to quantum matrix with states
        H_def = VGroup(MathTex("H_{ij}"),Tex("\\textasciitilde"),VGroup(Tex("Encodes probablility to"),Tex("transition from state"),Tex("i $\\leftarrow$ j in a small time j}")).arrange(DOWN)).arrange(RIGHT).move_to(x_list).shift(LEFT*2)
        ham_matrix = MobjectMatrix([
            [MathTex("(1 -> 1"), MathTex("(1 -> 2)"), MathTex("(1 -> 3)"), MathTex("...   "), MathTex("(1 -> N)")],
            [MathTex("(2 -> 1)"), MathTex("(2 -> 2)"),MathTex("(2 -> 3)"), MathTex("...  "), MathTex("(2 -> N)")],
            [MathTex("(3 -> 1)"), MathTex("(3 -> 2)"), MathTex("(3 -> 3)"), MathTex("...  "), MathTex("(3 -> N)")],
            [MathTex(), MathTex(), MathTex(), MathTex("\ddots  "), MathTex()],
            [MathTex("(N -> 1)"), MathTex("(N -> 2)"), MathTex("(N -> 3)"), MathTex("...  "), MathTex("(N -> N)")]
            ], h_buff = 2.5).scale(0.5)
        faded_ham_matrix = fade_lower_triangle(ham_matrix.copy())
        self.play(FadeOut(x_list),ReplacementTransform(C_def,H_def),Write(H_def),ReplacementTransform(cov_matrix_faded,faded_ham_matrix))
        self.wait(1)
        
        #generate a 5x5 matrix of symetric complex conjugates
        equivalent_Complex = MathTex("H_{ij}"," = ","H_{ij}^{*}").move_to(equivalent2)
        array1 = np.random.uniform(*bounds,size=size)
        array2 = np.random.uniform(*bounds,size=size)
        array1 = np.tril(array1.T) + np.triu(array1, 1)
        array2 = np.tril(array2.T,-1) + np.triu(array2*-1, 1)
        symetric_conj = [[str(int(array1[x][y]))+("+"*(int(array2[x][y])>=0)+str(int(array2[x][y]))+"i")*(x!=y) for y in range(size[1])] for x in range(size[0])]
        complex_symetric_matrix = Matrix(symetric_conj, h_buff = 2.6).scale(0.5)
        self.play(ReplacementTransform(faded_ham_matrix,complex_symetric_matrix),ReplacementTransform(equivalent2,equivalent_Complex))
        self.wait(1)
        
