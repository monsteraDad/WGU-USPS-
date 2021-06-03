"""
This file contains the Distance class, which is made to read the distance table into
a dictionary where the dictionary key is the intersect of addresses and the value the
distance between them. [address1,address2]: distance. This is done by creating two lists of addresses

"""
import csv


class DistanceTable:
    # initialize the distance table to an empty list
    def __init__(self):
        self.table = []

    # O(k)
    def insert_distance(self, address_1, address_2, distance):
        distance_key = [address_1, address_2]
        distance_value = distance
        distance_key_value = [distance_key, distance_value]
        # add distance_key_value to the distance table
        self.table.append(distance_key_value)

    # O(n^2)
    def look_up_distance(self, address_1, address_2):
        find = [address_1, address_2]
        # parse each row for a match with find
        for distance_rows in self.table:
            if distance_rows[0] == find:
                # return the distance
                return distance_rows[1]

    # O(n)
    def print_dist_table(self):
        # parse each row in distance table, printing each rows elements.
        for distance_rows in self.table:
            print(distance_rows[0][0], distance_rows[0][1], distance_rows[1])


# assign csv file to distanceFile to be read
distanceFile = "/Users/jaredbreyer/Desktop/DSAIIPA/supportingFiles/WGUPSDistanceTable.csv"

# open the distanceFile to be read
with open(distanceFile) as distFile:
    # read the distance file into readDistances
    readDistances = csv.reader(distFile)

    # read file into matrix address_list
    tempDistTable = []

    # creation of distance table object
    distTable = DistanceTable()

    # parse the rows in readDistance add them to temp
    # distance table
    for rows in readDistances:
        tempDistTable.append(rows)

    # initialize address_list as an empty list
    address_list = []

    # parse rows in temp. distance add the address to address_list
    for rows in tempDistTable:
        address = rows[0]
        # add address to address_list
        address_list.append(address)

    # parse temp-distance-table
    for rows in tempDistTable:
        # location is the first element of the row
        address1 = rows[0]

        # from element 1 to element 28
        for i in range(1, 28):
            # assign address2 to the element i in the address_list
            address2 = address_list[i]
            # assign the distance to value
            value = rows[i]

            # work around to make sure, to only collect distances
            if len(value) <= 4:
                # read string in as float
                value = float(value)
                # add the location to destination with distance between to distance table
                distTable.insert_distance(address1, address2, value)
