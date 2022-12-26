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
    def pays(self, bill):
        pass

class PdfReport:
    """
    Creates a Pdf file that contains the about flatmates
    such as their names, their due amount and the period
    of the bill.
    """

    def __init__(self, days_in_house):
        self.days_in_house = days_in_house

    def generate(self, flatmate1, flatmate2, bill):
        pass


