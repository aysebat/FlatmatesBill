from flat import Bill, Flatmate
from pdfGen import PdfReport
from pdfGen import FileSharer

bill_amount = float(input("Please, enter the bill amount, bill: "))
bill_period = input("Enter the bill period, Month Year: ")
name1 = input("Name of the first flatmate: ")
flatmate1_days = float(input(f"Number of days for the {name1}: "))
name2 = input("Name of the second Flatmate: ")
flatmate2_days = float(input(f"Number of days for the {name2}: "))

the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=name1, days_in_house=flatmate1_days)
flatmate2 = Flatmate(name=name2, days_in_house=flatmate2_days)

print(f" {flatmate1.name} Pays: ",flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f" {flatmate2.name} Pays: ",flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"Report_of_bill.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

fileshare = FileSharer(filepath=pdf_report.filename)
print(fileshare.share())