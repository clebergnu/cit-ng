from varianter_cit import Cit
from varianter_cit.Parser import Parser


def print_final_list(final_list, parameters):
    for i in range(len(final_list)):
        print("T" + "{}".format(i) + " is ", end='')
        for j in range(len(final_list[i])):
            print(parameters[j].values[final_list[i][j]], end='')
            if j != len(final_list[i]) - 1:
                print(",", end='')
        print()


def main():

    # Reading data from casa_tables i is the index of datafile
    parameters, constraints = Parser.parse(open("./data_file_example.txt"))
    t_value = 2

    input_data = [parameter.get_size() for parameter in parameters]
    # Computing
    program = Cit.Cit(input_data, t_value, constraints, True)
    # start_time = time.process_time()
    final_list = program.compute()

    print()
    print("---final_list ---")
    print_final_list(final_list, parameters)
    print()
    print("size: " + str(len(final_list)))
    print("data size: " + str(len(input_data)))
    print()
    # print("--- %s seconds ---" % (time.process_time() - start_time))


if __name__ == "__main__":
    main()
