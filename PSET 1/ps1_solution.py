###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    limitAval= limit
    #return a lsit of list, sublists represent individual trip
    trips = []
    #store the cows already travelled 
    cowsTravelled = []

    #create a copy of the lsit to avoid mutating the initial list
    itemsCopy = sorted(cows, key= cows.get, reverse = True)
    ##creating trips if not all the cows are shipped
    #if the weight of the cow < weight available and has not been shipped,
    #   add it to the tempList and cowsTravelled
    #   space limit reduced by the weight of the cow
    
    while len(itemsCopy) != len(cowsTravelled):
        tempList = []
        limitAval= limit
        for i in range(len(itemsCopy)):
            
            if cows[itemsCopy[i]] <= limitAval and itemsCopy[i] not in cowsTravelled:
                tempList.append(itemsCopy[i])
                cowsTravelled.append(itemsCopy[i])
                limitAval -= cows[itemsCopy[i]]
                
        trips.append(tempList)
    return trips



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # The worst case: the shortest case contain len(cows) trips
    shortest = len(cows)
    #initizalize the return lsit as empty list of list
    BestTrips = [[]]
    
    #Check all the partitions from get_partitions()
    #1. whether the trip is a goodtrip: Total weight of the trips<=limit
    #2. whether the number of trips  is < shortest
    for part in get_partitions(cows.keys()):
        goodTrip = True
        #check the total weight of the individal trip in part
        for trip in part:
            
            weightSum = 0
            for cow in trip:
                weightSum += cows[cow]
                
            if weightSum > limit:
                goodTrip= False
                break
        # if it's a good trip, check the len of the trip  
        if (len(BestTrips)==0 or len(part) < len(BestTrips)) and goodTrip == True:
            BestTrips = part[:] 

    return BestTrips
    

        
# Problem 3
def compare_cow_transport_algorithms(cows):
                                     
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    #print(start)
    greadyTrip = greedy_cow_transport(cows)
    end = time.time()
    print('Time for Gready:', end-start, '| Trips taken:', len(greadyTrip))
    print(greadyTrip,'\n')
    
    start1 = time.time()
    BFTrip = brute_force_cow_transport(cows)
    end1 = time.time()
    print('Time for BF:', end1-start1, '| Trips taken:', len(BFTrip))
    print(BFTrip)
    return None
"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=14
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms(cows)
