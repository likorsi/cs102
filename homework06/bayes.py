import numpy as np
import string

class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha = alpha
        self.labels = []
        self.table = dict()
        self.p_labels = []

    def fit(self, titles, y):

        self.labels = [i for i in set(y)] 

        unic_labels = []
        for i in range(len(self.labels)):
            if self.labels[i] not in unic_labels:
                unic_labels.append(self.labels[i]) 

        self.p_labels = [[0] * 2] * len(unic_labels)
        for i in range(len(self.labels)): 
            self.p_labels[unic_labels.index(self.labels[i])][0] += 1
            self.p_labels[unic_labels.index(self.labels[i])][1] = self.labels[i]

        for i in range(len(self.p_labels)):
            self.p_labels[i][0] /= len(self.labels)

        tr = str.maketrans("", "", string.punctuation)

        for i in range(len(titles)):
            titles[i] = titles[i].translate(tr).lower()
            words = titles[i].split(' ')        
            for word in words:
                if self.table.get(word):
                    self.table[word][unic_labels.index(self.labels[i])] += 1
                else:
                    self.table[word] = [0] * len(unic_labels) * 2
                    self.table[word][unic_labels.index(self.labels[i])] = 1
        
        for key, value in self.table.items():
            for i in range(len(unic_labels)):
                m = self.table.values()
                words_in_label = 0
                for j in len(m):
                    words_in_label += m[j][i] 
                p = (self.alpha + value[k]) / (self.alpha * len(self.table.keys()) + words_in_label)
                self.table[key][i+len(unic_labels)] = p
        

    def predict(self, x):

        result_label = []
        words = set()
        for i in range(len(x)):
            x[i] = x[i].translate(tr).lower()
            words.add(x[i].split(' '))
            sum_log = []
            for i in range(len(self.p_labels)):
                sum_log.append(self.p_labels[0])
            for word in words:
                if self.table[word]:
                    for k in range(len(self.p_labels)):
                        sum_log[k] += np.log(self.table[word][k+len(self.p_labels)])
                    
            result_label[i] = self.p_labels[sum_log.argmax()][1]

        return result_label


    def score(self, X_test, y_test):

        forecast = self.predict(X_test)
        c = 0
        for i in range(len(forecast)):
            if forecast[i] == y_test[i]:
                c += 1
        score = c / len(y_test)
        return score

