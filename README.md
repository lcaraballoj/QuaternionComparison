# Quaternion Comparison
This is part of a math research project on quaternions. It's purpose is to compare the compute times using various different methods for the rotation of 3D objects given three random angles.

# Index
1. [Introduction](#introduction)
2. [The Why](#the-why)
3. [Understanding the Math](#understanding-the-math)
4. [Understanding the Code](#understanding-the-code)
5. [Resources](#resources)

# Introduction
The goal of this project is to be able to compare the compute time of various math methods and concepts to calculate the rotation of a 3D object given three random angles. These include using Euler Angles and matrices to get out a rotation matrix, and quaternions to get a quaternion describing this rotation. The hypothesis is that quaternions will be faster to compute over a large set of data. 

# The Why
The goal is prove that quaternions are a more efficient way to compute the rotation of 3D objects. It is a supplementary addition to a research paper on quaternions and a way to collect original data. Quaternions are widely used and are preferred over Euler angles becuase of the speed of computing them, the size, only four scalars vs. the nine in matrix multiplication, and the fact that using quaternions does not result in something called gimbal lock. To have hard data that shows the compute time of quaternions is superior is beneficial for visualizing why we would want to go through the trouble of understanding the complexities of quaternions. 

# Understanding the Math
This code uses rotation matrices generated from three random Euler angles as well as Rodrigues' rotation formula. The most interesting part is going to be the various ways to generate quaternions.

When given a quaternion to rotate we are then going to get a quaternion out, but we can also generate a quaternion to describe rotation using Euler angles as well as vectors. This is base for the formulas used to genearte the rotation quaternion and what is being used to compare the compute times. 

# Understanding the Code
The code has five main parts: `EulerAngle.py`, `Rodrigues.py`, `Quaternions.py`, `EulerVQuaternion.py`, and `RodriguesVQuaternion.py`. There is also a `UnitVector.py` and `Graphs.py`, but these are more suplemental. The real bulk of the computations happens in the aforementioned files. 

- `EulerAngle.py` is used to compute the rotation matrix given three random Euler angles.
   - This includes:
      1.  Finding the 3x3 matrix for the x-axis: `X`
      2.  Finding the 3x3 matrix for the y-axis: `Y`
      3.  Finding the 3x3 matrix for the z-axis: `Z`
- `Rodrigues.py` is used to compute Rodrigue's rotation formula given two random vectors, with one being turned into a unit vector with `UnitVector.py` and a random angle. 
  - This includes:
      1. Finding the vector using Rodrigues rotation formula: `rodrigues_formula()`
- `Quaternions.py` is used for all the quaternion computations.
  - This includes:
    1. Finding the conjugate: `conjugate()`
    2. Generating a quaternion given a vector and angle: `calc_quaternion()` [Uses `conjugate()` and functions from `UnitVector.py`]
    3. Multiplying quaternions following the i, j, k relations needed: `quaternion_multiplication()`
    4. Calculating the quaternion to represent a rotation with generating the quaternion: `quaternion_rotation_convert()` [Uses `calc_quaternion()` and `quaternion_multiplication`]
    5. Calculating the quaternion to represent a rotation without generating the quaternion: `quaternion_rotation()` [Uses `quaternion_multiplication]
    6. Calculating the quaternion to reprsent a rotation using three Euler angles: `euler_to_quaternion()`
 
 - `EulerVQuaternion.py` takes all functions from `EulerAngle.py` and `euler_to_quaternion()` from `Quaternions.py` and compares their compute times when given the same three random angles. Will then generate two graphs: one displaying and comparing the compute times for all iterations and one displaying and comparing the average compute time over the iterations as well as a table using [prettytable](https://pypi.org/project/prettytable/). 
 - `RodriguesVQuaternion.py` takes all functions from `Rodrigues.py` and `quaternion_rotation()` from `Quaternions.py` and compares their compute times when given the same three random angles. Will then generate two graphs: one displaying and comparing the compute times for all iterations and one displaying and comparing the average compute time over the iterations as well as a table using [prettytable](https://pypi.org/project/prettytable/).
 - `Graphs.py` generates the graphs using [matplot](https://matplotlib.org/) and [pandas](https://pandas.pydata.org/). 

# Resources
[Computing Euler Angles](https://www.meccanismocomplesso.org/en/3d-rotations-and-euler-angles-in-python/) <br>
[Computing Quaternions](https://www.meccanismocomplesso.org/en/hamiltons-quaternions-and-3d-rotation-with-python/)
