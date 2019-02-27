import numpy as np
import string


class NaiveBayesClassifier:

    def __init__(self, alpha=1):
        self.alpha = alpha
        self.labels = []
        self.table = dict()
        self.p_labels = dict()

    def fit(self, titles, y):

        self.labels = [i for i in y] 

        unic_labels = []
        for i in self.labels:
            if i not in unic_labels:
                unic_labels.append(i) 

        for i in range(len(self.labels)):
            if self.p_labels.get(self.labels[i]):
                a = self.p_labels[self.labels[i]]
                a += 1 
                self.p_labels[self.labels[i]] = a
            else:
                self.p_labels[self.labels[i]] = 1      

        for key, value in self.p_labels.items():
            value /= len(self.labels)
            self.p_labels[key] = np.log(value)

        tr = str.maketrans("", "", string.punctuation)

        for i in range(len(titles)):
            titles[i] = titles[i].translate(tr).lower()
            words = titles[i].split(' ')        
            for word in words:
                if self.table.get(word):
                    a = self.table[word]
                    a[unic_labels.index(self.labels[i])] += 1
                    self.table[word] = a
                else:
                    a = [0 for _ in range(len(unic_labels) * 2)]
                    a[unic_labels.index(self.labels[i])] = 1
                    self.table[word] = a
        
        for key, value in self.table.items():
            for i in range(len(unic_labels)):
                m = self.table.values()
                words_in_label = 0
                for j in m:
                    words_in_label += j[i] 
                p = (self.alpha + value[i]) / (self.alpha * len(self.table.keys()) + words_in_label)
                self.table[key][i+len(unic_labels)] = p
        

    def predict(self, x):

        result_label = [[] for _ in range(len(x))]
        tr = str.maketrans("", "", string.punctuation)
        for i in range(len(x)):
            x[i] = x[i].translate(tr).lower()
            words = x[i].split(' ')
            sum_log = [value for value in self.p_labels.values()]

            for word in words:
                if self.table.get(word):
                    for k in range(len(self.p_labels)):
                        sum_log[k] += np.log(self.table[word][k+len(self.p_labels)])
                
            result_label[i] = list(self.p_labels)[np.argmax(sum_log)]

        return result_label


    def score(self, X_test, y_test):

        forecast = self.predict(X_test)
        c = 0
        for i in range(len(forecast)):
            if forecast[i] == y_test[i]:
                c += 1
        score = c / len(y_test)
        return score

