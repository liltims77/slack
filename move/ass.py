




def calc_prob(self):
    if self.logic == 0:  # Leaf node
        return self.prob
    elif self.logic == 1:  # OR gate
        prob = self.child.calc_prob()
        sibling = self.child.sibling
        while sibling:
            prob = 1 - (1 - prob) * (1 - sibling.calc_prob())
            sibling = sibling.sibling
        return prob
    elif self.logic == 2:  # AND gate
        prob = self.child.calc_prob()
        sibling = self.child.sibling
        while sibling:
            prob *= sibling.calc_prob()
            sibling = sibling.sibling
        return prob
