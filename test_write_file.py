from functions.get_file_content import write_file


def main():
    working_directory = "calculator"
    result = write_file(working_directory,  "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    result = write_file(working_directory, "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    result = write_file(working_directory, "/tmp/temp.txt", "this should not be allowed")
    print(result)


main()