from docutils.core import publish_doctree
import rst2pdf
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Frame

rest_text = """
This is a paragraph. It has a link: http://rst2pdf.ralsina.me and then some random text.

+-------------+---------------------------+
| A table     | With cells                |
|             |                           |
|             |                           |
|             |                           |
|             |                           |
+-------------+---------------------------+
| And inside                              |
| it some                                 |
| more text                               |
|                                         |
|                                         |
+-----------------------------------------+

* And a list
* Just to make it harder

    + with a nested item here
"""
r2p = rst2pdf.version.
doctree = publish_doctree(rest_text)
story = r2p.gen_elements(doctree)
canv = Canvas("platypus-rest.pdf")
f = Frame(2 * cm, 2 * cm, 16 * cm, 18 * cm, showBoundary=True)
f.addFromList(story, canv)
canv.save()