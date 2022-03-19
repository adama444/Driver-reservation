class Vehicle:
    def __init__(self,
                 id_vehicle, brand, model,
                 gear_box, chassis_number, place_number,
                 color, insurance_id, id_owner):
        self.id_vehicle = id_vehicle
        self.brand = brand
        self.model = model
        self.gear_box = gear_box
        self.chassis_number = chassis_number
        self.place_number = place_number
        self.color = color
        self.insurance_id = insurance_id
        self.id_owner = id_owner

    def __repr__(self):
        dictionary = {
            "id_vehicle": self.id_vehicle,
            "brand": self.brand,
            "model": self.model,
            "gear_box": self.gear_box,
            "chassis_number": self.chassis_number,
            "place_number": self.place_number,
            "color": self.color,
            "insurance_id": self.insurance_id,
            "id_owner": self.id_owner,
        }
        return dictionary
