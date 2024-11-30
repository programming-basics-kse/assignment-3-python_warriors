def write_result_into_file(result_file, results):
    with open(result_file, "w") as file:
        for i, result in enumerate(results):
            file.write(result + "\n")


def output_from_file(text_file):
    with open(text_file, 'r') as result:
        for line in result:
            print(line)