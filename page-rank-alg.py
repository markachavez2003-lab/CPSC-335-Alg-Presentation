from manim import *

# ---------- Scene 1: Title / Names ----------
class PresentationIntro(Scene):
    def construct(self):
        # Title
        title = Text("PageRank Presentation", font_size=60)
        self.play(Write(title))
        self.wait(1)

        # Names
        names = Text("Marco\nJeremy\nRichard\nArman", font_size=40)
        names.next_to(title, DOWN, buff=1)  # positions below title
        self.play(Write(names))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(names))
        self.wait(1)

# ---------- Scene 2: Matrix Example ----------
class MatrixExample(Scene):
    def construct(self):
        # Title for the matrix
        matrix_title = Text("Matrix Example from Linear Algebra", font_size=50)
        self.play(Write(matrix_title))
        self.wait(1)

        # Example matrix
        matrix = MathTex(
            r"\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}", 
            font_size=50
        )
        matrix.next_to(matrix_title, DOWN, buff=1)
        self.play(Write(matrix))
        self.wait(2)

        # Optional: highlight an element
        box = SurroundingRectangle(matrix[0][4], color=YELLOW, buff=0.1)  # highlights '5'
        self.play(Create(box))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(matrix_title), FadeOut(matrix), FadeOut(box))