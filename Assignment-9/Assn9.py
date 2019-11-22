from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble
import matplotlib.pyplot as plt


class Evaluation:
    def __init__(self):
        self.cancer = load_breast_cancer()
        # Split data into training and test sets
        # Test size is to define how much of the data set goes to the test size
        self.X_train, self.X_test, self.y_train, self.y_test \
            = train_test_split(self.cancer.data, self.cancer.target, test_size=0.9)
        self.tree_score = 0
        self.bagging_score = {}
        self.boost_score = {}
        self.forest_score = {}

    def decision_tree(self):
        tree_one = tree.DecisionTreeClassifier(criterion="gini").fit(self.X_train, self.y_train)
        self.tree_score = tree_one.score(self.X_test, self.y_test)
        print(self.tree_score)

    def bagging(self):
        # n_estimators = # of trees
        for i in range(1,26):
            bagging = ensemble.BaggingClassifier(tree.DecisionTreeClassifier(), n_estimators=i).fit(self.X_train, self.y_train)
            self.bagging_score[i] = bagging.score(self.X_test, self.y_test)
        keys = list(self.bagging_score.keys())
        values = list(self.bagging_score.values())
        plt.plot(keys, values, 'ro')
        plt.axis([0,27,0,1])
        plt.show()

    # def forest(self):


    # def boost(self):


    # def summary(self):


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    # exp.forest()
    # exp.boost()
    # exp.summary()