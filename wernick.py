# Wernick root find method.

"""
This is a Brent type method using Inv Quad Int.  I experimented with Chandrupatla 
and found some of logic bit confusing.  So, I went back to a pure IQI with recalc 
of c at every step.
Simplified Logic:
  calc c by Bisection.
  calc s by Inv Quad (safety check failing to Secant).
  adjust bracket.
"""

from utils import eps


def fsolve(f, x, args=(), tol=1e-6, maxi=48):
  assert len(x) == 2
  a, b = x  # unpack the x bracket
  fa = f(a, *args)
  if abs(fa) <= eps:
    return a
  fb = f(b, *args)
  if abs(fb) <= eps:
    return b
  assert fa * fb <= 0
  for i in range(maxi):
    dx = b - a  # bracket delta
    c = a + 0.5 * dx  # bisection
    if abs(dx) <= tol:
      return c
    fc = f(c, *args)
    if abs(fc) <= tol:
      return c

    if fa != fc and fb != fc:
      # inv quad interp
      fab, fac, fbc = fa-fb, fa-fc, fb-fc
      s = a*fc*fb/fac/fab + c*fa*fb/fac/fbc - b*fa*fc/fab/fbc
    else:
      # secant
      s = a + dx * fb / (fa - fb)

    fs = f(s, *args)
    if abs(fs) <= tol:
      return s

    # adjust bracket [a, c, s, b]
    if fc * fs < 0:
      a, fa = c, fc
      b, fb = s, fs
    elif fa * fc < 0:
      b, fb = c, fc
    elif fs * fb < 0:
      a, fa = s, fs
  raise Exception('Max its reached!')
