from fleet import Fleet
from thing import Thing
fleet = Fleet()

# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch
fleet.add(Thing('Get milk'))
fleet.add(Thing('Remove the obstacles'))

thing1=Thing('stand up')
thing1.complete()
fleet.add(thing1)

thing2=Thing('Eat lunch')
thing2.complete()
fleet.add(thing2)


print(fleet)
