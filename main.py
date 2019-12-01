from peewee import *

db = PostgresqlDatabase('cli_app', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class FlashCard(BaseModel):
    question = CharField()
    answer = CharField()
    number_correct = PositiveIntegerField()
    number_incorrect = PositiveIntegerField()

db.create_tables([FlashCard])

card1 = FlashCard(question='What is your name?', answer='Shelby')
card1.save()
card2 = FlashCard(question='What is your quest?', answer='To find the Holy Grail')
card2.save()
card3 = FlashCard(question='What is the airspeed velocity of an unladen swallow?', answer='11 meters per second')
card3.save()


