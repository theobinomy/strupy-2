rffrom reportlab.pdfgen import canvas
import matplotlib.pyplot as plt

eqs = r"$F_G = G\frac{m_1m_2}{r^2}$"
#c = canvas()
from reportlab.lib.units import cm

c = canvas.Canvas('hello2.pdf')
mms = plt.text(-.9, .42, r'gamma: $\gamma$', {'color': 'r', 'fontsize': 20})
plt.show()
c.addLiteral(mms)
#c.drawString(9*cm, 22*cm, mms)
c.showPage()
c.save()

