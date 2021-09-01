# Brent root finding method.

from utils import eps, SIGN


def fsolve(f, x, args=(), tol=1e-6, maxi=48):
  if len(x) != 2:
    raise Exception('Method needs two starting guesses!')
  a, b = x
  fa = f(a, *args)
  fb = f(b, *args)
  if fa * fb > 0:
    raise Exception("Root must be bracketed!")
  c, fc = b, fb
  e = d = b - a
  for its in range(maxi):
    if fb * fc > 0:
      c, fc = a, fa
      e = d = b - a
    if abs(fc) < abs(fb):
      a, b = b, c
      fa, fb = fb, fc
      c, fc = a, fa
    tol1 = 2 * eps * abs(b) + 0.5 * tol
    xm = 0.5 * (c - b)
    if abs(xm) <= tol1 or fb == 0:
      return b
    if abs(e) >= tol1 and abs(fa) > abs(fb):
      s = fb / fa
      if a == c:
        p = 2 * xm * s
        q = 1 - s
      else:
        q = fa / fc
        r = fb / fc
        p = s * (2 * xm * q * (q - r) - (b - a) * (r - 1))
        q = (q - 1) * (r - 1) * (s - 1)
      if p > 0:
        q = -q
      p = abs(p)
      min1 = 3 * xm * q - abs(tol1 * q)
      min2 = abs(e * q)
      min0 = min1 if (min1 < min2) else min2
      if 2 * p < min0:
        e, d = d, p / q
      else:
        d, e = xm, d
    else:
      d, e = xm, d
    a, fa = b, fb
    if abs(d) > tol1:
      b += d
    else:
      b += SIGN(tol1, xm)
    fb = f(b, *args)
  raise Exception("Max its reached!")
