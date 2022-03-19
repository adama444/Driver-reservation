from abc import ABC


class User(ABC):
    def __init__(self,
                 id_user, first_name, last_name,
                 gender, phone_number, email, age, job, localization):
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.age = age
        self.job = job
        self.localization = localization
