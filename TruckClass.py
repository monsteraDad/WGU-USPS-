
import DistanceClass
import FindNearestNeighbor
import PackageClass
import math
import datetime as dt


class Truck:
    # Creation of truck manifest list.
    def __init__(self, available_trucks=3):
        self.table = []
        # add an empty list for the number of available trucks
        for i in range(available_trucks):
            self.table.append([])

    # takes package id, delivery deadline, special_instruction, and the maximum capacity of each
    # truck and loads the packages into the trucks.
    # O(n)
    def load_trucks(self, package_id, deadline, special_instruction, max_capacity=16):
        # Assign trucks to location on trucks manifest.
        truck1_manifest = self.table[0]
        truck2_manifest = self.table[1]
        truck3_manifest = self.table[2]

        # possible special instructions
        flight_delay = 'Delayed on flight---will not arrive to depot until 9:05 am'
        assigned_truck2 = "Can only be on truck 2"

        # truck 1  if it does not have 16 packages and is a morning delivery
        if len(truck1_manifest) < max_capacity and (deadline == "9:00 AM" or deadline == "10:30 AM"):
            truck1_manifest.append(package_id)

        # truck 2 if it does not have 16 packages and is delayed on flight or required to be on truck 2
        elif len(truck2_manifest) < max_capacity and (
                special_instruction == assigned_truck2 or special_instruction == flight_delay):
            truck2_manifest.append(package_id)
        # truck 3 for all remaining packages
        elif len(truck3_manifest) < max_capacity:
            truck3_manifest.append(package_id)
        # revisit loading truck1 and truck2 when truck3 is full
        elif len(truck1_manifest) < max_capacity:
            truck1_manifest.append(package_id)
        elif len(truck2_manifest) < max_capacity:
            truck2_manifest.append(package_id)

        # sort trucks in ascending order of package id
        truck1_manifest.sort()
        truck2_manifest.sort()
        truck3_manifest.sort()

    # updates trucks based on status
    # O(n^3)
    def update_trucks(self, package_id, status):
        for trucks in self.table:
            for packs in trucks:
                if packs[0] == package_id:
                    packs[3] = status

    # prints trucks manifest
    # O(n)
    def print_trucks(self):
        for trucks in self.table:
            print(trucks)

    # Delivery algorithm of trucks
    # O()
    def greedy_delivery_algorithm(self):
        # assign empty list to package information list
        package_info_list = []

        # assign empty list to trucks information list
        trucks_info_list = []

        # set start time to 8AM
        start_time = dt.datetime(2021, 5, 10, 8, 0, 0)

        # load current time from package class
        current_time = PackageClass.packagesHash.time

        # set total_distance traveled to 0
        total_distance_traveled = 0

        # set hub location
        hub = "4001 South 700 East"

        # reporting times
        early_time1 = dt.datetime(2021, 5, 10, 8, 35, 0)
        early_time2 = dt.datetime(2021, 5, 10, 9, 25, 0)
        mid_time1 = dt.datetime(2021, 5, 10, 9, 50, 0)
        mid_time2 = dt.datetime(2021, 5, 10, 10, 25, 0)
        afternoon_time1 = dt.datetime(2021, 5, 10, 12, 3, 0)
        afternoon_time2 = dt.datetime(2021, 5, 10, 13, 12, 0)

        # truck number to be incremented for reporting
        k = 1

        # parse each truck
        for trucks in self.table:
            # assign empty list to truck info.
            truck_info = []

            # assign trucks with starting data
            current_location = hub
            distance_traveled = 0
            mph = 18  # Miles per hour

            # parse packages on trucks
            for packages in trucks:
                # updates status of packages from at hub to en route
                PackageClass.packagesHash.update_status(packages, status="en route", time=current_time)

            # while the truck has packages
            while len(trucks) > 0:

                # send the trucks manifest to the nearest neighbor algorithm
                # returns the package info that is closest to the current location
                package_info_list.append(FindNearestNeighbor.nearest_neighbor(trucks, current_location, current_time))

                # assign the package info to its respective variables
                package_id = package_info_list[0][0]
                destination_location = package_info_list[0][1]
                shortest_distance_found = package_info_list[0][2]     # distance returned from nearest neighbor algo.

                # clear package info list for next batch
                package_info_list.clear()

                # calculate the distance traveled by truck
                distance_traveled += shortest_distance_found

                # calculate the travel time and increment the current time by seconds
                travel_time = (shortest_distance_found / mph) * 60 * 60
                current_time = current_time + dt.timedelta(seconds=travel_time)

                # update the current time in PackageClass file
                PackageClass.packagesHash.update_day_time(current_time)

                # update current_location to the destination
                current_location = destination_location

                # update total distance traveled in day
                total_distance_traveled += shortest_distance_found

                # update package as delivered
                PackageClass.packagesHash.update_status(package_id, 'delivered', current_time)

                # update time for all packages
                for packages in trucks:
                    PackageClass.packagesHash.update_packages_time(packages, current_time)

                # remove package from truck manifest
                for packages in trucks:
                    if package_id == packages:
                        trucks.remove(packages)

                # Send truck back to hub calculating the distance the truck traveled
                # incrementing the total distance traveled, and time
                if len(trucks) == 0:
                    distance_to_hub = DistanceClass.distTable.look_up_distance(current_location, hub)
                    distance_traveled += distance_to_hub
                    total_distance_traveled += distance_to_hub
                    travel_time = (shortest_distance_found / 18) * 60 * 60
                    current_time = current_time + dt.timedelta(seconds=travel_time)
                    current_location = hub

                # printing reports
                if early_time1.time() < current_time.time() < early_time2.time() and k == 1:
                    print("------------------Early Morning Report-----------------")
                    print(" Total Distance Traveled:", total_distance_traveled)
                    print(" Truck", k, "Distance Traveled: ", distance_traveled)
                    PackageClass.packagesHash.hash_look_up_time(current_time.time())
                    k += 1

                if mid_time1.time() < current_time.time() < mid_time2.time() and k == 2:
                    print("-----------------Mid Morning Report--------------------")
                    print(" Total Distance Traveled:", total_distance_traveled)
                    print(" Truck", k, "Distance Traveled: ", distance_traveled)
                    PackageClass.packagesHash.hash_look_up_time(current_time.time())
                    k += 1

                if afternoon_time1.time() < current_time.time() < afternoon_time2.time() and k == 3:
                    print("------------------Afternoon Report---------------------")
                    print(" Total Distance Traveled:", total_distance_traveled)
                    print(" Truck", k, "Distance Traveled: ", distance_traveled)
                    PackageClass.packagesHash.hash_look_up_time(current_time.time())
                    k += 1

                # update trucks info to match the respective variable reassignments
                truck_info = [current_location, distance_traveled, current_time]

            # when truck finished add truck information to the trucks information list
            trucks_info_list.append(truck_info)

        # truck numbers to be incremented during reporting
        j = 1


        # print end of day report
        print("------------------End of Day Report--------------------")
        print(" Start Time:", start_time)
        print(" Trucks start Location: ", hub)
        print("-------------Distance Traveled by trucks---------------")

        i = 1
        for trucks in trucks_info_list:
            print(" Truck", i, ":", math.ceil(trucks[1]), "miles")
            i += 1
        print(" Total Traveled: ", math.ceil(total_distance_traveled), "miles")
        print("------------Time Trucks finished deliveries------------")


        for trucks in trucks_info_list:
            print(" Truck", j, ":", trucks[2])
            j += 1
        PackageClass.packagesHash.hash_look_up_time(current_time.time())
        print(" Trucks End location: ", hub)
        print(" Deliveries Complete at:", current_time.time())
        print("-------------------------------------------------------\n")
