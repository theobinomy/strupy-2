from mako.template import Template
import rst2pdf

mytemplate = Template('''


hello, ${name}, ${fancy}!
-------------------------





''')
print(mytemplate.render(name="jack", fancy="j1ack"))

zz = mytemplate.render(name="jack", fancy="j1ack")

print(zz)

c = rst2pdf(zz, output11.pdf)