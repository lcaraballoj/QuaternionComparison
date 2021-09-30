# Quaternion Comparison
This is part of a math research project on quaternions. It's purpose is to compare the compute times using various different methods for the rotation of 3D objects given three random angles.

# Index
1. [Introduction](#introduction)
2. [Understanding the Math](#understanding_the_math)
3. [Understanding the Code](#understanding_the_code)
4. [Resources](#resources)

# Introduction
The goal of this project is to be able to compare the compute time of various math methods and concepts to calculate the rotation of a 3D object given three random angles. These include using Euler Angles and matrices to get out a rotation matrix, and quaternions to get a quaternion describing this rotation. The hypothesis is that quaternions will be faster to compute over a large set of data. 

# Understanding the Math

# Understanding the Code

# The Why
The goal is prove that quaternions are a more efficient way to compute the rotation of 3D objects. It is a supplementary addition to a research paper on quaternions and a way to collect original data. Quaternions are widely used and are preferred over Euler angles becuase of the speed of computing them, the size, only four scalars vs. the nine in matrix multiplication, and the fact that using quaternions does not result in something called gimbal lock. To have hard data that shows the compute time of quaternions is superior is beneficial for visualizing why we would want to go through the trouble of understanding the complexities of quaternions. 

# Resources
[Computing Euler Angles](https://www.meccanismocomplesso.org/en/3d-rotations-and-euler-angles-in-python/) <br>
[Computing Quaternions](https://www.meccanismocomplesso.org/en/hamiltons-quaternions-and-3d-rotation-with-python/)
