# Standard regula-falsi method.

from utils import eps


def fsolve(f, x0, args=(), tol=1e-5, maxi=98):
  if len(x0) != 2:
    raise Exception("Need two guesses!")
  a, b = x0
  fa = f(a, *args)
  fb = f(b, *args)
  if fa * fb > 0:
    raise Exception("No bracket!")
  if fb < 0:
    a, b = b, a
    fa, fb = fb, fa
  c, fc = a, fa
  for i in range(maxi):
    if (abs(a - b) < tol) or abs(fc) < tol:
      return c
    df = fb - fa
    if abs(df) <= eps:
      raise Exception("Divide by zero!")
    c = (fb * a - fa * b) / df
    fc = f(c, *args)
    if fa * fb <= 0:
      b, fb = c, fc
    else:
      a, fa = c, fc
  raise Exception("Max its reached!")
