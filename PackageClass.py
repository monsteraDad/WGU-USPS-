import csv
import TruckClass
import datetime as dt

# loading the CSV file
packages = "/Users/jaredbreyer/Desktop/DSAIIPA/supportingFiles/WGUPSPackageFile.csv"


# initializing hash as an empty list, since package ID's unique, use of a direct hash
# is present with the ability to chain onto the buckets to allow for scalability.
class ChainingHashTable:

    def __init__(self, initial_capacity=40):
        # Initialize Hash Table with an empty list and start time of 8AM
        self.table = []
        self.time = dt.datetime(2021, 5, 10, 8, 0, 0)

        # Add an empty list for each packages, if there is more packages to deliver
        # just change initial_capacity to be the number of packages to be delivered
        for i in range(initial_capacity):
            self.table.append([])

    # take the key (package ID) mod 40 (length of the table) to directly hash the packages into the hash table.
    # O(k) where k is a constant integer
    def hash_insert(self, key, address, deadline, city, zip_code, weight, special_notes, status, time):
        # define the buckets for packages to be added to
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        key_values = [key, address, deadline, city, zip_code, weight, special_notes, status, time]
        # if a bucket_list already contains a package this will add the package after the one that
        # might already be in the bucket.
        bucket_list.append(key_values)

    # use the key to find the bucket that the package is in. while the hashtable has 40 buckets
    # the hash_look_up function has O(n^2).
    def update_status(self, key, status, time):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        # for the key value pairs in the bucket list
        # check if the key (1st element) is the same as key
        for kv in bucket_list:
            if kv[0] == key:
                # update status (8th element) and time (9th element)
                kv[7] = status
                kv[8] = time

    # takes the current time and updates the hash tables current time
    # O(k)
    def update_day_time(self, current_time):
        self.time = current_time

    # updates the packages time if the package has not been delivered
    # O(n^2)
    def update_packages_time(self, key, current_time):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        # for the key value pairs in the bucket list
        for kv in bucket_list:
            if kv[7] != 'delivered':
                # if not delivered update time
                kv[8] = current_time

    # updates the address of packages and special instruction to
    # when the package address was updated
    # O(n^2)
    def update_address(self, key, address, zipcode):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = address
                kv[4] = zipcode
                kv[6] = 'updated at: ', self.time

    # looks up the package by package ID (key)
    # O(n^2)
    def hash_look_up_id(self, key):
        bucket = key % 40
        bucket_list = self.table[bucket]

        # check each index of the bucket_list against the key parameter.
        # if match return the key_values(kv) at that index.
        for kv in bucket_list:
            if kv[0] == key:
                print("--------------------------------------------")
                print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                      kv[2], "\n Weight: ",
                      kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                print(" Time: ", kv[8].time())
                print("--------------------------------------------")
        return None

    # Looks up the package destination by key and returns the package address
    # O(n^2)
    def hash_look_up_destination(self, key):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        # check each index of the bucket_list against the key parameter.
        # if match return the key_values(kv) at that index.
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

    # Looks up the package by street address, returns package information if
    # match found
    # O(n^3)
    def hash_look_up_street_address(self, street_address):
        print("Packages to be delivered at: ", street_address)
        for buckets in self.table:
            for kv in buckets:
                if kv[1] == street_address:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
        print("--------------------------------------------")

    # Looks up packages by deadline, returns package information
    # if match is found
    # O(n^3)
    def hash_look_up_deadline(self, deadline):
        print("Packages to be delivered by: ", deadline)
        for buckets in self.table:
            for kv in buckets:
                if kv[2] == deadline:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
        print("--------------------------------------------")

    # Looks up packages by city, returns package information, if match is found.
    # O(n^3)
    def hash_look_up_city(self, city):
        print("Packages to be delivered in: ", city)
        for buckets in self.table:
            for kv in buckets:
                if kv[3] == city:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
                else:
                    print("No Packages to be delivered in ", city)
        print("--------------------------------------------")

    # Looks up packages by zipcode, returns package information if match is found
    # O(n^3)
    def hash_look_up_zipcode(self, zipcode):
        print("Packages to be delivered in: ", zipcode)
        for buckets in self.table:
            for kv in buckets:
                if kv[4] == zipcode:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
        print("--------------------------------------------")

    # Looks up packages by weight, returns package information if match is found
    # O(n^3)
    def hash_look_up_weight(self, weight):
        print("Packages of weight: ", weight)
        weights = []
        for buckets in self.table:
            for kv in buckets:
                if kv[5] == weight:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
                    weights.append(kv[0])
        # if no match found returns no packages found
        if len(weights) == 0:
            print("No packages found with weight: ", weight)
        print("--------------------------------------------")

    # Looks up packages by status, returns packages information if found
    # O(n^3)
    def hash_look_up_status(self, status):
        print("Packages of Status: ", status)
        matches = []
        for buckets in self.table:
            for kv in buckets:
                if kv[7] == status:
                    print("--------------------------------------------")
                    print(" Package ID: ", kv[0], "\n Delivery Address:", kv[1], ",", kv[3], ",", kv[4], "\n Deadline",
                          kv[2], "\n Weight: ", kv[5], "\n Special Instruction: ", kv[6], "\n Status: ", kv[7], )
                    print(" Time: ", kv[8].time())
                    matches.append(kv[0])
        if len(matches) == 0:
            print("All packages were delivered")

    # Looks up packages status at a time, returns packages information
    # O(n^2)
    def hash_look_up_time(self, time):
        print(" Time: ", time)
        for buckets in self.table:
            for kv in buckets:
                print(" Package ID:", kv[0], " | Status:", kv[7], " ›| Time:", kv[8])
        print("-------------------------------------------------------")


# read the WGUPSPackageFile.csv into hashtable

with open(packages) as packages:

    # Assigns packages with initial start time
    start_time = dt.datetime(2021, 5, 10, 8, 0, 0)

    # Read CSV File into readPackage
    readPackages = csv.reader(packages)

    # starting point of the packages
    delivery_status = "at the hub"

    # Creation of hashtable
    packagesHash = ChainingHashTable()

    # Creation of trucks
    truck_manifest = TruckClass.Truck()

    # Creation of known zipcode list to be used for console menu
    known_zip_codes = []

    # parse through csv files rows to collect data to be stored in packagesHash hashtable
    # and load packages onto trucks.
    for row in readPackages:
        package_id_num = int(row[0])
        delivery_address = row[1]
        delivery_deadline = row[5]
        delivery_city = row[2]
        delivery_zip = int(row[4])
        package_weight = int(row[6])
        package_special_notes = row[7]

        # Pass rows information to the hash_insert function
        packagesHash.hash_insert(package_id_num, delivery_address, delivery_deadline, delivery_city, delivery_zip,
                                 package_weight, package_special_notes, delivery_status, start_time)

        # Add zipcode to known zipcodes list if the zipcode is
        # not already in the list
        if delivery_zip not in known_zip_codes:
            known_zip_codes.append(delivery_zip)

        # load trucks based on package information
        truck_manifest.load_trucks(package_id_num, delivery_deadline, package_special_notes)
