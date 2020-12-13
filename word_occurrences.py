def main():
    list_text = {}
    text = input("text: ")
    raw_arr = text.split()
    raw_arr.sort()
    for i in raw_arr:
        if i in list_text:
            count = list_text[i]
            count += 1
            list_text[i] = count
        else:
            list_text.update({i: 1})


    for i in list_text:
        print("{} : {}".format(i, list_text[i]))


if __name__ == '__main__':
    main()
