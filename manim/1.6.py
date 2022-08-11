from modulefinder import ReplacePackage
from manim import *
import numpy as np
from utils import ChangingMatrix

class Intro(Scene):
    def construct(self):
        funtion_tex =  MathTex("\\frac{1}{n}", "\\sum_{i=0}^{n} ","f","(M_{i})")
        det_tex = MathTex("\\frac{1}{n}", "\\sum_{i=0}^{n} ","det","(M_{i})")
        trace_tex = MathTex("\\frac{1}{n}", "\\sum_{i=0}^{n} ","Tr","(M","_{i}",")")
        moved_function_tex1 = MathTex("Tr","(M",")").move_to(funtion_tex)
        moved_function_tex2 = MathTex("f(M)").move_to(funtion_tex)
        basis_invariant_tex = Tex("Basis-Invariant Quantities").move_to(UP)
        equivalency_tex1 = MathTex("f(M)"," = ", "f","(","UM{U}^{-1}",")")
        equivalency_tex2 = MathTex("f","(M)"," = ","f","(","\\widetilde{M}",")").next_to(equivalency_tex1,DOWN)
        cob_tex = MathTex("\\widetilde{M} = UM{U}^{-1}").move_to(equivalency_tex1)
        self.add(funtion_tex)
        self.play(TransformMatchingTex(funtion_tex,det_tex),run_time=2)
        self.play(TransformMatchingTex(det_tex,trace_tex),run_time=2)
        self.play(TransformMatchingTex(trace_tex,moved_function_tex1),run_time=2)
        self.play(TransformMatchingShapes(moved_function_tex1,moved_function_tex2),run_time=0.5)
        self.play(Write(basis_invariant_tex),TransformMatchingTex(moved_function_tex2,equivalency_tex1),run_time=2)
        self.play(AnimationGroup(
            TransformMatchingTex(equivalency_tex1,equivalency_tex2), 
            Write(cob_tex),lag_ratio=0.5),run_time=2)
        self.play(Wiggle(equivalency_tex2.submobjects[0]),Wiggle(equivalency_tex2.submobjects[3]),run_time=2)
        self.wait(1)


