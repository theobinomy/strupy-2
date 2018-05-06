#!/usr/bin/env/python
#
# More of a reference of using jinaj2 without actual template files.
# This is great for a simple output transformation to standard out.
#
# Of course you will need to "sudo pip install jinja2" first!
#
# I like to refer to the following to remember how to use jinja2 :)
# http://jinja.pocoo.org/docs/templates/
#
from jinja2 import Environment



HTML = """
<html>
<head>
<title>{{ title }}</title>
</head>
<body>
Hello.
</body>
</html>
"""

def print_html_doc():
    print(Environment.from_string(HTML).render(title='Hellow Gist from GutHub'))

if __name__ == '__main__':
    print_html_doc()