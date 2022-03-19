from controller import vehicle_controller
from controller.customer_controller import search_driver
from model.customer import Customer

customer1 = Customer(1, "Adama", 'Samake', 'M', '92029008', "aaa@aa.aaa", 25, 'Etudiant', 'Zanguera', False)
customer2 = Customer(2, "Toto", 'ABALO', 'M', '94029001', "aasa@aa.aaa", 30, 'Comptable', 'Agouè', True, 4)
customer3 = Customer(3, "Kodjo", 'ODANOU', 'M', '92429508', "aada@aa.aaa", 40, 'Professeur', 'Attiegou', True, 2)
customer4 = Customer(4, "Amina", 'Sossou', 'F', '92429508', "aada@aa.aaa", 40, 'Professeur', 'Attiegou', True, 2)

customers_list = [customer1, customer2, customer3]

search_driver(customer1, vehicle_controller.get_vehicle(customer1.id_user))
