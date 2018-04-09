from naive_Bayes import *

nb = NB(training_data, testing_data)
nb.confusion_matrix()
# nb.odds_ratio(1, 8)




# def start():
#     nb = NB(training_data, testing_data)
#     return nb
#
# def show_confusion_matrix():
#     return nb.confusion_matrix()
#
#
#
# if __name__ == "main":
#     start()
#     show_confusion_matrix()
