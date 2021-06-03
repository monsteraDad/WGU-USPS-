# Jared Breyer, SID: 001032849
import PackageClass


# creation of console

def main_menu():
    print("Western Governors University Postal Service \n")

    # Deliver the packages
    PackageClass.truck_manifest.greedy_delivery_algorithm()

    # Print the main menu
    print("What would you like to do? (A/C)\n")
    print("A: Look up package information\n")
    print("C: Exit application \n")
    user_input = input("What would you like to do? \n")

    while user_input != 'C':

        # look up a package by was selected
        if user_input == 'A' or user_input == 'a':
            # print options on how to look up
            print("How would you like to look up a package? (D/E/F/G/H/I/J/K)")
            print("D: By Package ID")
            print("E: By Delivery Address")
            print("F: By delivery deadline")
            print("G: By Delivery City")
            print("H: By Delivery Zipcode")
            print("J: By package weight")
            print("K: By status")
            print("N: return to main menu")

            # Get user input
            look_up_input = input()

            # look up by package ID selected
            if look_up_input == "D" or look_up_input == "d":
                package_id = int(input("Please enter a package ID. \n"))
                PackageClass.packagesHash.hash_look_up_id(package_id)

            # look up by delivery address selected
            elif look_up_input == "E" or look_up_input == "e":
                package_street_address = input("Please enter a street address.\n")
                PackageClass.packagesHash.hash_look_up_street_address(package_street_address)

            # look up by delivery deadline selected
            elif look_up_input == 'f' or look_up_input == 'F':
                package_delivery_deadline = input("enter a possible deadline, (9:00 AM/10:30 AM/EOD)\n")
                PackageClass.packagesHash.hash_look_up_deadline(package_delivery_deadline)

            # look up by delivery city selected
            elif look_up_input == 'G' or look_up_input == 'g':
                package_delivery_city = input("Please enter a city. \n")
                PackageClass.packagesHash.hash_look_up_city(package_delivery_city)

            # look up by delivery zipcode selected
            elif look_up_input == 'H' or look_up_input == 'h':
                print("known zipcodes:", PackageClass.known_zip_codes)
                package_delivery_zipcode = int(input("Please enter a zipcode: "))
                PackageClass.packagesHash.hash_look_up_zipcode(package_delivery_zipcode)

            # look up by package weight selected
            elif look_up_input == 'J' or look_up_input == 'j':
                package_weight = int(input("Please enter a weight: "))
                PackageClass.packagesHash.hash_look_up_weight(package_weight)

            # since the delivery of packages are not happening in real time you can only look up if the
            # packages are delivered. however, if the program was running in real time we would be able
            # to see if the packages are at the hub or en route. you will notice in the screen shots when checking
            # between times that the status of packages change from at the hub, to en route, and finally to delivered.
            elif look_up_input == 'K' or look_up_input == 'k':
                package_status = input("Please enter a status (at the hub/en route/delivered):")
                PackageClass.packagesHash.hash_look_up_status(package_status)

            # returns the user to main menu
            elif look_up_input == 'N' or look_up_input == "N":
                print("What would you like to do? (A/B/C)\n")
                print("A: Look up a package \n")
                print("C: Exit application \n")
                user_input = input("What would you like to do? \n")


# initializes the console
main_menu()
