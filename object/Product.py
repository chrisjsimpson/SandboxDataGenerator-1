import random
import uuid

category_list = ["Mortgage", "Account","Credit Card","Loan","Savings","Overdraft"]
family_list = ["Mortgage", "Service","Credit Card","Loan","Credit","Loan"]
super_family_list =["Lending", "Service","Lending","Lending","Credit","Lending"]

product_list = list(zip(category_list, family_list, super_family_list))
class Product:
    def __init__(self, bank, code, name, category, family, super_family,
                 more_info_url, meta
                 ):
        self.bank = bank
        self.code = code
        self.name = name
        self.category = category
        self.family =family
        self.super_family = super_family
        self.more_info_url = more_info_url
        self.meta = meta

        self.dict = {
            "bank_id":bank.id,
            "code":code,
            "name":name,
            "category":category,
            "family":family,
            "super_family":super_family,
            "more_info_url":more_info_url,
            "meta":meta
        }

    @staticmethod
    def Generator(bank,  num):
        for i in range(num):
            code = str(uuid.uuid4())
            name = "PRODUCT{}{:2d}".format(code[:4], num)
            category, family, super_family = random.choice(product_list)

            yield Product(
                bank=bank,
                code=code,
                name=name,
                category=category,
                family=family,
                super_family=super_family,
                more_info_url="",
                meta={
                    "license":{
                        "id": "copyright",
                        "name": "Copyright"
                    }
                }
            )
