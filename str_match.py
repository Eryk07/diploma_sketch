class StrMatch():
    def first_algorithm(str1, str2):
        out = True
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                out = False
                break
        return out


                
