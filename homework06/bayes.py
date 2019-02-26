import numpy as np
import string

class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha = alpha
        self.labels = []
        self.titles = []
        self.table = []


    def fit(self, x, y):
        """ Fit Naive Bayes classifier according to X, y. """
        for i in range(len(y)):
            self.labels[i] = y[i] 

        good, maybe, never = 0, 0, 0
        for i in rabge(len(self.labels)):
            if self.labels[i] == 'good':
                good += 1
            elif self.labels[i] == 'maybe':
                maybe += 1
            elif self.labels[i] == 'never':
                never += 1

        p_maybe = maybe / len(self.labels)
        p_never = never / len(self.labels)
        p_good = good / len(self.labels)

        for i in range(len(x)):
            self.titles[i] = x[i]

        tr = str.maketrans("", "", string.punctuation)

        g = collections.Counter()
        m = collections.Counter()
        n = collections.Counter()

        words = []
        unic_words = set()

        for i in range(len(self.titles)):
            self.titles[i] = self.titles[i].translate(tr).lower()
            words = self.titles[i].split(' ')
            for word in words:
                unic_words.add(word) 
                if self.labels[i] == 'good':
                    g[word] += 1
                elif self.labels[i] == 'maybe':
                    m[word] += 1
                elif self.labels[i] == 'never':
                    n[word] += 1 


        self.table = []
        for i in range(len(unic_words)):
            word = unic_words[i]
            if not g[word]:
                g[word] = 0
            elif not m[word]:
                m[word] = 0
            elif not n[word]:
                n[word] = 0

            self.table[i] = [word, g[word], m[word], n[word]]


    def predict(self, x):
        """ Perform classification on an array of test vectors X. """

        words = set()
        for i in range(len(x))
            self.titles[i] = x[i]
            self.titles[i] = self.titles[i].translate(tr).lower()
            words.add(self.titles[i].split(' '))

        for i in range(len(self.titles))

        result_label = np.argmax(np.log(p_good_d), np.log(p_maybe_d), np.log(p_never_d))


        return result_label

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        forecast = self.predict(X_test)
        c = 0
        for i in range(len(forecast)):
            if forecast[i] == y_test[i]:
                c += 1
        score = c / len(y_test)
        return score

