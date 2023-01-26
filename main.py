class Person:
    def __init__(self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __str__(self):
        return f"Имя сотрудника - {self.name}, фамилия сотрудника - {self.surname}, квалификация - {self.qualification}"
    def __del__(self):
        print(f'До свидания, мистер {self.name} {self.surname}. Будем ждать Вас снова!')
        del self
if __name__ == '__main__':
    person_1 = Person('Кирилл', 'Шендерук', 4)
    person_2 = Person('Eva', 'Mirtanskaya', 3)
    person_3 = Person("Jon", 'Abraham', 1)
    print(person_1)
    print(person_2)
    print(person_3)
    del person_3
    input()