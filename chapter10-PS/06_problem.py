from random import randint 
class Train:
    def __init__(slf,TrainNo):#so there was No error self=slf
        slf.TrainNo=TrainNo
    def book(Raj,fro,to):#there was no error self=raj
        print(f'Ticket is booked in train no {Raj.TrainNo} from {fro} To {to}')
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