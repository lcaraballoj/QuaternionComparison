import math
from manim import *

def arrow_on_path(path, alpha, angle, sign = +1, delta = 0.01):
  tip = Triangle().scale(0.15)

  pos1 = path.point_from_proportion(alpha - delta * sign)
  pos2 = path.point_from_proportion(alpha + delta * sign)
  pos = (pos1 + pos2) / 2

  rotation = angle + angle_of_vector(pos1 - pos2)

  tip.rotate(rotation).move_to(pos)
  tip.set_fill(WHITE, opacity=1).set_stroke(width=0)

  return tip

class EllipseExample(Scene):
    def construct(self):
        ellipse_1 = Ellipse(width=2.0, height=4.0).set_color(RED).rotate(.30).move_to(4*LEFT)
        ellipse_2 = Ellipse(width=2.0, height=4.0).set_color(BLUE).rotate(.30)
        ellipse_3 = Ellipse(width=2.0, height=4.0).set_color(GREEN).rotate(.30).move_to(4*RIGHT)

        arrow_1 = Arrow(start=ellipse_1.get_center(), end=[-2,1,0], color=WHITE)
        arrow_2 = Arrow(start=ellipse_2.get_center(), end=[-2,-1,0], color=WHITE)

        arrowDir1 = arrow_on_path(ellipse_1, 0.16, PI/2)
        arrowDir2 = arrow_on_path(ellipse_1, 0.64, PI/2)

        arrowDir3 = arrow_on_path(ellipse_2, 0.16, PI/2)
        arrowDir4 = arrow_on_path(ellipse_2, 0.64, PI/2)

        arrowDir5 = arrow_on_path(ellipse_3, 0.18, PI/2)
        arrowDir6 = arrow_on_path(ellipse_3, 0.16, PI/2)
        arrowDir7 = arrow_on_path(ellipse_3, 0.62, PI/2)
        arrowDir8 = arrow_on_path(ellipse_3, 0.64, PI/2)

        textQV = MathTex(r"qv", font_size = 80).move_to(ellipse_1).shift(DOWN*3, RIGHT*.4)
        textVQ = MathTex(r"vq^*", font_size = 80).shift(DOWN*3).shift(RIGHT*.4)
        textQVQ = MathTex(r"qvq^*", font_size = 80).move_to(ellipse_3).shift(DOWN*3, RIGHT*.4)

        self.add(ellipse_1, ellipse_2, ellipse_3, arrow_1, arrow_2, arrowDir1, arrowDir2, arrowDir3, arrowDir4, arrowDir5, arrowDir6, arrowDir7, arrowDir8, textQV, textVQ, textQVQ)
