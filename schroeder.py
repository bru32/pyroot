# Schroeders method (uses 2nd derivative).

from utils import dydx2


def fsolve(f, x, args=(), tol=1e-6, maxi=50):
  for i in range(maxi):
    xo = x
    fx, f1, f2 = dydx2(f, x, *args)
    dxn = fx / f1  # newton correction
    x -= dxn * (1.0 + 0.5 * dxn * f2 / f1)
    if abs(x - xo) <= tol:
      return x
  raise Exception("Max its reached!")
