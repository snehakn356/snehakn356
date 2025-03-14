Class A:
def feature1(self):
  print("Feature1")

Class B:
def feature2(self):
  print("Feature2")

Class C(A,B):
pass

obj=C()
obj.feature1()
