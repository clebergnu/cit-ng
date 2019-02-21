from varianter_cit import Cit


def data_converter(file_name):
    """
    In casa_tables folder are old data with different format, this function converts data to  known format
    :param file_name: index of data file
    :return: parameters and constraints
    """
    data = open("./casa_tables/parameter" + file_name + ".txt").readline()
    data = data.split()
    parameters = [[]] * len(data)
    counter = 0
    constraints = []
    for i in range(len(data)):
        array = []
        data[i] = int(data[i])
        for j in range(data[i]):
            array.append(counter)
            counter += 1
        parameters[i] = array
    constraint = open("./casa_tables/constraint" + file_name + ".txt").read().split('\n')
    for line in constraint:
        output = ""
        if line[0] == "-":
            line = line.replace("-", "")
            line = line[1:]
            pom = line.split()
            for index in range(len(pom)):
                for i in range(len(parameters)):
                    for j in range(len(parameters[i])):
                        if int(pom[index]) == parameters[i][j]:
                            if index < len(pom) - 1:
                                output = output + str(i) + " != " + str(j) + " || "
                                break
                            else:
                                output = output + str(i) + " != " + str(j)
                                break
            constraints.append(output)
    return data, constraints


def print_final_list(final_list):
    for i in range(len(final_list)):
        print("T" + "{}".format(i) + " is ", end='')
        for j in range(len(final_list[i])):
            print(final_list[i][j], end='')
            if j != len(final_list[i]) - 1:
                print(",", end='')
        print()


def main():
    "manual data addition"
    # input_data = "2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2"
    # t_value = 3
    # constraints = []
    #
    # input_data = input_data.split()
    # for i in range(len(input_data)):
    #     input_data[i] = int(input_data[i])

    # Reading data from casa_tables i is the index of datafile
    t_value = 2
    i = 23
    input_data, constraints = data_converter(str(i))

    # Computing
    program = Cit.Cit(input_data, t_value, constraints)
    # start_time = time.process_time()
    final_list = program.compute()

    print()
    print("---final_list " + str(i) + " ---")
    print_final_list(final_list)
    print()
    print("size: " + str(len(final_list)))
    print("data size: " + str(len(input_data)))
    print()
    # print("--- %s seconds ---" % (time.process_time() - start_time))


if __name__ == "__main__":
    main()
