
from reportlab.pdfgen import canvas

txt = open('./demo.txt', 'r').readlines()
print(txt)


# def generatePDF():
#     c = canvas.Canvas('demo90.pdf', pagesize=(595.27, 841.89)) # A4 size.
#     c.drawString(50, 780, readfile('./demo.txt')) #(x, y) => (50, 780)
#     c.showPage()
#     c.save()

# generatePDF()
cvs = canvas.Canvas('demo91.pdf', pagesize=(595.27, 841.89)) # A4 size.
def generatePDF(c):
    for i in txt: 
        print(i)
        c.drawString(50, 780, i) #(x, y) => (50, 780)
    c.showPage()
    c.save()

generatePDF(cvs)