#!/usr/bin/env python3

from generator import Generator
import const

gen = Generator(const.words.words)

for i in range(100):
    fd = open("output/" + str(i) + ".html", "wt")
    fd.write(gen.generate())
    fd.close()
