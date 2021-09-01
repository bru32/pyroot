# Chandrupatla root finding method.

from utils import eps


def fsolve(f, x, args=(), ftol=1e-6, maxi=48):
  if len(x) != 2:
    raise Exception("Two guesses needed!")
  a = x[1]
  fa = f(a, *args)
  if abs(fa) <= eps:
    return a
  b = x[0]
  fb = f(b, *args)
  if abs(fb) <= eps:
    return b
  if fa * fb > 0:
    raise Exception("No bracket!")
  t = 0.5
  for i in range(maxi):
    xt = a + t * (b - a)
    ft = f(xt, *args)
    if ft * fa > 0:
      c, fc = a, fa
    else:
      c, b = b, a
      fc, fb = fb, fa
    a, fa = xt, ft
    if abs(fa) < abs(fb):
      xm, fm = a, fa
    else:
      xm, fm = b, fb
    tol = eps * (2.0 + abs(xm))
    tlim = tol / abs(b - c)
    if (tlim > 0.5) or (abs(ft) <= ftol):
      return xm
    xi = (a - b) / (c - b)
    phi = (fa - fb) / (fc - fb)
    if phi < xi / phi < 2.0 - phi:
      # inverse quadratic step
      t = fa / (fb - fa) * fc / (fb - fc) + (c - a) / (b - a) * fa / (fc - fa) * fb / (fc - fb)
    else:
      t = 0.5
    t = min(1.0 - tlim, max(tlim, t))
  raise Exception("Max its reached!")
