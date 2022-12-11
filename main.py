from fileinput import FileInput


def main():
    file = FileInput('input.txt')
    print(file.get_content())


if __name__ == '__main__':
    main()
