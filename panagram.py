def panagram(strs):
    length = len(strs)
    if (length < 26) or (length == 26 and strs.isdigit()):
        return False
    else:
        strs_sorted_set = set(sorted(strs))
        if len(strs_sorted_set) <26:
            return False
        else:
            return True


if __name__ == '__main__':
    sentence = "thequickbrownfoxerthelazydog"
    op = panagram(sentence)
    print(op)
