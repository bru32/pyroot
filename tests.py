# Root finder tests

__author__ = "Bruce Wernick"
__date__ = "1 September 2021"

import math

import bisection, rtbis, zbis
import anderson, illinois, pegasus, ridder
import falsi, mfalsi
import newt, newton, rtsafe, dnewt
import secant, broyden
import brent, chandru, kiusalaas, wernick
import halley, schroeder
import resub, aitken, fixpoint, steffensen, wegstein
import polynewt, polyroot


def efunc(x):
  """function result only"""
  return (x - 3) * (x + 5)


def dfunc(x):
  """function and slope"""
  return (x - 3) * (x + 5), 2 * (x + 1)


def afunc(x):
  """fixed point function"""
  return 1 - 0.5 * math.sin(x)


def test_illinois():
  x0 = (1, 5)  # starting guess
  x = illinois.fsolve(efunc, x0)
  print(f"illinois: {x:0.5f}")


def test_newt():
  x0 = 1  # starting guess
  x = newt.fsolve(dfunc, x0)
  print(f"newt: {x:0.5f}")


def test_aitken():
  x0 = 1.0  # starting guess
  x = aitken.fixpoint(afunc, x0)
  print(f"aitken: {x:0.5f}")


def test_polynewt():
  x0 = 1.0  # starting guess
  a = [-3, 2, 0.5]
  x = polynewt.polyroot(a, x0)
  print(f"polynewt: {x:0.5f}")


def test_halley():
  x0 = 1.0  # starting guess
  x = halley.fsolve(efunc, x0)
  print(f"halley: {x:0.5f}")


def test_brent():
  x0 = (1, 5)  # starting guess
  x = brent.fsolve(efunc, x0)
  print(f"brent: {x:0.5f}")


def test_mfalsi():
  x0 = (1, 5)  # starting guess
  x = mfalsi.fsolve(efunc, x0)
  print(f"mfalsi: {x:0.5f}")


def test_rtbis():
  x0 = (1, 5)  # starting guess
  x = rtbis.fsolve(efunc, x0)
  print(f"rtbis: {x:0.5f}")


def test_broyden():
  x0 = 1  # starting guess
  x = broyden.fsolve(efunc, x0)
  print(f"broyden: {x:0.5f}")


if __name__ == "__main__":

  # selected tests
  test_illinois()
  test_newt()
  test_aitken()
  test_polynewt()
  test_halley()
  test_brent()
  test_mfalsi()
  test_rtbis()
  test_broyden()
