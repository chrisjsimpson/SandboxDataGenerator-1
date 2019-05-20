import random
import uuid

from object.Branch import ATM, Branch
from object.Routing import Routing, Meta_list, lobby_default, driveup_default

banks = ('bank_a', 'bank_b', 'bank_c', 'bank_d')
countries = ('uk', 'hk')
class Bank:
    def __init__(self,
                 bank_id, full_name, short_name, logo_url, website_url,
                 swift_bic, national_identifier, bank_routing):
        self.id = bank_id
        self.full_name = full_name
        self.short_name = short_name
        self.logo_url = logo_url
        self.website_url = website_url
        self.swift_bic = swift_bic
        self.national_identifier = national_identifier
        self.bank_routing = bank_routing

    def dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "short_name": self.short_name,
            "logo": self.logo_url,
            "website": self.website_url
        }

    def create_branches(self, num):
        branchGenerator = Branch.Generator(self, num)
        branch_list = []
        for j in range(num):
            branch_list.append(next(branchGenerator))
        return branch_list

    def create_atms(self, num):
        atmGenerator = ATM.Generator(self, num)
        atm_list = []
        for j in range(num):
            atm_list.append(next(atmGenerator))
        return atm_list

    def create_product(self):
        pass

    @staticmethod
    def Generator(num):
        bank_tmp = random.choice(banks)
        country = random.choice(countries)
        for i in range(num):
            full_name = "{}_{:02d}".format(bank_tmp, i)
            short_name = "{}_{:02d}".format(bank_tmp, i)
            bank_id = short_name + "." + country
            logo_url = "https://static.openbankproject.com/images/sandbox/{}.png".format(full_name)
            website_url = "https://www.example.com"
            swift_bic="IIIGGB22"
            national_identifier=country
            bank_routing: Routing = Routing(
                scheme="OBP",
                address=bank_id
            )
            yield Bank(
                bank_id=bank_id,
                full_name=full_name,
                short_name=short_name,
                logo_url=logo_url,
                website_url=website_url,
                swift_bic=swift_bic,
                national_identifier=national_identifier,
                bank_routing=bank_routing
            )
