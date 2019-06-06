import random
import uuid

from object.Account import Account
from object.Customer import Customer
from object.Routing import *

boy_first_names=('John','Andy','Joe')
girl_first_names=('Alice','Ammy')
last_names=('Johnson','Smith','Williams')
mails=('gmail.com','qq.com','tesobe.com')
class User:
    def __init__(self,username, email, password, phone, relationship_status, employment_status, highest_education_attained):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.relationship_status = relationship_status
        self.employment_status = employment_status
        self.highest_education_attained = highest_education_attained

    def dict(self):
        return {
            'user_name':self.username,
            'email': self.email,
            'password': self.password
        }

    def create_account(self, branch, type, currency, amount):
        account_id=str(uuid.uuid4())
        number = str(digits11())
        label = "{} {}".format(self.username, branch.name)
        iban = generateIBAN(branch.address.country_code.upper())
        return Account(
            account_id=str(uuid.uuid4()),
            branch=branch,
            user=[self],
            label=label,
            number=number,
            type=type,
            balance={
                 "currency":currency,
                 "amount":amount
             },
            account_routing=Routing(
                scheme="OBP",
                address=account_id
            ),
            iban=iban
        )

    def create_customer(self, bank):
        customer_number = str(uuid.uuid4())
        face_image = {
            "url": "www.example.com",
            "date": gen_datetime().strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        date_of_birth = gen_datetime(min_year = 1970, max_year=2001).strftime("%Y-%m-%dT%H:%M:%SZ")
        dob_of_dependants = [
            gen_datetime().strftime("%Y-%m-%dT%H:%M:%SZ") for _ in range(2)
        ]

        kyc_status = True
        last_ok_date = gen_datetime().strftime("%Y-%m-%dT%H:%M:%SZ")
        credit_rating=""
        credit_limit=""
        return Customer(
            customer_number=customer_number,
            user=self,
            mobile_phone_number=self.phone,
            face_image=face_image,
            date_of_birth=date_of_birth,
            relationship_status=self.relationship_status,
            dependants=random.randint(0,6),
            dob_of_dependants=dob_of_dependants,
            highest_education_attained=self.highest_education_attained,
            employment_status=self.employment_status,
            kyc_status=kyc_status,
            last_ok_date=last_ok_date,
            bank=bank,
            credit_rating=credit_rating,
            credit_limit=credit_limit
        )

    @staticmethod
    def Generator(num, gender = 'male', relationship_status = 'married', employment_status = 'retired', highest_education_attained='BA.'):
        if gender == 'male':
            first_names = boy_first_names
        else:
            first_names = girl_first_names
        first_name_tmp = random.choice(first_names)
        last_name = random.choice(last_names)
        for i in range(num):
            first_name = "{}".format(first_name_tmp)
            username = "{} {}".format(first_name, last_name)
            email = first_name +"@"+ random.choice(mails)
            password = str(uuid.uuid4())[:10]
            yield User(
                username=username,
                email=email,
                password=password,
                phone=phone_number_generation(),
                relationship_status= relationship_status,
                employment_status= employment_status,
                highest_education_attained = highest_education_attained
            )