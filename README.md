# Lissajous-Curves
An animation of [Lissajous Curves](https://en.wikipedia.org/wiki/Lissajous_curve) in Python 3.x using the Pygame library.

# Maths
All explanations of the mechanics behind these curves can be found at the hyperlink above.
The [following equation](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line) was used to determine where 2 line collide:
![](https://www.codecogs.com/eqnedit.php?latex=https://latex.codecogs.com/gif.latex?{\begin{aligned}(P_{x},P_{y})={\bigg&space;(}&{\frac&space;{(x_{1}y_{2}-y_{1}x_{2})(x_{3}-x_{4})-(x_{1}-x_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}},\\&{\frac&space;{(x_{1}y_{2}-y_{1}x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4})-(y_{1}-y_{2})(x_{3}-x_{4})}}{\bigg&space;)}\end{aligned}})
