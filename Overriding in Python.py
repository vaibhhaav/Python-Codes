class P:
    def properties_status(self):
        print('Moneym Land, Gold')
    def to_marry(self):
        print('Anushka')

class C(P):
    def study_status(self):
        print("Sudies done waiting for job")
    def to_marry(self):
        print('Megha')

c = C()
c.properties_status()
c.study_status()
c.to_marry()