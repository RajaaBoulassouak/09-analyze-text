def analyze_text(text):
    alphas_num = 0
    for index in range(len(text)):
        if text[index].isalpha():
            alphas_num = alphas_num + 1

    count_e = text.count('e') + text.count('E')
    percent = count_e / alphas_num * 100
    percent = "%.2f" % percent
    return(f"The text contains {alphas_num} alphabetic characters, of which {count_e} ({percent}%) are 'e'.")
