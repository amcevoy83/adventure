from data import locations

#dictionary of directions, each set as co-ordinate, when added to a position, will move it in that direction.
# eg moving east will add 1 to the x co ordinate sot aht (1,1) becomes (2,1)
directions = {
    'west': (-1,0),
    'east': (1,0),
    'north': (0,-1),
    'south': (0,1),
}

#define our starting position
position = (0,0)

while True:
    #find the name of the location by pulling the detail from the locations dictionary
    location = locations[position]
    print 'You are at the %s' % location

## BELOW YOU ARE ESTABLISHING A NEW DICTIONARY CALLED VALID DIRECTIONS FOR THE USER WHICH WILL BE PROVIDED BACK TO THE USER WHEN CALLED
    valid_directions = {}

## THEN YOU START BRINGING IN THE VALUES FROM OUR CURRENT LOCATIONS LIST MATCHED WITH THE DIRECTION COORDINATES
    #read both the keys(k) and values(v) of the dictionary when iterating through it.
    for k, v in directions.iteritems():
        #for each direction, calculate the possible position if we take that direction
        possible_position = (position[0] + v[0], position[1] + v[1])
        #check if this position is in the list of locations - use .get for this as it will return None if that key doesn't exist
        possible_location = locations.get(possible_position)
        #if the location does exist, print the name of the location from the locations dictionary.
        if possible_location:
            print 'to the %s is the %s' %(k, possible_location)
            #then add this location to a valid directions dictionary to be used later if the user decides to move there (saves
            #doing the calculations again
            valid_directions[k] = possible_position

    #as the user for their direction the ywould like to go
    direction = raw_input('Which direction do you want to go?\n')
    #use the valid_cirections dictionary to move us there.
    position = valid_directions[direction]
