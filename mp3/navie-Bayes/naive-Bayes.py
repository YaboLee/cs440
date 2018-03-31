from loaddata import *

training_data = load_training()
testing_data = load_testing()

class NB(onject):
    def __init__(self, training_data, testing_data):
        self.training_data = training_data
        self.testing_data = testing_data
        self.priors = {}

    def priors(self):
        total_count = 0
        for index, object in self.training_data.items():
            self.priors[index] = object.number_of_tokens()
            total_count += 
        for i in range
