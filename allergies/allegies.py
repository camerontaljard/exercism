__author__ = 'cameron'


allergens = dict(
    eggs=1, peanuts=2, shellfish=4,
    strawberries=8, tomatoes=16, chocolate=32,
    pollen=64, cats=128
    )


so_allergens = sorted(allergens.items(), key=lambda x: x[1], reverse=True)


class Allergies(object):

    def __init__(self, score):
        self.list = []

        for sym in so_allergens:
            if score >= sym[1]:
                score -= sym[1]
                self.insert(0, sym[0])

            while score <= sym[1]:
                score -= sym[1]

        print self.list


        def is_allergic_to(self, allergy):
            if allergy in self.list:
                return True
            return False







