from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class BonusTransaction:
    id: str
    date: str
    docType: str
    departmentId: str
    goodsId: str
    paymentId: str
    quantity: int
    points: float

    @staticmethod
    def from_dict(obj: Any) -> 'BonusTransaction':
        _id = str(obj.get("id"))
        _date = str(obj.get("date"))
        _docType = str(obj.get("docType"))
        _departmentId = str(obj.get("departmentId"))
        _goodsId = str(obj.get("goodsId"))
        _paymentId = str(obj.get("paymentId"))
        _quantity = int(obj.get("quantity"))
        _points = float(obj.get("points"))
        return BonusTransaction(_id, _date, _docType, _departmentId, _goodsId, _paymentId, _quantity, _points)



@dataclass
class Client:
    lastName: str
    firstName: str
    patronymic: str
    phone: str

    @staticmethod
    def from_dict(obj: Any) -> 'Client':
        _lastName = str(obj.get("lastName"))
        _firstName = str(obj.get("firstName"))
        _patronymic = str(obj.get("patronymic"))
        _phone = str(obj.get("phone"))
        return Client(_lastName, _firstName, _patronymic, _phone)



@dataclass
class FuelTransaction:
    id: str
    date: str
    docType: str
    departmentId: str
    goodsId: str
    quantity: int

    @staticmethod
    def from_dict(obj: Any) -> 'FuelTransaction':
        _id = str(obj.get("id"))
        _date = str(obj.get("date"))
        _docType = str(obj.get("docType"))
        _departmentId = str(obj.get("departmentId"))
        _goodsId = str(obj.get("goodsId"))
        _quantity = int(obj.get("quantity"))
        return FuelTransaction(_id, _date, _docType, _departmentId, _goodsId, _quantity)

@dataclass
class MoneyTransaction:
    id: str
    date: str
    docType: str
    departmentId: str
    money: int

    @staticmethod
    def from_dict(obj: Any) -> 'MoneyTransaction':
        _id = str(obj.get("id"))
        _date = str(obj.get("date"))
        _docType = str(obj.get("docType"))
        _departmentId = str(obj.get("departmentId"))
        _money = int(obj.get("money"))
        return MoneyTransaction(_id, _date, _docType, _departmentId, _money)

@dataclass
class Result:
    code: str
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        _code = str(obj.get("code"))
        _description = str(obj.get("description"))
        return Result(_code, _description)




@dataclass
class Card:
    number: str
    bonusTransactions: List[BonusTransaction]
    moneyTransactions: List[MoneyTransaction]
    fuelTransactions: List[FuelTransaction]

    @staticmethod
    def from_dict(obj: Any) -> 'Card':
        _number = str(obj.get("number"))
        _bonusTransactions = [BonusTransaction.from_dict(y) for y in obj.get("bonusTransactions")]
        _moneyTransactions = [MoneyTransaction.from_dict(y) for y in obj.get("moneyTransactions")]
        _fuelTransactions = [FuelTransaction.from_dict(y) for y in obj.get("fuelTransactions")]
        return Card(_number, _bonusTransactions, _moneyTransactions, _fuelTransactions)

@dataclass
class Data:
    client: Client
    cards: List[Card]

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        _client = Client.from_dict(obj.get("client"))
        _cards = [Card.from_dict(y) for y in obj.get("cards")]
        return Data(_client, _cards)

@dataclass
class Root:
    result: Result
    data: Data

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _result = Result.from_dict(obj.get("result"))
        _data = Data.from_dict(obj.get("data"))
        return Root(_result, _data)
# Example Usage

# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
