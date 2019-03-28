import random
import uuid

from object.Routing import lobby_default, driveup_default
from object.Routing import Address, Location, Meta_list, Day, Routing, phone_number_generation


class Branch:
    def __init__(self, branch_id, bank, name,
                 address, location, meta, lobby, drive_up,
                 branch_routing =None, is_accessible=None, accessibleFeatures=None, branch_type=None,
                 more_info=None, phone_number=None
                 ):
        self.id = branch_id
        self.bank = bank
        self.name = name
        self.address = address
        self.location = location
        self.meta = meta
        self.lobby = lobby
        self.drive_up = drive_up
        self.branch_routing = branch_routing
        self.is_accessible = is_accessible
        self.accessibleFeatures = accessibleFeatures
        self.branch_type = branch_type
        self.more_info= more_info
        self.phone_number = phone_number

        self.dict = {
            "id": self.id,
            "bank_id": self.bank.id,
            "name": self.name,
            "address": self.address,
            "location": self.location,
            "meta": self.meta,
            "lobby": self.lobby,
            "drive_up": self.drive_up
        }

    @staticmethod
    def Generator(bank, num):
        for i in range(num):
            branch_id = "branch-id-{}".format(str(uuid.uuid4())[:10])
            name = "Branch {} of {}".format(i, bank.id)
            address = Address()
            location = Location()
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":random.choice(Meta_list)
                }
            }

            lobby = {
                "monday":[Day()],
                "tuesday":[Day()],
                "wednesday":[Day()],
                "thursday":[Day()],
                "friday":[Day()],
                "saturday":[Day()],
                "sunday":[Day()]
            }

            drive_up = {
                "monday": Day(),
                "tuesday": Day(),
                "wednesday": Day(),
                "thursday": Day(),
                "friday": Day(),
                "saturday": Day(),
                "sunday": Day()
            }

            branch_routing = Routing(
                scheme="OBP",
                address=branch_id
            )

            is_accessible = "true" if random.uniform(0,1) > 0.5 else "false"
            accessibleFeatures = "feature {:02}".format(i)
            branch_type = "Full service store"
            more_info = "more info {:02}".format(i)
            phone_number = phone_number_generation()
            yield Branch(
                branch_id = branch_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta,
                lobby=lobby,
                drive_up=drive_up,
                branch_routing=branch_routing,
                is_accessible=is_accessible,
                accessibleFeatures=accessibleFeatures,
                branch_type=branch_type,
                more_info=more_info,
                phone_number=phone_number
            )

class ATM:
    def __init__(self, atm_id, bank, name,
                 address, location, meta
                 ):
        self.id = atm_id
        self.bank = bank
        self.name = name
        self.address = address
        self.location = location
        self.meta = meta

        self.dict = {
            "id": self.id,
            "bank_id": self.bank.id,
            "name": self.name,
            "address": self.address,
            "location": self.location,
            "meta": self.meta
        }

    @staticmethod
    def Generator(bank, num):
        for i in range(num):
            atm_id = "atm-id-{}".format(str(uuid.uuid4())[:10])
            name = "ATM {} of {}".format(i, bank.id)
            address = Address()
            location = Location()
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":random.choice(Meta_list)
                }
            }

            lobby = lobby_default
            driveUp = driveup_default

            yield ATM(
                atm_id = atm_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta
            )