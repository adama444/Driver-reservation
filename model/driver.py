from model.user import User


class Driver(User):
    def __init__(self,
                 id_driver, first_name, last_name, gender,
                 phone_number, email, age,
                 job, localization, driving_license_id,
                 driving_year_experience, id_driving_licence_category):
        super().__init__(
            id_driver, first_name, last_name,
            gender, phone_number, email, age, job, localization)
        self.driving_license_id = driving_license_id
        self.driving_year_experience = driving_year_experience
        self.id_driving_licence_category = id_driving_licence_category

    def __repr__(self):
        dictionary = {
            "id_driver": self.id_driver,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "email": self.email,
            "age": self.age,
            "job": self.job,
            "localization": self.localization,
            "driving_license_id": self.driving_license_id,
            "driving_year_experience": self.driving_year_experience,
            "id_driving_licence_category": self.id_driving_licence_category
        }
        return dictionary


class DrivingLicenseCategory:
    def __init__(self, id_category, name, description):
        self.id_category = id_category
        self.name = name
        self.description = description

    def __repr__(self):
        dictionary = {
            "id_category": self.id_category,
            "name": self.name,
            "description": self.description,
        }
        return dictionary
