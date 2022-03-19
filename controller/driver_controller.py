from model.driver import Driver
from model.driver import DrivingLicenseCategory


def get_all_drivers():
    return drivers_list


def notify_task(driver):
    print("Cher", driver.first_name)
    choice = input("Vous avez une proposition de course. Voulez-vous accepter ? (y / n)")
    if str.lower(choice) == "y":
        choice = True
    else:
        choice = False
    return choice


driver1 = Driver(1, "Gael", "ROSS", 'M', 90070634, 'aqa@gmail.com', 25,
                 'Developpeur', 'Agouè', 1234567, 2, 1)
driver2 = Driver(2, "Toto", "ROSS", 'M', 90070634, 'aqa@gmail.com', 50,
                 'Enseignant', 'Agouè', 1274567, 8, 1)
driver3 = Driver(3, "Ali", "ROSS", 'M', 90070634, 'aqa@gmail.com', 24,
                 'Chauffeur', 'Zanguera', 3234567, 3, 1)
driver4 = Driver(4, "Daniel", "ROSS", 'M', 90070634, 'aqa@gmail.com', 30,
                 'Basketteur', 'Agouè', 1237567, 5, 1)
driver5 = Driver(5, "Jack", "ROSS", 'M', 90070634, 'aqa@gmail.com', 19,
                 'Agent de sécurité', 'Attiegou', 9234567, 1, 1)
driver6 = Driver(6, "Jeff", "Bezos", 'M', 90070634, 'aqa@gmail.com', 20,
                 'Agent d\'entretient', 'Zanguera', 2234567, 2,
                 1)
driver7 = Driver(7, "Gael", "ROSS", 'M', 90070634, 'aqa@gmail.com', 40,
                 'Policier', 'Attiegou', 1234561, 6, 1)
driver8 = Driver(8, "Gael", "ROSS", 'M', 90070634, 'aqa@gmail.com', 33,
                 'Comedien', 'Zanguera', 1234067, 7, 1)

drivers_list = [driver1, driver2, driver3, driver4, driver5, driver6, driver7, driver8]

driving_license_category = DrivingLicenseCategory(1, 'B', "Vehicle poids leger")

