import numpy as np

class Digit(object):
    '''
        one digit object represents one class of tokens;
        digit: 0--9;
        tokens: list of matrix/image;
    '''
    def __init__(self, digit):
        '''
            digit: 0--9
            tokens: all the related images
            matrix_zero: the frequency matrix of 0
            matrix_one: the frequency matrix of 1
        '''
        self.digit = digit
        self.tokens = []
        self.matrix_one = np.zeros((32, 32))
        self.matrix_zero = np.zeros((32, 32))


    def add_token(self, image):
        '''
            image is raw data, a list of str-lists;
            ["00000000000000", "0000001000000"]
            Add a image to the list;
        '''
        image = list(map(lambda x: x.rstrip(), image)) # Erase "\n"
        image2str = "".join(image)
        str2list = [int(i) for i in image2str]
        matrix = np.array(str2list).reshape(32, 32)
        self.tokens.append(matrix)
        return matrix

    def print_tokens(self):
        '''
            Print all the tokens in this class.
        '''
        for i in self.tokens:
            print(i)

    def print_token(self, index):
        '''
            Print a specific token in this class.
        '''
        print(self.tokens[index])

    def calculate_frequency_matrix(self):
        '''
            Calculate the # of times pixel (i, j) has value 0/1
            return two matrice
        '''
        for token in self.tokens:
            for i in range(32):
                for j in range(32):
                    if token[i][j] == 1:
                        self.matrix_one[i][j] += 1
                    else:
                        self.matrix_zero[i][j] += 1
        return self.matrix_zero, self.matrix_one
