import os
import webbrowser
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Creates a Pdf file that contains the about flatmates
    such as their names, their due amount and the period
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill Report', border=0, align='C', ln=1)

        # add the period and value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt="Period ", border=0)
        pdf.cell(w=10, h=40, txt=":", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # add flatmates1
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=10, h=40, txt=":", border=0)
        pdf.set_font(family='Times', size=18)
        pdf.cell(w=100, h=40, txt=flatmate1_pay, border=0, ln=1)

        # add flatmates2
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=10, h=40, txt=":", border=0)
        pdf.set_font(family='Times', size=18)
        pdf.cell(w=100, h=40, txt=flatmate2_pay, border=0, ln=1)

        os.chdir("Report")
        #generate the pdf file
        pdf.output(self.filename)
        #automaticaly open the pdf file
        webbrowser.open('file://' + os.path.realpath(self.filename))


class FileSharer:
    """Uploading a pdf file filstack and share the URL"""

    def __init__(self, filepath, api_key="Ay8jx9TiXQD6Cr93xc8tpz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