class ShowEnsemble(MovingCameraScene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(1)
            
    def construct(self):
        N = 2 # size of matrix   
        niter = 5000 # number of samples
        dets = np.zeros((niter))
        histograms = np.zeros((niter,100))
        matricies = np.zeros((niter,N,N))
        for i in range(niter):
            matricies[i] = np.random.randn(N,N)
            dets[i] = np.trace(np.matmul(matricies[i],matricies[i]))
            histograms[i] = np.histogram(dets[:i+1],bins=np.linspace(-10, 10,101))[0]
        
        t = ValueTracker(0)
        chart = BarChart(values=np.zeros((100)), y_range=[0,10,1])
        number_line = NumberLine(x_range=[-10,10,1],include_numbers=True).put_start_and_end_on(chart.c2p(0,0),chart.c2p(100,0))
        
        
        equals_tex = Tex("M = ")
        matrix = ChangingMatrix(matricies,t).next_to(equals_tex)
        sqrd = MathTex("Tr(M^2) =")
        tr_tex = DecimalNumber().add_updater(lambda d: d.set_value(dets[int(t.get_value())])).next_to(sqrd).update()
        n_tex = Tex("N: ")
        count_tex = Integer().add_updater(lambda d: d.set_value(int(t.get_value())+1)).next_to(n_tex)
        ul = VGroup(n_tex,count_tex).move_to(UL+UL+LEFT+LEFT)
        ur = VGroup(VGroup(equals_tex,matrix),VGroup(sqrd,tr_tex)).arrange(DOWN).to_edge(UR)
        tr_rect = SurroundingRectangle(tr_tex)
        
        self.play(Create(equals_tex),Create(matrix),Create(sqrd))
        self.play(Create(chart),Create(number_line),Create(tr_tex))
        
        self.wait(1)
        self.play(Create(tr_rect))
        chart.add_updater(lambda c: c.change_bar_values(histograms[int(t.get_value())]))
        chart.update()
        self.wait(1)
        self.play(FadeOut(tr_rect),Create(ul))

        self.play(t.animate(rate_func=rush_into).set_value(50),run_time=1)
        
        c2 = BarChart(values=np.zeros((100)), y_range=[0,100,10])
        c2.add_updater(lambda c: c.change_bar_values(histograms[int(t.get_value())]))
        self.play(Transform(chart,c2))
        self.remove(chart)
        self.add(c2)
        
        self.play(t.animate(rate_func=smooth).set_value(niter-1),run_time=1)
        self.wait(1)
        
        index = np.where(np.histogram(np.average(dets),bins=np.linspace(-7,7,101))[0]==1)[0]
        vtN = ValueTracker(0)
        c2.add_updater(lambda c: c.change_bar_values([max(0,val-int(vtN.get_value())*(abs(i-index))) for i,val in enumerate(histograms[niter-1])]))
        self.play(vtN.animate(rate_func=smooth).set_value(150),run_time=1)
        self.wait(1)
        
        axes1 = Axes(x_range=[-5,6,1], y_range=[0,1.1, 0.2]).scale(0.5).add_coordinates().scale(0.5).move_to(UL*2+LEFT*2)
        axes1.add(Tex("0").scale(0.4).next_to(axes1.x_axis.n2p(0), DOWN*0.5))
        entry = MathTex("M_{ij}").next_to(axes1, RIGHT).shift(RIGHT+UP)
        arrow = CurvedArrow(entry.get_center(),axes1.c2p(0.8,0.8), color = YELLOW)
        entry_equivalence_tex = MathTex("Tr(M^2) = \sum \lambda_i^2").scale(0.75).next_to(entry, DOWN)
        eiegen_equivalence_tex1 = MathTex("\lambda_{\pm} &= \\frac{M_{11} +M_{22}}{2} \pm \\frac{1}{2}\sqrt{(M_{11}-M_{22})^2 + 4M_{12}^2}").scale(0.5).next_to(axes1, DOWN).shift(RIGHT*2)
        eiegen_equivalence_tex2 = MathTex("\lambda \propto", "f(M_{11}...M_{22})").next_to(axes1, DOWN)
        eiegen_equivalence_tex3 = MathTex("\lambda \propto", "f(M_{11}...M_{nn})").next_to(axes1, DOWN)
        eiegen_equivalence_tex4 = MathTex("\lambda \propto", "\sqrt{n}").next_to(axes1, DOWN)
        guas = axes1.plot(lambda x: np.exp(-(x/3)**2),color=BLUE)
        guas_area = axes1.get_area(guas)
        
        self.playWait(FadeOut(ul),Create(axes1),Create(guas_area),Create(entry))
        self.playWait(Create(entry_equivalence_tex),Create(arrow))
        self.playWait(Create(eiegen_equivalence_tex1))
        self.playWait(ReplacementTransform(eiegen_equivalence_tex1,eiegen_equivalence_tex2))
        self.playWait(ReplacementTransform(eiegen_equivalence_tex2,eiegen_equivalence_tex3))
        self.playWait(ReplacementTransform(eiegen_equivalence_tex3,eiegen_equivalence_tex4))
        


class ShowList(MovingCameraScene):
    def construct(self):
        strings = ["det(M)", "Tr(M)", "Tr(M^2)","...","Tr(M^k)", "\\text{eigenvectors} = v : Mv = Lv \\text{for some} L"]
        texs = VGroup(*[MathTex(str(i+1)+"\\text{. }"+s) for i,s in enumerate(strings)]).arrange(DOWN,aligned_edge=LEFT,buff=0.5).to_edge(UL)
       
        sqrd = MathTex("Tr(M^2)").move_to(texs[2],RIGHT)
        sum_tex = MathTex("= \sum \lambda_i^2").next_to(sqrd)
        
        brace = Tex("\left\}").scale(7)
        func = MathTex("f(\{\lambda_i\})")
        brace_func = VGroup(brace,func).arrange(RIGHT).next_to(texs[2])
        
        self.play(Create(texs[:-1]),run_time=2)
        self.play(Create(brace_func),run_time=1)
        ref = func.copy()
        self.play(Transform(ref,texs[-1]),run_time=1)
        self.add(sqrd)
        self.play(self.camera.frame.animate.scale(0.5).move_to(sqrd).shift(RIGHT),FadeOut(texs,ref,brace_func), run_time=1)
        self.play(Create(sum_tex))
        self.wait(1)
        
        #self.play(Create(texs),run_time=3)
        #self.wait()

class Vectors(ThreeDScene):
    # def mfv(self, vec1,vec2.vec3): #matrixfromvectors
    #     return [[vec1[0],vec2[0],vec3[0]],[vec1[1],vec2[1],vec3[1]],[vec1[2],vec2[2],vec3[2]]]

    def vecs2poly(self, vector1, vector2):
        return Polygon(vector1.get_start(), vector1.get_end(), vector1.get_end()+vector2.get_end(), vector2.get_end(), color = YELLOW, fill_color=YELLOW, fill_opacity=0.5)

    def get_area(self, vector1=None,vector2=None):
        return np.linalg.norm(np.cross(np.array(vector1.get_end()), np.array(vector2.get_end())))
        

    def construct(self):
        
        axes = ThreeDAxes()
        vec1, vec2 = [3/2,0,0], [0,2/3,0]
        matrix = np.array([[(np.sqrt(3)/2)*np.cos(np.pi/18),(np.sqrt(2))*np.cos(np.pi/9),0], [(np.sqrt(3)/2)*np.sin(np.pi/18),(np.sqrt(2))*np.sin(np.pi/9),0],[0,0,1]]).round(2)
        a = PI/0.75
        axis = X_AXIS+Z_AXIS
        rot_matrix = rotation_matrix(a, axis)
        
        rmr = np.matmul(rot_matrix,np.matmul(matrix,np.linalg.inv(rot_matrix))).round(2)
        
        vector1 = Vector(vec1, color=GREEN)
        vector2 = Vector(vec2, color=RED)
        v1_label = Tex("v",color=GREEN).add_updater(lambda m: m.move_to(vector1.get_end())).update()
        v2_label = Tex("w",color=RED).add_updater(lambda m: m.move_to(vector2.get_end())).update()
        
        area = self.vecs2poly(vector1,vector2).set_z_index(-1)
        area.add_updater(lambda m: m.set_points_as_corners(self.vecs2poly(vector1,vector2).get_vertices()))
        area_val = DecimalNumber()
        area_val.add_updater(lambda x: x.move_to(area.get_center())).update()
        area_val.add_updater(lambda x: x.set_value(self.get_area(vector1,vector2))).update()
        
        self.add(axes,vector1,vector2,v1_label,v2_label)
        self.wait(1)
        self.play(Create(area),Write(area_val))

        # apply matrix transformation and leave copy
        vec1 = np.matmul(matrix,vec1) 
        vec2 = np.matmul(matrix,vec2)
        self.play(vector1.animate.put_start_and_end_on(ORIGIN,vec1),vector2.animate.put_start_and_end_on(ORIGIN,vec2))
        self.add(VGroup(area.copy().clear_updaters(),area_val.copy().clear_updaters(),vector1.copy(),vector2.copy()).set_opacity(0.5))
        self.wait(1)
        
        # apply inverse matrix transformation
        vec1 = np.matmul(np.linalg.inv(matrix),vec1)
        vec2 = np.matmul(np.linalg.inv(matrix),vec2)
        self.play(vector1.animate.put_start_and_end_on(ORIGIN,vec1),vector2.animate.put_start_and_end_on(ORIGIN,vec2))
        self.wait(1)
        
        # show 3d perspective
        self.move_camera(phi=45 * DEGREES,theta=-75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.25)
        
        # rotate vectors in 3D
        vec1 = np.matmul(rot_matrix,vec1) 
        vec2 = np.matmul(rot_matrix,vec2)
        self.play(
            Rotate(vector1,angle=a,axis=axis,about_point=ORIGIN),
            Rotate(vector2,angle=a,axis=axis,about_point=ORIGIN)
        )
        self.wait(1)

        # apply matrix transformation
        vec1 = np.matmul(rmr,vec1)
        vec2 = np.matmul(rmr,vec2)
        self.play(vector1.animate.put_start_and_end_on(ORIGIN,vec1),vector2.animate.put_start_and_end_on(ORIGIN,vec2))
        self.wait(1)

        # roate vectors back in 3D
        a*=-1
        vec1 = np.matmul(np.linalg.inv(rot_matrix),vec1) 
        vec2 = np.matmul(np.linalg.inv(rot_matrix),vec2)
        self.play(
            Rotate(vector1,angle=a,axis=axis,about_point=ORIGIN),
            Rotate(vector2,angle=a,axis=axis,about_point=ORIGIN)
        )
        self.wait(1)

class VectorLabel(Scene):
    def playWait(self, *args,**kwargs):
            self.play(*args,**kwargs)
            self.wait(0.1)
    
    def construct(self):
        
        vec1, vec2 = [3/2,0,0], [0,2/3,0]
        matrix = np.array([[(np.sqrt(3)/2)*np.cos(np.pi/18),(np.sqrt(2))*np.cos(np.pi/9),0], [(np.sqrt(3)/2)*np.sin(np.pi/18),(np.sqrt(2))*np.sin(np.pi/9),0],[0,0,1]]).round(2)
        a = PI/0.75
        axis = X_AXIS+Z_AXIS
        rot_matrix = rotation_matrix(a, axis)
        rmr = np.matmul(rot_matrix,np.matmul(matrix,np.linalg.inv(rot_matrix))).round(2)
        
        caption1 = Text("(v, w) ",t2c={"v":GREEN, "w" :RED}).move_to((-4,3,0))
        caption1C1 = caption1.copy()
        caption1C2 = caption1.copy()
        caption2 = Text("(Mv, Mw) ",t2c={"v":GREEN, "w":RED,"M": YELLOW}).move_to((-4,3,0))
        caption3 = Text("(Rv, Rw) ",t2c={"v":GREEN, "w":RED,"M": YELLOW,"R":PURPLE}).move_to((-4,3,0))
        caption4 = MathTex("(","\\widetilde{M}","R","v",", ","\\widetilde{M}","R","w",")").move_to((-4,3,0))
        caption4.set_color_by_tex_to_color_map({"v":GREEN, "w":RED,"M": YELLOW,"R":PURPLE})

        matrix_equals_tex1 = MathTex("M"," = ").next_to(caption1,DOWN,buff=1.5).shift(LEFT)
        matrix_equals_tex2 = MathTex("\\widetilde{M}", "=","R", "M", "{R}^{T}", " = ").next_to(caption1,DOWN,buff=1.5).shift(LEFT)
        matrix_equals_tex3 = MathTex("\\widetilde{M}", " = ").next_to(caption1,DOWN,buff=1.5).shift(LEFT)
        matrix_equals_tex1.set_color_by_tex("M",YELLOW)
        matrix_equals_tex2.set_color_by_tex_to_color_map({"M": YELLOW,"R":PURPLE})
        matrix_equals_tex3.set_color_by_tex("M",YELLOW)
        
        matrix_tex1 = Matrix(matrix[:2,:2]).next_to(matrix_equals_tex1,RIGHT)
        matrix_tex2 = Matrix(rmr).next_to(matrix_equals_tex2,RIGHT)
        matrix_tex3 = Matrix(matrix).next_to(matrix_equals_tex3,RIGHT)
        matrix_tex3C = matrix_tex3.copy()
        
        
        det_tex1 =  VGroup(
            Tex("det(","M",") = ").set_color_by_tex("M", YELLOW),
            DecimalNumber(np.linalg.det(matrix))
        ).arrange(RIGHT).next_to(matrix_tex1,DOWN)
        
        tinv_tex = VGroup(
            Tex("* For a matrix whos change"), 
            Tex("of basis is a rotation the"),
            Tex("transpose is equal to its inverse"), 
            MathTex("R^{T} = R^{-1}").scale(2)
        ).arrange(DOWN).move_to(UR*2+RIGHT*2).scale(0.5)
        
        
        self.playWait(Write(caption1),Write(VGroup(matrix_equals_tex1,matrix_tex1)))
        self.playWait(Write(det_tex1))
        self.playWait(FadeOut(det_tex1))
        self.playWait(ReplacementTransform(caption1,caption2))
        self.playWait(ReplacementTransform(caption2,caption1C1))
        self.playWait(FadeOut(matrix_tex1),FadeIn(matrix_tex3))
        self.playWait(ReplacementTransform(caption1C1,caption3))
        
        self.playWait(ReplacementTransform(matrix_equals_tex1,matrix_equals_tex2),ReplacementTransform(matrix_tex3,matrix_tex2),Write(tinv_tex))
        self.playWait(ReplacementTransform(matrix_equals_tex2,matrix_equals_tex3),matrix_tex2.animate.next_to(matrix_equals_tex3,RIGHT))
        self.playWait(ReplacementTransform(caption3,caption4))
        
        self.playWait(ReplacementTransform(matrix_tex2,matrix_tex3C))
        self.playWait(FadeOut(tinv_tex),ReplacementTransform(caption4,caption1C2))
        
