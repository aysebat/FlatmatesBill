import os.path
import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contain data about a bill,
    such as total amount of  period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
class Flatmate:
    """
    Creates a flatmate person who lives un the flat
    and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house    
    def pays(self, bill, flatmate2):
        weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

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

        #Add icon
        pdf.image("files/house.png", w=30, h=30)

        #Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill Report', border=0, align='C', ln=1)

        #add the period and value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt="Period ", border=0)
        pdf.cell(w=10, h=40, txt=":", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #add flatmates1
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

        #generate the pdf file
        pdf.output(self.filename)

        #automaticaly open the pdf file
        webbrowser.open('file://'+os.path.realpath(self.filename))



the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("Johns Pays",john.pays(bill=the_bill, flatmate2=marry))
print("Marry Pays",marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)