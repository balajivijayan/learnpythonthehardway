things = ['a', 'b', 'c', 'd', 'e']

print things[1]

things[1] = 'z'

print things[1]

#Dictionaries also called as dicts are hashes in python

stuff = {'name': 'Balaji', 'age': 25, 'height': 6 * 12 + 2}

print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = 'Chennai'

print stuff['city']

stuff[1] = 'Neato'
stuff[2] = 'Wow'

print stuff


####Study Drills
#Creates a mapping of state to abbreviation
states = {
	'Tamilnadu' : 'TN',
	'Karnataka' : 'KA',
	'Andhra' : 'AP',
	'Maharashtra' : 'MH',
	'Kerala' : 'KL'
}


#Create a basic set of states and the cities in them
cities = {
	'TN' : 'Chennai',
	'KA' : 'Bangalore',
	'AP' : 'Hyderabad',
	'KL' : 'Trivandrum',
	'MH' : 'Mumbai'
}

# add more cities
cities['PUN'] = 'Pune'
cities['TRY'] = 'Trichy'

# print out some cities

print '-' * 10
print "TN state has: ", cities['TN']
print "MH state has: ", cities['MH']

# print out some abbreviations
print '-' * 10
print 'Tamilnadu has: ', cities[states['Tamilnadu']]

# print every state abbreviation
print '-' * 10
for state, abbreviation in states.items():
	print "%s is abbreviated as %s" % (state, abbreviation)

# print every city in state
print '-' * 10
for abbreviation, city in cities.items():
	print '%s city has the city %s' % (abbreviation, city)

# print both
print '-' * 10
for state, abbreviation in states.items():
	print '%s state is abbreviated as %s and has the city %s'  % (state, abbreviation, cities[abbreviation])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
	print 'Sorry, no Texas.'


# get a city with a default value
city = cities.get('Tx', 'Does not exist')
print "The city for the state 'TX' is : %s " % city






