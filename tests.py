# Root finder tests

import bisection, rtbis, zbis
import anderson, illinois, pegasus, ridder
import falsi, mfalsi
import newt, newton, rtsafe, dnewt
import secant, broyden
import brent,  chandru, kiusalaas, wernick
import halley, schroeder
import resub, aitken, fixpoint, steffensen, wegstein
import polynewt, polyroot

def efunc(x):
  return (x - 3) * (x + 5)


def test_illinois():
  x0 = (1, 5)
  x = illinois.fsolve(efunc, x0)
  print(x)


if __name__ == "__main__":
  test_illinois()
