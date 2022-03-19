from model.customer import Customer
import vehicle_controller
import driver_controller


def get_all_customers():
    pass


def get_customer():
    pass


def add_customer():
    pass


def update_customer():
    pass


def delete_customer():
    pass


def notify(customer, messages):
    if customer.gender == 'M':
        print("Mr", customer.first_name)
        for message in messages:
            print(message)
    else:
        print("Mme", customer.first_name)
        for message in messages:
            print(message)


def print_drivers_found(customer, drivers_found):
    if customer.gender == 'M':
        print("Mr", customer.first_name)
        print("Voici les conducteurs trouvés dans votre zone")
        for driver in drivers_found:
            print("--> ", driver.first_name, driver.last_name,
                  driver.driving_year_experience, 'ans d\'experiences')
    else:
        print("Mme", customer.first_name)
        print("Voici les conducteurs trouvés dans votre zone")
        for driver in drivers_found:
            print("--> ", driver.first_name, driver.last_name,
                  driver.driving_year_experience, 'ans d\'experiences')


def search_driver(customer, vehicle):
    drivers_found = []
    messages = []
    drivers_list = driver_controller.get_all_drivers()
    for driver in drivers_list:
        if driver.localization == customer.localization:
            if driver_controller.notify_task(driver):
                messages.append('Un conducteur a été trouvé dans votre zone')
                drivers_found.append(driver)
            else:
                messages.append("Aucun conducteur trouvé dans votre zone")
    notify(customer, messages)
    print_drivers_found(customer, drivers_found)
