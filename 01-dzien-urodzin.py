# Jaki to był dzień tygodnia? Sprawdzanie po wpisaniu daty urodzin, jaki to był dzień tygodnia. Odpowiedź ma być podana w języku polskim.


import datetime
import calendar

# wprowadzone match - pierwszy sposób, aby przetłumaczyć wyniki z angielskiego na polski

def translate_to_polish(day_name):
    match day_name:
        case 'Monday':
            return 'Poniedziałek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Środa'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday': 
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'
        

date_of_birth = input("Podaj date urodzin w formacie dzien-miesiac-rok (np.1-1-2000): ")
day, month, year = date_of_birth.split("-") # (1, 1, 2000)


date_of_birth = datetime.datetime(int(year), int(month), int(day))

# print(date_of_birth.weekday())

day_name = calendar.day_name [date_of_birth.weekday()]
print(translate_to_polish(day_name))


