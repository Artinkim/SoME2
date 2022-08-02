from manim import *
import numpy as np

class Vectors(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=False
        )

    def mfv(self, vec1,vec2): #matrixfromvectors
        return [[vec1[0],vec2[0]],[vec1[1],vec2[1]]]

    def vecs2poly(self, vector1, vector2):
        return Polygon(vector1.get_start(), vector1.get_end(), vector1.get_end()+vector2.get_end(), vector2.get_end(), color = YELLOW, fill_color=YELLOW, fill_opacity=0.5)

    def get_area(self, vector1=None,vector2=None):
        """
        Returns the area of the polygon defined by the vectors

        Default vectors are basis (1,0) and (0,1)
        """
        if vector1==None:
            vector1 = self.get_vector([1,0])
        if vector2==None:
            vector2 = self.get_vector([0,1])
        return np.linalg.det(self.mfv(vector1.get_end(), vector2.get_end()))
        

    def construct(self):
        vec1, vec2 = [2,0], [0,1]
        #matrix = [[-1,-2], [2,0]]
        matrix = (np.random.rand(2,2)*4-2).round(2)
        print(matrix)

        vector1 = self.get_vector(vec1, color=GREEN)
        vector2 = self.get_vector(vec2, color=RED)
        v1_label = Tex("v",color=GREEN).add_updater(lambda m: m.move_to(vector1.get_end()))
        v2_label = Tex("w",color=RED).add_updater(lambda m: m.move_to(vector2.get_end()))
        
        caption = Tex(*[c for c in "(v, w) → (Mv, Mw)"])
        matrix_tex =  VGroup(Tex("M"," = ").set_color_by_tex("M", YELLOW),DecimalMatrix(matrix)).arrange(RIGHT)
        ul = VGroup(caption, matrix_tex).arrange(DOWN).to_edge(UL)

        caption.set_color_by_tex("v", GREEN)
        caption.set_color_by_tex("w", RED)
        caption.set_color_by_tex("M", YELLOW)
        
        area = self.vecs2poly(vector1,vector2).set_z_index(-1)
        area.add_updater(lambda m: m.set_points_as_corners(self.vecs2poly(vector1,vector2).get_vertices()))
        
        det_decimal = DecimalNumber(np.linalg.det(self.mfv(vec1,vec2)))
        det_decimal.add_updater(lambda x: x.move_to(area.get_center()))
        det_decimal.add_updater(lambda x: x.set_value(self.get_area(vector1,vector2)))

        self.add_transformable_mobject(vector1,vector2)
        self.add_background_mobject(area,det_decimal,ul,v1_label,v2_label)
        
        self.apply_matrix(matrix)
        self.wait(1)
        self.moving_mobjects = []
        self.add_background_mobject(VGroup(self.vecs2poly(vector1,vector2),vector1.copy(),vector2.copy(),DecimalNumber(det_decimal.get_value()).move_to(det_decimal)).set_opacity(0.25))
        self.apply_inverse(matrix)

        a = PI/2.4
        self.play(Rotate(vector1,angle=a,about_point=ORIGIN),Rotate(vector2,angle=a,about_point=ORIGIN))

        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait(1) 
        #self.play(Rotate(vector1,angle=-a,about_point=ORIGIN),Rotate(vector2,angle=-a,about_point=ORIGIN))

        self.wait(1)