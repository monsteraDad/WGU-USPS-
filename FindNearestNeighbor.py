"""
This package contains the nearest Neighbor function which takes the current truck
and current location and finds the package with the closest destination returning
runtime is ...
"""
import DistanceClass
import PackageClass
import datetime as dt


def nearest_neighbor(truck_manifest, current_location, current_time):

    # time stored to use in updating of package 9
    update_package_address_time = dt.datetime(2021, 5, 10, 10, 20, 0)

    # initialize an empty list to store package info
    package_to_deliver = []

    # assign an arbitrary temporary distance
    temp_dist = 25

    # parse packages in the truck_manifest
    for packages in truck_manifest:
        # check to see if the current time is 10:20 AM or not
        if (current_time.time() <= update_package_address_time.time()) and packages == 9:
            pass
        # when the time is 10:20 AM update package 9's address to the correct address
        elif current_time.time() >= update_package_address_time.time() and packages == 9:
            PackageClass.packagesHash.update_address(key=9, address="410 S State St", zipcode=84111)

        # collect delivery address of package
        destination = PackageClass.packagesHash.hash_look_up_destination(packages)

        # retrieve distance data from distance table using the current location and
        # package delivery address.
        distance = DistanceClass.distTable.look_up_distance(current_location, destination)

        # if the distance is less than the temporary distance assign the distance
        # to the temporary distance, if the distance is not maintains the shortest distance.
        # if the truck_manifest has 1 package left then assign the temp_distance to the distance
        # calculated above.
        if distance <= temp_dist or (len(truck_manifest) == 1):
            temp_dist = distance
            projected_destination = destination
            package_id = packages

            # assign package_to_deliver information with the shortest distance
            package_to_deliver = [package_id, projected_destination, temp_dist]

    # when done looping return the package information with the shortest distance
    # from current location
    return package_to_deliver
