from yoomoney import Client, Quickpay


class NotEnoughMoney(Exception):
    pass


class NoPaymentFound(Exception):
    pass


def payment_found(label, history):
    for operation in history.operations:
        if operation.label == label:
            return True
    return False


def payment_sufficient(operation, amount, is_commission=True):
    if is_commission:
        commission_rate = 0.04
        actual_amount = float(operation.amount)
        expected_amount_min = round(amount * (1 - commission_rate), 2)
        expected_amount_max = round(amount, 2)
        return expected_amount_min <= actual_amount <= expected_amount_max
    else:
        return float(operation.amount) == amount


class YooMoneyClient:
    """The YooMoneyClient class is designed for working with the YooMoney API. To create an object of this class, you need to pass it a token as an argument.

Attributes:

client: an object of the Client class from the yoomoney-sdk-python library, which is used for working with the API.
Methods:

get_data(): returns information about the user account in the form of a string.
Example usage:

1.Create a token variable and assign it the value of your token:
token = "YOUR_TOKEN_HERE"

2.Create an object of the YooMoneyClient class, passing the token as an argument:
client = YooMoneyClient(token)

3.Call the get_data() method to retrieve information about the user account:
print(client.get_data())

This method returns a string containing the following information about the user account:
Account number
Account balance
Currency code in ISO 4217 format
Account status
Account type
Extended balance information about linked bank cards.
"""
    def __init__(self, token):
        self.client = Client(token)

    def get_data(self):
        user = self.client.account_info()
        result = [
            f"Account number: {user.account}",
            f"Account balance: {user.balance}",
            f"Account currency code in ISO 4217 format: {user.currency}",
            f"Account status: {user.account_status}",
            f"Account type: {user.account_type}",
            "Extended balance information:"
        ]
        for pair in vars(user.balance_details):
            result.append(f"\t--> {pair}: {vars(user.balance_details).get(pair)}")
        result.append("Information about linked bank cards:")
        cards = user.cards_linked
        if len(cards) != 0:
            for card in cards:
                result.append(f"{card.pan_fragment} - {card.type}")
        else:
            result.append("No card is linked to the account")
        return "\n".join(result)

    def check_payment(self, label, amount, is_commission=True):
        history = self.client.operation_history(label=label)

        if payment_found(label, history):
            for operation in history.operations:
                if operation.label == label:
                    if payment_sufficient(operation, amount, is_commission):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NoPaymentFound

        return False


class QuickPayYoomoney:
    def __init__(self, receiver, price, label, quick_pay_form="shop", targets="TEST", payment_type="SB"):
        self.receiver = receiver
        self.quick_pay_form = quick_pay_form
        self.targets = targets
        self.payment_type = payment_type
        self.price = price
        self.label = label

    def quickpay(self):
        quickpay = Quickpay(
            receiver=self.receiver,
            quickpay_form=self.quick_pay_form,
            targets=self.targets,
            paymentType=self.payment_type,
            sum=self.price,
            label=self.label
        )
        return quickpay.redirected_url


