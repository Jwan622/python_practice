class Dog:
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"this is the self method: {self.name}"

	def description(self):
		return f"{self.name} is {self.age} years old"

	def speak(self, sound):
		return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
print('milesname:', miles.name)
print('buddyname:', buddy.name)
print('buddyspecies:', buddy.species)
print('milesspeicies:', miles.species)
print('buddyage:', buddy.age)
print('milesage:', miles.age)
miles.species = 'a new species'
print('milesnewspecies:', miles.species)
print('miles.descripiton', miles.description())
print('miles.speak', miles.speak('woof woof'))
print('miles.speak', miles.speak('bow wow'))
print('this is printing the self', miles)



class Parent:
	hair_color = "brown"

class Child(Parent):
	hair_color = "purple"


c = Child()
p = Parent()
print('child hair purple:', c.hair_color)
print('parent hair purple:', p.hair_color)


class Parent1:
	speaks = ["English"]


class Child1(Parent1):
	def __init__(self):
		super().__init__()
		self.speaks.append("German")

p1 = Parent1()
print("parent speaks english:", p1.speaks)
c1 = Child1()
print("child pseaks both", c1.speaks)



class Dog1:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says tt {sound}"

class JackRussellTerrier(Dog1):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog1):
    pass

class Bulldog(Dog1):
    pass

miles1 = JackRussellTerrier("Miles", 4, )
buddy1 = Dachshund("Buddy", 9)

print('miles species: canis familiarias', miles1.species)
print('buddy name:', buddy1.name)
print('type miles', type(miles))
print('true:', isinstance(miles, Dog))
print('miels says arf', miles1.speak())
print('miels says grrrr', miles1.speak('grrrr'))

jim = Bulldog("Jim", 5, )
print('jim says woof', jim.speak("Woof"))
miles2 = JackRussellTerrier('miles', 6)
print('miles2 says default arf', miles2.speak())



class ReportCard:
	some_class_variable = 5

	def __init__(self, scores):
		self.scores = scores

	def __str__(self):
		return f"scores are: {self.scores}"


class Student:
	def __init__(self, report_card):
		self.report_card = report_card

	def fail(self):
		self.report_card.scores.append("F")


r1 = ReportCard(['1', '2', '3'])
r2 = ReportCard(['2', '3'])
print('r1 scores', r1.scores)
mark = Student(r1)
print('mark repoert card', mark.report_card)
mark.fail()
print('mark repoert card with fail', mark.report_card)
jeff = Student(r2)
jeff.fail()
print('jeff report card with fail', jeff.report_card)

