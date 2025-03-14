lass bank:
  def__init__(self,balance=0):
    self.balance=balance
    def invest(self,amount):
      self.balance+=amount
      print(f"current balance{self.balance}")
      def withdraw(self,amount):
        if amount<balance:
          self.balance-=amount
          print(f"current balance{self.balance}")
        else:
          print(f"current balance{self.balance}")
          
  obj1=bank()
  obj1.invest(100) 
  obj1.withdraw(50)       
          
