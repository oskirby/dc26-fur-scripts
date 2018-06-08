"""Emotes test"""

import dcfurs
import random

class emotes:
  frames = [
    ## Anger
    [0x00000, 0x10002, 0x08004, 0x04008, 0x02010, 0, 0],
    ## X.X
    [0x00000, 0x11022, 0x0a014, 0x04008, 0x0a014, 0x11022, 0],
    ## -.-
    [0x00000, 0x00000, 0x00000, 0x0e01c, 0x00000, 0, 0],
    ## "."
    [0x00000, 0x00000, 0x0a014, 0x0a014, 0x00000, 0, 0],
    ## c.c
    [0x00000, 0x00000, 0x0f03c, 0x01020, 0x01020, 0, 0],
    ## ?.?
    [0x0e01c, 0x11022, 0x11022, 0x0c018, 0x04008, 0, 0x04008],
    ## #.#
    [0x00000, 0x0a014, 0x1f03e, 0x0a014, 0x1f03e, 0x0a014, 0],
    ## \\.\\
    [0x00000, 0x00000, 0x0a00a, 0x0a00a, 0x14014, 0x14014, 0],
    ## @.@
    [0x0e01c, 0x11022, 0x2c859, 0x2a855, 0x2e85d, 0x19032, 0x02004],
    ## !.!
    [0x00000, 0x04004, 0x04004, 0x04004, 0x04004, 0x00000, 0x04004],
    ## ~.^
    [0x00000, 0x04000, 0x0a014, 0x1100a, 0, 0, 0],
    ## o.o
    [0x00000, 0x00000, 0x04008, 0x0a014, 0x0a014, 0x04008, 0],
    ## O.o
    [0x00000, 0x00018, 0x04024, 0x0a024, 0x0a024, 0x04018, 0],
    ## O.O
    [0x00000, 0x06018, 0x09024, 0x09024, 0x09024, 0x06018, 0],
    ## ` . `
    [0x00000, 0x10002, 0x08004, 0, 0, 0, 0],
    ## u.u
    [0x00000, 0x00000, 0x00000, 0x11022, 0x1f03e, 0, 0],
    ## >.<
    [0x00000, 0x04008, 0x02010, 0x01020, 0x02010, 0x04008, 0],
    ## =.=
    [0x00000, 0x00000, 0x0f03c, 0x00000, 0x0f03c, 0, 0],
    ## 9.9
    [0x06018, 0x09024, 0x09024, 0x0e038, 0x08020, 0x09024, 0x06018],
  ]

  def __init__(self):
    self.interval = 1000
    self.frame = 0

  def draw(self):
    dcfurs.set_frame(self.frames[self.frame])
    self.frame = (self.frame + 1) % len(self.frames)