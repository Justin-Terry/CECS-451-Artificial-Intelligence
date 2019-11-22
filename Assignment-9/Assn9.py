from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn import tree, ensemble


class Evaluation:
    def __init__(self):
        self.cancer = load_breast_cancer()
        self.X_train, self.X_test, self.y_train, self.y_test \
            = train_test_split(self.cancer.data, self.cancer.target, test_size=0.9)
        self.tree_score = 0
        self.bagging_score = {}
        self.boost_score = {}
        self.forest_score = {}

    def decision_tree(self):


    def bagging(self):


    def forest(self):


    def boost(self):


    def summary(self):


if __name__ == '__main__':
    exp = Evaluation()
    exp.decision_tree()
    exp.bagging()
    exp.forest()
    exp.boost()
    exp.summary()