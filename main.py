#!/usr/bin/env python3

from generator import Generator
import const

gen = Generator(const.words.words)

print(gen.generate())
