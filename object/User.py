import random
import uuid

from object.Account import Account
from object.Routing import Routing, digits11, generateIBAN

boy_first_names=('John','Andy','Joe')
girl_first_names=('Alice','Ammy')
last_names=('Johnson','Smith','Williams')
mails=('gmail.com','qq.com','tesobe.com')
class User:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

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

    @staticmethod
    def Generator(num, gender = 'male'):
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
                password=password
            )