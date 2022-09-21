library = [
    {
        'прізвище': 'Порошенко',
        'посада': 'колишнiй презедент',
        'досвід роботи': 5,
        'портфоліо': 'три фото',
        'коефіцієнт ефективності': 0,
        'стек технологій': 'вiдсутнiй',
        'зарплата': 10000000000
    },
    {
        'прізвище': 'Олегов',
        'посада': 'прибиральник',
        'досвід роботи': 10,
        'портфоліо': 'вiдсутнiй',
        'коефіцієнт ефективності': 100,
        'стек технологій': 'вiдсутнiй',
        'зарплата': 1000
    },
    {
        'прізвище': 'Хмара',
        'посада': 'полiтолог',
        'досвід роботи': 20,
        'портфоліо': 'вiдсутнiй',
        'коефіцієнт ефективності': 113,
        'стек технологій': 'вiдсутнiй',
        'зарплата': 10000
    }
]
while True:
    button = int(input('search - 1\nedit - 2\nsorted - 3'))
    if button == 3:
        answer = input('Enter the  key:')
        list_sorted = [person.get(answer) for person in library]
        list_sorted.sort()
        list_sorted_final = list()

        for i in range(len(library)):
            for person in library:
                if person.get(answer) == list_sorted[i]:
                    list_sorted_final.append(person)
        print(list_sorted_final)

    elif button == 1:
        surname = input('Entered Surname: ')
        for i in range(len(library)):
            for person in library:
                if person.get('прізвище') == surname:
                    print(person)
            break

    elif button == 2:
        person = dict()
        person['прізвище'] = input('прізвище: ')
        person['посада'] = input('посада: ')
        person['досвід роботи'] = input('досвід роботи: ')
        person['портфоліо'] = input('портфоліо: ')
        person['коефіцієнт ефективності'] = input('коефіцієнт ефективності: ')
        person['стек технологій'] = input('стек технологій: ')
        person['зарплата'] = input('зарплата: ')
        library.append(person)
        print(library)