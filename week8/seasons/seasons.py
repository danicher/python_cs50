from datetime import date
import inflect
import sys

def main():
    date = input("Date of birth: ")
    minutes = calculate_age_in_minutes(date)
    minutes = inflect.engine().number_to_words(minutes, andword="").capitalize()
    print(f"{minutes} minutes")

def calculate_age_in_minutes(birth_date_str):
    try:
       birth_date = date.fromisoformat(birth_date_str)
       today = date.today()
       age_in_days = (today - birth_date).days
       age_in_minutes = age_in_days * 24 * 60
       return age_in_minutes
    except ValueError:
       sys.exit("Invalid date")
if __name__ == "__main__":
    main()