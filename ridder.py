# Ridder root find method.

from utils import SIGN
from math import sqrt


def fsolve(f, x0, args=(), tol=1e-6, maxi=48):
  if len(x0) != 2:
    raise Exception("Two guesses needed!")
  x1, x2 = x0
  fl = f(x1, *args)
  fh = f(x2, *args)
  if fl * fh >= 0.0:
    raise Exception("Root must be bracketed!")
  xl, xh = x1, x2
  x = -1.11e30
  for i in range(maxi):
    xm = 0.5 * (xl + xh)
    fm = f(xm, *args)
    s = sqrt(fm * fm - fl * fh)
    if s == 0.0:
      return xm
    if fl >= fh:
      xnew = xm + (xm - xl) * fm / s
    else:
      xnew = xm + (xl - xm) * fm / s
    if abs(xnew - x) <= tol:
      return xnew
    x = xnew
    fx = f(x, *args)
    if fx == 0.0:
      return x
    if SIGN(fm,fx) != fm:
      xl, fl = xm, fm
      xh, fh = x, fx
    elif SIGN(fl,fx) != fl:
      xh, fh = x, fx
    elif SIGN(fh, fx) != fh:
      xl, fl = x, fx
    else:
      raise Exception("Undefined error!")
    if abs(xh - xl) <= tol:
      return x
  raise Exception("Max its reached!")
