#!/usr/bin/env/python
#
# Using the file system load
#
# We now assume we have a file in the same dir as this one called
# test_template.html
#
import os
import time

from jinja2 import Environment, FileSystemLoader
# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    print(j2_env.get_template('test_template.html').render(
        title='Hellow Gist from GutHub'
    ))

if __name__ == '__main__':
    print_html_doc()

