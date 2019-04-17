import random
import uuid

from object.Routing import lobby_default, driveup_default
from object.Routing import Address, Location, Meta_list, Day, Routing, phone_number_generation


class Branch:
    def __init__(self, branch_id, bank, name,
                 address, location, meta, lobby, drive_up
                 ):
        self.id = branch_id
        self.bank = bank
        self.name = name
        self.address = address
        self.location = location
        self.meta = meta
        self.lobby = lobby
        self.drive_up = drive_up

    def dict(self):
        return {
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
            branch_id = str(uuid.uuid4())
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
                "hours":"M-TH 8:30-3:30, F 9-5"
            }

            drive_up = {
                "hours": "M-Th 8:30-5:30, F-8:30-6, Sat 9-12"
            }

            yield Branch(
                branch_id = branch_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta,
                lobby=lobby,
                drive_up=drive_up
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

    def dict(self):
        return {
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
            atm_id = str(uuid.uuid4())
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