
class Trebuchet:
    def __init__(self, file):
        self.input_file = file
        self.sum = 0
        self.runner()

    def runner(self):
        file_lines = open(self.input_file, 'w', encoding="utf-8")
        with open('input.txt', encoding="utf-8") as file_lines:
            data = file_lines.read()
            for line in data:
                print(line)
                self.sum = self.sum + self.find_first_val() + self.find_second_val()
        print("THE ANSWER IS")
        print(self.sum)

    def find_first_val(self, line):
        for val in line:
            if val.isdigit():
                return int(val)


    def find_second_val(self, line):
        reversed_line = line[::-1]
        for val in reversed_line:
            if val.isdigit():
                return int(val)

if __name__ == "__main__":
    treb = Trebuchet('input.txt')


