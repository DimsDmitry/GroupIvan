class Pupil:
    def __init__(self, Name, Mark):
        self.Name = Name
        self.Mark = Mark


pupils = []


def print_class(pupils):
    for pupil in pupils:
        print(pupil.Name, "-", pupil.Mark)
    print("\n")


def find_biggest(pupils):
    Biggest_Pupil = Pupil("", 0)
    for pupil in pupils:
        if pupil.Mark > Biggest_Pupil.Mark:
            Biggest_Pupil.Mark = pupil.Mark
            Biggest_Pupil.Name = pupil.Name
    return Biggest_Pupil


def get_average_mark(pupils):
    sum = 0
    for pupil in pupils:
        sum += pupil.Mark
    sum /= len(pupils)
    return sum


with open("my_class.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], int(data[1]))
        pupils.append(pupil)

print_class(pupils)
Biggest_Pupil = find_biggest(pupils)
Average_Mark = get_average_mark(pupils)

print("Самый высокий балл у ученика:", Biggest_Pupil.Name, " - ", Biggest_Pupil.Mark, "\nСредний балл группы:", Average_Mark)