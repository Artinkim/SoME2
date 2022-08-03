from manim import *
import numpy as np

# class ChangingMatrix(MobjectMatrix):
#         def __init__(self, matrix, curr):
#             self.size = [len(matrix),len(matrix[0])]
#             self.nums = [[DecimalNumber() for _ in range(self.size[1])] for __ in range(self.size[0])]
            
#             for x in range(self.size[0]):
#                 for y in range(self.size[1]):
#                     self.nums[x][y].set_value(matrix[x][y])
#                     curr.add_fixed_in_frame_mobjects(self.nums[x][y])
                    

#             # self.add_updater(lambda m: vt*0)
#             super().__init__(self.nums, h_buff=2, element_alignment_corner=DR)

#         def animations(self,matrix):
#             animations = []
#             for x in range(self.size[0]):
#                 for y in range(self.size[1]):
#                     self.nums[x][y].clear_updaters()
#                     vt = ValueTracker(self.nums[x][y].get_value())
#                     self.nums[x][y].add_updater(lambda d: d.set_value(vt.get_value()))
#                     animations.append(vt.animate.set_value(matrix[x][y]))
#             return animations

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
        a = PI/1.25
        axis = X_AXIS+Z_AXIS
        rot_matrix = rotation_matrix(a, axis)
        rmr = np.matmul(rot_matrix,np.matmul(matrix,np.linalg.inv(rot_matrix))).round(2)
        
        vector1 = Vector(vec1, color=GREEN)
        vector2 = Vector(vec2, color=RED)
        v1_label = Tex("v",color=GREEN).add_updater(lambda m: m.move_to(vector1.get_end())).update()
        v2_label = Tex("w",color=RED).add_updater(lambda m: m.move_to(vector2.get_end())).update()
        
        caption1 = Tex(*[c for c in "(v, w) → (Mv, Mw)"]).set_color_by_tex("v", GREEN).set_color_by_tex("w", RED).set_color_by_tex("M", YELLOW)
        caption2 = MathTex(*[c for c in "(Rv, Rw)"],"\\rightarrow"," (","R", "M", "{{R}}^{-1}","R", "v", ", ", "R", "M","{{R}}^{-1}","R", "w",")").set_color_by_tex("v", GREEN).set_color_by_tex("w", RED).set_color_by_tex("M", YELLOW).set_color_by_tex("R", PURPLE)
        matrix_equals_tex1 = Tex("M"," = ").set_color_by_tex("M", YELLOW)
        matrix_equals_tex2 = MathTex("R", "M", "{{R}}^{-1}", " = ").set_color_by_tex("M", YELLOW).set_color_by_tex("R", PURPLE)
        matrix_tex1 = VGroup(matrix_equals_tex1,Matrix(matrix).scale(0.75)).arrange(RIGHT)
        matrix_tex2 = VGroup(matrix_equals_tex2,Matrix(rmr).scale(0.75)).arrange(RIGHT)
        det_unit_tex1 =  VGroup(Tex("det(","M",") = ").set_color_by_tex("M", YELLOW),DecimalNumber(np.linalg.det(matrix))).arrange(RIGHT)#.add_updater(lambda x: x.set_value(np.linalg.det(matrix)))
        det_unit_tex2 =  VGroup(MathTex("det(","R", "M", "{{R}}^{-1}",") = ").set_color_by_tex("M", YELLOW).set_color_by_tex("M", YELLOW).set_color_by_tex("R", PURPLE),DecimalNumber(np.linalg.det(matrix))).arrange(RIGHT) 
        ul1 = VGroup(caption1, matrix_tex1,det_unit_tex1).arrange(DOWN).to_edge(UL)
        ul2 = VGroup(caption1, matrix_tex2,det_unit_tex2).arrange(DOWN).to_edge(UL)
        caption2.to_edge(UL)
        
        area = self.vecs2poly(vector1,vector2).set_z_index(-1)
        area.add_updater(lambda m: m.set_points_as_corners(self.vecs2poly(vector1,vector2).get_vertices()))
        area_val = DecimalNumber()
        area_val.add_updater(lambda x: x.move_to(area.get_center())).update()
        area_val.add_updater(lambda x: x.set_value(self.get_area(vector1,vector2))).update()
        
        self.add_fixed_in_frame_mobjects(ul1)
        self.add(axes,vector1,vector2,v1_label,v2_label,area,area_val)
        self.move_camera(phi=45 * DEGREES,theta=-75 * DEGREES)
        #self.begin_ambient_camera_rotation(rate=0.5)

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
        
        # rotate vectors in 3D
        vec1 = np.matmul(rot_matrix,vec1) 
        vec2 = np.matmul(rot_matrix,vec2)
        self.play(
            Rotate(vector1,angle=a,axis=axis,about_point=ORIGIN),
            Rotate(vector2,angle=a,axis=axis,about_point=ORIGIN)
        )
        self.remove(matrix_tex1,det_unit_tex1,caption1)
        self.add_fixed_in_frame_mobjects(matrix_tex2,det_unit_tex2,caption2)
        #self.play(Transform(matrix_tex1,matrix_tex2),Transform(det_unit_tex1,det_unit_tex2))
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
        self.remove(matrix_tex2,det_unit_tex2,caption2)
        self.add_fixed_in_frame_mobjects(matrix_tex1,det_unit_tex1,caption1)
        self.wait(1)
