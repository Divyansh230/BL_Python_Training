class Walker:
    def walk(self):
        print("walking...")

class Runner:
    def run(self):
        print("Running...")



class Athelete(Walker,Runner):
    def __init__(self,training_hours):
        self.training_hours = training_hours
    def train(self ):
        print(f'Athelete is trainig for {self.training_hours} hours')

athelete=Athelete(10)
athelete.walk()
athelete.run()
athelete.train()

