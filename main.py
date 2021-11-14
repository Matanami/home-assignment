def missing_num(num_list):
    """
    find the missing number between 0-9
    :param num_list:list of 9 number between 0-9
    :return: the missing number between 0-9
    """
    sum_list = sum(num_list)
    sum_max = sum(range(10))
    return sum_max - sum_list


def sum_of_all():
    """
    calculate sum of user input
    :return: sum of the user input
    """
    sum_input = 0
    while True:
        input_user = input("Enter a number to add or stop to exist")
        if input_user == "stop":
            break
        else:
            try:
                num_input = int(input_user)
                sum_input += num_input
            except:
                print("the input is not a integer or stop ")
    return sum_input



