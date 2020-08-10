"""
============
NumPy basics
============

What is NumPy
=========================================

NumPy (Numerical Python) is the fundamental package for scientific computing in Python.
NumPy creates powerful n-dimensional arrays that fast and versatile. NumPy arrays can be
vectorized, indexed, and broadcast for fast and clean code. NumPy has numerical computing
tools with comprehensive mathematical functions, random number generators, linear algebra
routines, Fourier transforms, and more. The core of NumPy is well-optimized C code. You
can enjoy the flexibility of Python with the speed of compiled code. NumPy supports a wide
range of hardware and computing platforms, and plays well with distributed, GPU, and
sparse array libraries. The high-level NumPy syntax makes NumPy easy to use and accessible
for programmers with a wide variety of backgrounds and experience. 

Numpy is distributed under an open source _BSD License:
https://github.com/numpy/numpy/blob/master/LICENSE.txt, Numpy is developed and maintained
_publicly on GitHub: https://github.com/numpy/numpy by a vibrant, responsive, and diverse
_community: https://numpy.org/community. 

Learn more about :ref:`NumPy here <whatisnumpy>`!

Getting Help
=========================================

You can print out this help document in iPython or Jupyter with::

    >>>import numpy as np
    >>>import np.doc
    >>>?doc.basics

The full NumPy documentation is rendered in html at https://numpy.org/doc/stable/

If you're just getting started try the :ref:`Absolute basics for beginners
<absolute_beginners>`

Every function and object in the NumPy library has docstrings which can be accessed by
using either `?` or `help()`. For example, to print out the docstring in iPython or a
Jupyter notebook you can run either::

    >>> ?np.array

or::

    >>> help(np.array)

You can reach out to the NumPy community for help in the
_NumPy-Discussion:numpy-discussion@python.org or post issues on the _NumPy
repository:https://github.com/numpy/numpy/issues. 

Using NumPy
=========================================

Throughout the NumPy documentation, NumPy is imported as `np` as such,::
    >>> import numpy as np

This allows you as a NumPy programmer to create an array such as `[1,2,3]` as such,::
    >>> a = np.array([1,2,3])

If you run the code above, you have create a one-dimensional array with three elements: 1,
2, and 3. There are a  
