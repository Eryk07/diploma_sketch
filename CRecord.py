import str_match as sm

class CRecord():
    str1 = ""
    str2 = ""
    dist_Ham = 0.0
    dist_Lev = 0.0
    dist_Jaro = 0.0
    dist_Jaro_Wink = 0.0

    def fill(self,s1,s2):
        self.str1 = s1
        self.str2 = s2
        self.calc_factors()

    def calc_factors(self):
        self.dist_Ham = sm.distance_Hamming(self.str1, self.str2)
        self.dist_Lev = sm.distance_Levenshtein(self.str1, self.str2)
        self.dist_Jaro = sm.distance_Jaro(self.str1, self.str2)
#        self.dist_Jaro_Wink = sm.distance_Jaro_Winkler(self.str1, self.str2)
