# Newton with bisection.

from utils import dydx


def fsolve(f, x0, args=(), tol=1e-6, maxi=48):
  if len(x0) != 2:
    raise Exception("Need two guesses!")
  a, b = x0
  fa = f(a, *args)
  fb = f(b, *args)
  if (fa > 0.0 and fb > 0.0) or (fa < 0.0 and fb < 0.0):
    raise Exception("No bracket!")
  if fa == 0.0:
    return a
  if fb == 0.0:
    return b
  if fa > 0.0:
    a, b = b, a
    fa, fb = fb, fa
  x = 0.5 * (a + b)
  dx0 = abs(b - a)
  dx = dx0
  fx, df = dydx(f, x, *args)
  for i in range(maxi):
    if (((x-b)*df-fx)*((x-a)*df-fx) > 0.0) or (abs(2.0*fx) > abs(dx0*df)):
      # bisection step
      dx0 = dx
      dx = 0.5 * (b - a)
      x = a + dx
      if a == x:
        return x
    else:
      # newton step
      dx0 = dx
      dx = fx / df
      t = x
      x -= dx
      if t == x:
        return x
    if abs(dx) < tol:
      return x
    fx, df = dydx(f, x, *args)
    if fx < 0.0:
      a = x
    else:
      b = x
  raise Exception("Max its reached!")
