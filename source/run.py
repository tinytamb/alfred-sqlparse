#!/usr/bin/env python3
# coding: UTF-8
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(current_dir) + '/lib')
import sqlparse

args = sys.argv
input_lines = args[1]

# ==== settings ==== #
settings = {}

settings["keyword_case"] = 'upper'
settings["reindent"] = True

result = sqlparse.format(input_lines, **settings)
print(result)
