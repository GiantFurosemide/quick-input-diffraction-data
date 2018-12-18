

'''run a input and return a d_list'''


def make_result_list():
    diffraction_results_list = []
    diffraction_description_list = []
    for i in range(16):
        diffraction_results = input("row {} diffraction = ? A:".format(i+1))
        diffraction_results_list.append(diffraction_results)

    for i in range(16):
        diffraction_description = input("row {} description scale is ?:  ".format(i+1))
        diffraction_description_list.append(diffraction_description)

    return diffraction_description_list, diffraction_results_list


def d_list_standard():
    b, a = make_result_list()
    c = [(a[i], b[i]) for i in range(len(a))]
    d = ['d']
    for i in c:
        d.append(i)
    return d


