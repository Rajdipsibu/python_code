from random import randint 
class Train:
    def __init__(self,TrainNo):
        self.TrainNo=TrainNo
    def book(self,fro,to):
        print(f'Ticket is booked in train no {self.TrainNo} from {fro} To {to}')
    def getStatus(self,):
        print(f"the train no:{self.TrainNo} is on time.")
    def getFare(self,fro,to):
        print(f"Ticket Fare in train no {self.TrainNo} from {fro} To {to} is {randint(222,444)}")


t1=Train(12866)
# t1.TrainNo=12085
t1.fro='Midnapore'
t1.to='khargapur'
t1.book('Midnapore','khargapur')
t1.getStatus()
t1.getFare('Midnapore','khargapur')