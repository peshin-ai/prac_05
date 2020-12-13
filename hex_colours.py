def main():
    HEX_list = {'coral': '#ff7f50', 'cyan1': '#00ffff', 'GreenYellow': '#adff2f',
                'LightGoldenrodYellow': '#fafad2', 'NavyBlue': '#000080', 'yellow1': '#ffff00',
                'LightPink': '#FFB6C1', 'SandyBrown': '#F4A460', 'LavenderBlush': '#FFF0F5d'}

    name = input('enter your color: ').lower()
    while name != '':
        if name in HEX_list:
            print(HEX_list[name])
        name = input('enter your color: ').lower()

if __name__ == '__main__':
    main()
