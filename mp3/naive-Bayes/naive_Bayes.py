from loaddata import *
import numpy as np
import math


training_data = load_training()
testing_data = load_testing()

class NB(object):
    def __init__(self, training_data, testing_data):
        '''
            training_data is a dictionary of all the classes(0--9) from training_data. Details are denoted in the Digit.py
            testing_data is a dictionary of the classes(0--9) from testing_data. Details are denoted in the Digit.py
                key: digit index
                value: digit object
            priors is a dictionary of priors probability for each digit.
                key: digit index
                value: probability
            posteriori is a dictionary of posteriori probability of each digit.
                key: digit index
                value: probability
        '''
        self.training_data = training_data
        self.testing_data = testing_data
        self.priors = {}

        self.posteriori = {}

    def calculate_priors(self):
        '''
            Calculate priors probability for each digit, according to training_data set.
        '''
        total_count = 0
        for index, object in self.training_data.items():
            self.priors[index] = object.number_of_tokens()
            total_count += object.number_of_tokens()
        for k, v in self.priors.items():
            self.priors[k] /= total_count
        return self.priors

    def calculate_posteriori(self):
        '''
            Calculate posteriori probability for each digit.
                likelihoods are calculated by method of digit object.
        '''
        for index, object in self.training_data.items():
            likelihoods_zero, likelihoods_one = object.priors()
            self.posteriori[index] = np.log(likelihoods_one).sum() + math.log1p(self.priors[index])
        return self.posteriori
