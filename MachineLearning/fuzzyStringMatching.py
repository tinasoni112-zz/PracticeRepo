def calc_ratio(str1, str2):
    from fuzzywuzzy import fuzz
    return fuzz.ratio(str1, str2)

def calc_partial_ratio(str1, str2):
    from fuzzywuzzy import fuzz
    return fuzz.partial_ratio(str1, str2)

def calc_token_sort_ratio(str1, str2):
    from fuzzywuzzy import fuzz
    return fuzz.token_sort_ratio(str1, str2)

def calc_token_set_ratio(str1, str2):
    from fuzzywuzzy import fuzz
    return fuzz.token_set_ratio(str1, str2)

def match_ratio_for_column(data, col):
    dat



