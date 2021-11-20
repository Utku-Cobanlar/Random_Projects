def cons_count(word):
        word_list = list(word.lower())
        count = 0
        vowels = "aeiou"
        for a in range(0,len(word)):
            if word_list[a] not in vowels:
                count += 1
            else:
                break
        return count
def pig_latin():
    word = input("Enter a word you want igpay atinlayzed: ")
    it_word = list(word.lower())
    vowels = "aeiou"
    out_word = ""
    count_num = cons_count(word)
    for a in range(0,count_num):
        out_word = it_word[a+1:] + it_word[0:a+1] + ["ay"]
    return "".join(out_word)
