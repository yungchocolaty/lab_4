from classes import Gang
from classes import Dutch
from classes import John
from classes import Gun
from classes import Arthur

Dutch = Dutch("Dutch",500,'Leader')
Dutch.show_info()
Dutch.action()

print("----------")

John = John('John', 'Gunslinger', 'Arabic')
John.show_info()
John.action()

print("----------")

Arthur = Arthur("right-hand man","perfect", "schofield", "one-shot kill")
Arthur.show_info()
Arthur.action()
