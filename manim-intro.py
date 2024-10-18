from manim import Circle, Square, Triangle, Transform, Create, Scene

class GeometricScene(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        circle2 = Circle(4)

        # Add shapes to the scene
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, triangle))
        self.play(Transform(triangle, circle2))
        self.wait()