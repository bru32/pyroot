# Pegasus method (variant of Illinois).

from utils import eps


def fsolve(f, x0, args=(), tol=1e-6, maxi=48):
  if len(x0) != 2:
    raise Exception("Two guesses needed!")
  x1, x2 = x0
  x = 0.5 * (x1 + x2)
  f1 = f(x1, *args)
  f2 = f(x2, *args)
  if f1 * f2 >= 0.0:
    raise Exception("Root must be bracketed!")
  for i in range(maxi):
    dx = x2 - x1
    dy = f2 - f1
    if abs(dy) <= eps:
      return x
    x3 = x1 - f1 * dx / dy
    f3 = f(x3, *args)
    x = x3
    if abs(f3) < tol:
      return x
    if f2 * f3 <= 0:
      x1, f1 = x2, f2
    else:
      m = f2 / (f2 + f3)
      f1 = m * f1
    x2, f2 = x3, f3
  raise Exception("Max its reached!")
