from model.user import User


class Customer(User):
    def __init__(self,
                 id_customer, first_name, last_name, gender,
                 phone_number, email, age,
                 job, localization, is_married, number_children=0):
        super().__init__(
            id_customer, first_name, last_name,
            gender, phone_number, email, age, job, localization)
        self.is_married = is_married
        self.number_children = number_children

    def __repr__(self):
        dictionary = {
            "id_customer": self.id_user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "email": self.email,
            "age": self.age,
            "job": self.job,
            "localization": self.localization,
            "is_married": self.is_married,
            "number_children": self.number_children
        }
        return dictionary
