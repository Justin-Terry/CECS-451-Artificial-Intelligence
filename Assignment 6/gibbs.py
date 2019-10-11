class Gibbs:

    def __init__(self):
        self.cloudy = 0.5
        # prob of sprinkler given C=[t, f]
        self.sprinkler = [0.1, 0.5]
        # prob of rain given C=[t, f]
        self.rain = [0.8, 0.2]
        # prob of wet grass given
        self.wet_grass = [0.99, 0.9, 0.9, 0]










if __name__ == '__main__':
    driver = Gibbs()