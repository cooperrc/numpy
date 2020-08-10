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

NumPy is distributed under an open source 
`BSD License <https://github.com/numpy/numpy/blob/master/LICENSE.txt>`, 
NumPy is developed and maintained publicly on `GitHub <https://github.com/numpy/numpy>`_
by a vibrant, responsive, and diverse _community: https://numpy.org/community. 

Learn more about :ref:`NumPy here <whatisnumpy>`!

Getting Help
=========================================

You can print out this help document in iPython or Jupyter with::

    >>> import numpy.doc as doc
    >>> help(doc.basics)

The full NumPy documentation is rendered in html at https://numpy.org/doc/stable/

If you're just getting started try the :ref:`absolute-beginners`

Every function and object in the NumPy library has docstrings which can be accessed by
using either ``?`` or ``help()``. For example, to print out the docstring in iPython or a
Jupyter notebook you can run either::

    >>> ?np.array

or::

    >>> help(np.array)

You can reach out to the NumPy community for help via the
`NumPy Discussion Board <numpy-discussion@python.org>` or post your issue on the 
`NumPy repository <https://github.com/numpy/numpy/issues>`. 

Using NumPy
=========================================

NumPy is usually imported as ``np`` as such::
    >>> import numpy as np

This command allows you to call numpy functions using ``np.function``. As a NumPy
programmer, you can create the array ``[1,2,3]`` as such::
    >>> a = np.array([1,2,3])
    >>> a
    array([1, 2, 3])

If you run the code above, you have created a one-dimensional array with three elements: 1,
2, and 3. You gave ``np.array`` the list, ``[1,2,3]`` and it created a one-dimensional
array. Now, you can use this array for a number of mathematical operations e.g. 

* add scalars to ``a``::

    >>> a+2
    array([3, 4, 5])

* multiply scalars by ``a``::

    >>> 3*a
    array([3, 6, 9])

* divide ``a`` by a scalar::

    >>> a/3
    array([0.33333333, 0.66666667, 1.        ])

* multiply a new array element-wise by ``a``::

    >>> b = np.array([4,5,6])
    >>> a*b
    array([ 4, 10, 18 ])

* and much more!

There are also lots more ways to create arrays, as seen in <arrays.creation>. Then, there are
plenty of ways to use arrays including :ref:`linearalgebra-svd`, :ref:`maskarrays`, etc.

Next Steps
===========

If you're just getting started with Python, check out the 
`Python tutorial <https://docs.python.org/tutorial/>`__.

If you're familiar with Python, but new to NumPy, check out the :ref:`absolute-beginners`. 

If you're coming from another array-based computing software like Matlab, you can check
out the :ref:`numpy-for-matlab-users` or :ref:`quickstart`. 

If you want to see the next ``np.doc`` tutorial, check out :ref:`arrays.creation` or run::
    >>> import numpy.doc as doc
    >>> ?doc.creation

No matter where you go next, enjoy the speed and efficiency of array-computing in NumPy!


"""
