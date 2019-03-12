def distance_Hamming_raw(str1, str2):
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs

def distance_Hamming(str1, str2):
    max_len = len(str1)
    if len(str2) > len(str1):
        max_len = len(str2)

    if max_len == 0:
        max_len = 1

    return (max_len - (distance_Hamming_raw(str1, str2)))/max_len

def distance_Levenshtein_raw(str1, str2):
    if len(str1) < len(str2):
        return distance_Levenshtein(str2, str1)

    # len(s1) >= len(s2)
    if len(str2) == 0:
        return len(str1)

    previous_row = range(len(str2) + 1)
    for i, c1 in enumerate(str1):
        current_row = [i + 1]
        for j, c2 in enumerate(str2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def distance_Levenshtein(str1, str2):
    max_len = len(str1)
    if len(str2) > len(str1):
        max_len = len(str2)

    if max_len == 0:
        max_len = 1

    return (max_len - (distance_Levenshtein_raw(str1, str2)))/max_len

def distance_Jaro(str1, str2):
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

def distance_Jaro_Winkler(str1, str2, p = 0.1):
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

    dj = distance_Jaro(str1,str2)
    return (dj + l * p * (1 - dj))

def distance_Ratcliff_Obershelp(str1, str2):
    answer = "."
    len1, len2 = len(str1), len(str2)
    if len1 == 0 and len2 == 0:
        return 1
    Km = 0
    while(answer != ""):
        answer = largest_common_substring(str1,str2)
        str1 = str1.replace(answer,"")
        str2 = str2.replace(answer,"")
        Km = Km + len(answer)

    return (2 * Km / (len1 + len2))
def largest_common_substring(str1,str2):
    answer, match,lcs_temp = "", '', 0
    len1, len2 = len(str1), len(str2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp=0
            match=''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and str1[i+lcs_temp] == str2[j+lcs_temp]):
                match += str2[j+lcs_temp]
                lcs_temp+=1
            if (len(match) > len(answer)):
                answer = match
    return answer