import random


# Creates the hospital environment
class Hospital:

    def __init__(self):

        # Areas covered by the cleaning robot
        self.areas = [
            "Emergency Room",
            "ICU",
            "Operation Theatre",
            "General Ward",
            "Waiting Area",
            "Corridor",
            "Washroom",
            "Pharmacy"
        ]

        # Randomly decide which areas need cleaning
        self.condition = {
            area: random.choice(["Needs Cleaning", "Clean"])
            for area in self.areas
        }

        # Random obstacles like beds or wheelchairs
        self.obstacles = {
            area: random.choice([True, False])
            for area in self.areas
        }


# AI hospital cleaning robot
class HospitalCleaningRobot:

    def __init__(self, hospital):

        self.hospital = hospital

        # Robot's starting conditions
        self.battery = 100
        self.time = 60

        # Waste carrying capacity
        self.bin_capacity = 4
        self.bin_load = 0

        # Keep track of work completed
        self.cleaned_areas = 0
        self.obstacles_avoided = 0
        self.recharges = 0

    # Recharge the robot when the battery is low
    def recharge(self):

        print("Battery is low.")
        print("Returning to charging station...")

        self.battery = 100
        self.recharges += 1

        print("Robot fully recharged.")

    # Check battery before starting work
    def check_battery(self):

        if self.battery <= 20:
            self.recharge()

    # Empty the waste bin when it is full
    def check_bin(self):

        if self.bin_load >= self.bin_capacity:

            print("Waste bin is full.")
            print("Emptying waste bin.")

            self.bin_load = 0

    # Avoid beds, wheelchairs or other obstacles
    def check_obstacle(self, area):

        if self.hospital.obstacles[area]:

            print("Obstacle found.")
            print("Robot changes its path.")

            self.obstacles_avoided += 1
            self.battery -= 5
            self.time -= 2

    # Clean emergency room
    def clean_emergency(self):

        print("Cleaning emergency room.")
        print("Removing waste and cleaning floor.")

        self.time -= 8
        self.battery -= 10
        self.bin_load += 1

    # Disinfect ICU
    def clean_icu(self):

        print("Disinfecting ICU surfaces.")

        self.time -= 10
        self.battery -= 12
        self.bin_load += 1

    # Sterilize operation theatre
    def sterilize_ot(self):

        print("Sterilizing operation theatre.")

        self.time -= 12
        self.battery -= 15
        self.bin_load += 1

    # Clean general ward
    def clean_ward(self):

        print("Cleaning general ward.")

        self.time -= 6
        self.battery -= 8
        self.bin_load += 1

    # Clean waiting area
    def clean_waiting_area(self):

        print("Cleaning waiting area.")

        self.time -= 5
        self.battery -= 7
        self.bin_load += 1

    # Clean hospital corridor
    def clean_corridor(self):

        print("Cleaning corridor.")

        self.time -= 4
        self.battery -= 5

    # Sanitize washroom
    def clean_washroom(self):

        print("Sanitizing washroom.")

        self.time -= 7
        self.battery -= 9
        self.bin_load += 1

    # Clean pharmacy
    def clean_pharmacy(self):

        print("Cleaning pharmacy.")

        self.time -= 5
        self.battery -= 6
        self.bin_load += 1

    # Start the hospital cleaning process
    def start(self):

        print("\n================================")
        print("   AI HOSPITAL CLEANING ROBOT")
        print("================================")

        for area in self.hospital.areas:

            print("\nArea:", area)

            # Stop if working time is finished
            if self.time <= 0:
                print("Working time finished.")
                break

            # Recharge before working if needed
            self.check_battery()

            # Check for obstacles
            self.check_obstacle(area)

            # Clean only if the area needs cleaning
            if self.hospital.condition[area] == "Needs Cleaning":

                if area == "Emergency Room":
                    self.clean_emergency()

                elif area == "ICU":
                    self.clean_icu()

                elif area == "Operation Theatre":
                    self.sterilize_ot()

                elif area == "General Ward":
                    self.clean_ward()

                elif area == "Waiting Area":
                    self.clean_waiting_area()

                elif area == "Corridor":
                    self.clean_corridor()

                elif area == "Washroom":
                    self.clean_washroom()

                elif area == "Pharmacy":
                    self.clean_pharmacy()

                # Mark the area as cleaned
                self.hospital.condition[area] = "Clean"
                self.cleaned_areas += 1

                # Check bin after collecting waste
                self.check_bin()

            else:

                print("Area is already clean.")

            print("Battery:", self.battery, "%")
            print("Time remaining:", self.time, "minutes")
            print("Bin:", self.bin_load, "/", self.bin_capacity)

        self.report()

    # Display final result
    def report(self):

        print("\n========== FINAL REPORT ==========")

        print("Areas Cleaned     :", self.cleaned_areas)
        print("Obstacles Avoided :", self.obstacles_avoided)
        print("Recharges         :", self.recharges)
        print("Battery Remaining :", self.battery, "%")
        print("Time Remaining    :", self.time, "minutes")
        print(
            "Bin Load          :",
            self.bin_load,
            "/",
            self.bin_capacity
        )


# Create hospital
hospital = Hospital()

# Create cleaning robot
robot = HospitalCleaningRobot(hospital)

# Start cleaning
robot.start()
