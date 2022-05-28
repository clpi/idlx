#!/usr/bin/env python3.10

import os, sys
from sys import argv, stderr, stdout, exit
from subprocess import call
from tempfile import mkdtemp
from shutil import rmtree
from argparse import ArgumentParser

IDLEX_DIR = os.path.dirname(os.path.abspath(__file__))
ccsrc = os.path.join(IDLEX_DIR, "cc", "src")
sys.path.append(ccsrc)

olddir = os.getcwd()
debug = False
program: str | None = None
clang = ["clang++", '-emit-llvm', 'c', '-g']
linker = "llvm-link"
cmd = []
files = []

def _err(msg):
    stdout.flush()
    stderr.flush()
    stderr.write(f"\x1b[31;1m[ ERROR ]\x1b[0m {msg}\n")

def install():
    pass
