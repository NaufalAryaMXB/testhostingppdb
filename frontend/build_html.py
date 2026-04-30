#!/usr/bin/env python3
"""Assemble parts into final index.html"""
import subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run(["python","build_part1.py"],check=True)
subprocess.run(["python","build_part2.py"],check=True)
with open("_part1.html","r",encoding="utf-8") as f: p1=f.read()
with open("_part2.html","r",encoding="utf-8") as f: p2=f.read()
with open("index.html","w",encoding="utf-8") as f: f.write(p1+p2)
os.remove("_part1.html")
os.remove("_part2.html")
print("index.html assembled successfully!")
