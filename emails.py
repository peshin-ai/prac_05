def main():
    listpp ={}
    string = input('Email: ')
    while string != '':
        full_name = string.split('@')
        name = full_name[0].split('.')
        try:
            check = input('is your name {} {}? (Y/n)'.format(name[0], name[1])).lower()
        except IndexError:
            check = input('is your name {}? (Y/n)'.format(name[0])).lower()

        if check == 'y':
            person =''
            try:
                person += name[0] + ' ' + name[1]
            except IndexError:
                person += name[0]
            listpp.update({person: string})
            string = input('Email: ')
        else:
            person = input('Name: ')
            listpp.update({person: string})
            string = input('Email: ')
    print()
    for key, value in listpp.items():
        print('{} ({})'.format(key, value))

if __name__ == '__main__':
    main()