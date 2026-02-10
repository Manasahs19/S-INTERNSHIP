class Payment:
    def pay(self):
       print("Payment method")

class GooglePay(Payment):
    def pay(self):
        print("GooglePay method")

class PhonePe(Payment):
    def pay(self):
        print("PhonePay method")

class CreditCard(Payment):
    def pay(self):
        print("CreditCard method")

P = Payment()
P.pay()
GP = GooglePay()
GP.pay()
PP = PhonePe()
PP.pay()
CC = CreditCard()
CC.pay()