class StrMatch():
    #def index_jaccard(self):
    def distance_Hamming(self, str1, str2):
        diffs = 0
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 1
        return diffs

    def distance_Levenshtein(self, str1, str2):
        if str1 == "":
            return len(str2)
        if str2 == "":
            return len(str1)
        if str1[-1] == str2[-1]:
            cost = 0
        else:
            cost = 1

        res = min([LD(str1[:-1], str2) + 1,
                   LD(str1, str2[:-1]) + 1,
                   LD(str1[:-1], str2[:-1]) + cost])
        return res

    def distance_Jaro(self, str1, str2):
        str1_len = len(str1)
        str2_len = len(str2)

        if str1_len == 0 and str2_len == 0:
            return 1

        match_distance = (max(str1_len, str2_len) // 2) - 1

        str1_matches = [False] * str1_len
        str2_matches = [False] * str2_len

        matches = 0
        transpositions = 0

        for i in range(str1_len):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, str2_len)

            for j in range(start, end):
                if str2_matches[j]:
                    continue
                if str1[i] != str2[j]:
                    continue
                str1_matches[i] = True
                str2_matches[j] = True
                matches += 1
                break

        if matches == 0:
            return 0

        k = 0
        for i in range(str1_len):
            if not str1_matches[i]:
                continue
            while not str2_matches[k]:
                k += 1
            if str1[i] != str2[k]:
                transpositions += 1
            k += 1

        return ((matches / str1_len) +
                (matches / str2_len) +
                ((matches - transpositions / 2) / matches)) / 3

    def distance_Jaro_Winkler(self, str1, str2, p = 0.1):
        l = 0
        if(len(str1) < len(str2)):
            min_len = len(str1)
        else:
            min_len = len(str2)

        for i in range(min_len):
            if str1[i]==str2[i]:
                l+=1
            else:
                break
        return (distance_Jaro(str1,str2) + l*p(1-distance_Jaro(str1,str2)))
