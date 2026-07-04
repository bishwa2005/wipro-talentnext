if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7]
    output_dict = {n: n**3 for n in input_list if n % 2 == 1}

    print("Input list:", input_list)
    print("Output dictionary:", output_dict)
