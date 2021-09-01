# Broyden 1d method.

"""
This is not really a documented method.  I derived it from
the actual documented multi-dimensional method of Broyden.
With cancellation, this would resolve to the Secant method.
But, as it stands, the method has some advantages.  There
are two main reasons:
  1. Single starting guess.
  2. Single function evaluation per iteration.
"""

from utils import eps, dxdy


def fsolve(f, x, args=(), tol=1e-6, maxi=96):
  fo, k = dxdy(f, x, *args)
  if abs(fo) <= tol:
    return x
  for i in range(maxi):
    dx = -k * fo
    x += dx
    fx = f(x, *args)
    if abs(fx) <= tol:
      return x
    dfx = fx - fo
    if abs(dfx) <= eps:
      return x
    a = dx * k * dfx
    dk = -k * (a - dx * dx) / a
    k += dk
    fo = fx
  raise Exception('Max its reached!')
