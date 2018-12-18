
# input big_type para1 and para2 for one output
# raster:'r',para1;no diffraction :'n';diffraction:


def a(big_type: object = None, para1: object = None, para2: object = None):
    big_type = str(big_type)
    big_type_list = ['r', 'n', 'd']
    if big_type in big_type_list:
        if big_type == 'r' and para1 != '':
            sr = "Raster to {}A".format(para1)
            return sr
        if big_type == 'n':
            print("no diffraction")
        if big_type == 'd' and para1 != '' and para2 != '':
            para2 = int(para2)
            # print('{}A'.format(para1))
            sb = '{} frames,{} degree, 350um att'.format(para2 * 50, para2 * 10)
            return sb
    else:
        print('try again')


def print_results(a_list):
    if a_list[0] == "r":
        for i in range(1, len(a_list)):
            if a_list[i] != '':
                print('{}'.format(a('r', str(a_list[i]))))
            else:
                print('')

    if a_list[0] == "d":
        result_list = []
        for i in range(1, len(a_list)):
            if a_list[i][0] != '' and a_list[i][1] != '':
                print(a('d', str(a_list[i][0]), str(a_list[i][1])))
                result_list.append('{} A'.format(a_list[i][0]))
            else:
                print('')
                result_list.append('')
        for i in result_list:
            if i != ':':
                print(i)
            else:
                print('')
