def analyze_text(text):
    alphas_num = 0
    for index in range(len(text)):
        if text[index].isalpha():
            alphas_num = alphas_num + 1

    count_e = text.count('e') + text.count('E')
    percent = count_e / alphas_num * 100
    percent_rounded = "%.2f" % percent
    result = "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'."
    return(result.format(alphas_num, count_e, percent_rounded))
