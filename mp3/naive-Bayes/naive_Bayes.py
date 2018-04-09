from loaddata import *
import numpy as np
import math
import matplotlib.pyplot as plt


np.set_printoptions(threshold=np.nan, precision=2)

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
            accuracy is the evaluation for the classification for each digit.
                key: digit index
                value: percentage of accuracy
        '''
        self.training_data = training_data
        self.testing_data = testing_data
        self.priors = {}
        self.likelihoods_zero = {}
        self.likelihoods_one = {}
        self.posteriori = {}
        self.accuracy = {}

    def calculate_priors(self):
        '''
            Calculate priors probability for each digit, according to training_data set.
            To make life easier, log them.
        '''
        total_count = 0
        for index, digit_object in self.training_data.items():
            self.priors[index] = digit_object.number_of_tokens()
            total_count += digit_object.number_of_tokens()
        for k, v in self.priors.items():
            self.priors[k] /= total_count
            self.priors[k] = math.log(self.priors[k])
        return self.priors

    def all_likelihoods(self):
        '''
            Obtain the likehoods from the training data set.
            First loop: obtain the matrix of likelihoods for each digit.
            Second & Third loop: log them.
        '''
        self.calculate_priors()
        for class_idx, class_obj in self.training_data.items():
            self.likelihoods_zero[class_idx], self.likelihoods_one[class_idx] = class_obj.likelihoods(0.01)
            # print(self.likelihoods_zero[class_idx])
        for k, v in self.likelihoods_zero.items():
            self.likelihoods_zero[k] = np.log(v)
        for k, v in self.likelihoods_one.items():
            self.likelihoods_one[k] = np.log(v)

    def calculate_posteriori(self, image, digit):
        '''
            Posteriori:
                P(class|observed) = log(prior) + log(specific likelihood)
            Given digit(prior), calclulate posteriori for this image.
                Observation is this image. To be specific, each pixel.
        '''
        posteriori = self.priors[digit]
        # print(self.priors)
        for (x, y), value in np.ndenumerate(image):
            if value == 0:
                posteriori += self.likelihoods_zero[digit][x][y]
            else:
                posteriori += self.likelihoods_one[digit][x][y]
        # print(posteriori)
        return posteriori

    def MAP_evaluation(self, image):
        '''
            For one image, what is the posteriori of each image? Return the greatest prediction.
        '''
        posteriori_list = []
        # for image in self.testing_data[digit].tokens:
        for digit in range(10):
            posteriori_list.append(self.calculate_posteriori(image, digit))
        return np.argmax(np.array(posteriori_list) )

    def confusion_matrix(self):
        self.all_likelihoods()
        confusion_matrix = np.zeros((10, 10))
        for class_idx, obj_idx in self.testing_data.items():
            prediction_count = np.zeros(10)
            for image in obj_idx.tokens:
                prediction = self.MAP_evaluation(image)
                prediction_count[prediction] += 1
            # prediction_count = np.array(prediction_count)
            # print(prediction_count)
            prediction_percent = prediction_count / prediction_count.sum()
            confusion_matrix[class_idx] = prediction_percent
        print(confusion_matrix)
        return confusion_matrix

    def odds_ratio(self, a, b):
        self.all_likelihoods()
        fig, ax = plt.subplots(1, 3)
        pcm = ax[0].imshow(self.likelihoods_one[a], cmap="jet")
        fig.colorbar(pcm, ax=ax[0])
        pcm = ax[1].imshow(self.likelihoods_one[b], cmap="jet")
        fig.colorbar(pcm, ax=ax[1])
        pcm = ax[2].imshow(self.likelihoods_one[a]-self.likelihoods_one[b], cmap="jet")
        fig.colorbar(pcm, ax=ax[2])
        # fig.show()
        plt.savefig("foo.png")
