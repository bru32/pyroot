# Halleys method (using the 2nd derivative).

from utils import dydx2


def fsolve(f, x, args=(), tol=1e-6, maxi=48):
  for i in range(maxi):
    fx, f1, f2 = dydx2(f, x, *args)
    d = 2.0 * f1 * f1 - fx * f2
    if abs(d) <= 1e-23:
      return x
    dx = (2.0 * fx * f1) / d
    x -= dx
    if abs(dx) <= tol:
      return x
  raise Exception("Max its reached!")
