# screens for grounds + the weather feature
from models.venue import Venue
from databases import Database
# for whether api data fetch 
import requests

class Manage_grounds:

    def __init__(self):
        self.grounds = []
        self.reports = []

        self.db_connection = Database()

        

    def add_ground(self):
        # current_ground =self.db.
        # take ground name
        ground_name = input("Enter ground name: ").strip()

        if not ground_name:
            print("ground name cannot be empty.")
            return

        existing_ground = self.db_connection.fetch_query("""SELECT venue_id FROM venues WHERE LOWER(venue_name) = LOWER(%s)""",(ground_name,))

        if existing_ground:
                print("Ground name already exists.")
                return

    
        city = input("Enter city: ").strip()

        if not city:
            print("City cannot be empty.")
            return

        try:
            latitude = float(input("Enter latitude: "))

            if not -90 <= latitude <= 90:
                print("Latitude must be between -90 and 90.")
                return

            longitude = float(input("Enter longitude: "))

            if not -180 <= longitude <= 180:
                print("Longitude must be between -180 and 180.")
                return

        except ValueError:
            print("Please enter valid numeric values.")
            return

        # new id genration logic 
        result = self.db_connection.fetch_query(
            """
            SELECT COALESCE(MAX(venue_id), 0) AS max_id FROM venues
            """
            )

        max_id = result[0]["max_id"]

        venue_id = max_id + 1

        # create Venue object
        venue = Venue(venue_id,ground_name,city,latitude,longitude)

        self.db_connection.execute_query(""" INSERT INTO venues (venue_id, venue_name, city, latitude, longitude) VALUES (%s, %s, %s, %s, %s)""",
                (
                    venue_id,
                    ground_name,
                    city,
                    latitude,
                    longitude
                )
            )

        print("ground added successfully")

    def view_ground(self):
        all_ground = self.db_connection.fetch_query("""
        SELECT venue_id, venue_name, city, latitude, longitude
        FROM venues
        ORDER BY venue_id
        """)

        if not all_ground:
            print("No grounds found.")
            return

        print("-" * 75)
        print("# Ground                   City        Latitude    Longitude")
        print("-" * 75)

        print("\n" + "-" * 80)
        print(
            f"{'ID':<5}"
            f"{'Ground':<25}"
            f"{'City':<15}"
            f"{'Latitude':<15}"
            f"{'Longitude':<15}"
        )
        print("-" * 80)

        # Display database records
        for ground in all_ground:
        
            print(
                    f"{ground['venue_id']:<5}"
                    f"{ground['venue_name']:<25}"
                    f"{ground['city']:<15}"
                    f"{ground['latitude']:<15.5f}"
                    f"{ground['longitude']:<15.5f}"
            )

        print("-" * 75)

    def edit_ground(self, ground_id):


        result = self.db_connection.fetch_query(
            """
            SELECT
                    venue_id,
                    venue_name,
                    city,
                    latitude,
                    longitude
                FROM venues
                WHERE venue_id = %s
                """,
                (ground_id,)
            )
        
        # Ground not found
        if not result:
            print("Ground not found.")
            return
        
        ground = result[0]

        print(f"\nEditing ground: {ground['venue_name']}")

        print("1. Ground name")
        print("2. City")
        print("3. Latitude")
        print("4. Longitude")

        choice = input("Enter what you want to edit: ").strip()

        # Edit ground name
        if choice == "1":
            new_name = input("Enter new ground name: ").strip()

            if not new_name:
                print("Ground name cannot be empty.")
                return

            # Check duplicate name
            duplicate = self.db_connection.fetch_query(
                        """
                        SELECT venue_id
                        FROM venues
                        WHERE LOWER(venue_name) = LOWER(%s)
                        AND venue_id != %s
                        """,
                        (new_name, ground_id)
                    )

            if duplicate:
                print("Ground name already exists.")
                return 
            
            # Update database
            self.db_connection.execute_query("""
                        UPDATE venues
                        SET venue_name = %s
                        WHERE venue_id = %s
                        """,
                        (new_name, ground_id)
                    )
            print("Ground name updated successfully.")
        # Edit city
        elif choice == "2":

            new_city = input("Enter new city: ").strip()

            if not new_city:
                print("City cannot be empty.")
                return

            # Update database
            self.db_connection.execute_query(
                """
                UPDATE venues
                SET city = %s
                WHERE venue_id = %s
                """,
                (new_city, ground_id)
            )
            print("City updated successfully.")

        # Edit latitude
        elif choice == "3":

            try:
                new_latitude = float(input("Enter new latitude: "))

                if not -90 <= new_latitude <= 90:
                    print("Latitude must be between -90 and 90.")
                    return

            except ValueError:
                print("Please enter a valid number.")
                return 
            
            # Update database
            self.db_connection.execute_query(
                        """
                        UPDATE venues
                        SET latitude = %s
                        WHERE venue_id = %s
                        """,
                        (new_latitude, ground_id)
                    )  
            print("Latitude updated successfully.")


        # Edit longitude
        elif choice == "4":

            try:
                new_longitude = float(input("Enter new longitude: "))

                if not -180 <= new_longitude <= 180:
                    print("Longitude must be between -180 and 180.")
                    return

            except ValueError:
                print("Please enter a valid number.")
                return
            # Update database
            self.db_connection.execute_query(
                        """
                        UPDATE venues
                        SET longitude = %s
                        WHERE venue_id = %s
                        """,
                        (new_longitude, ground_id)
                    )
            print("Longitude updated successfully.")
            
        else:
            print("Invalid choice.")

    def delete_ground(self, ground_id):

        # Find ground from database
        result = self.db_connection.fetch_query(
                """
                SELECT
                    venue_id,
                    venue_name,
                    city
                FROM venues
                WHERE venue_id = %s
                """,
                (ground_id,)
            )
        if not result:
            print("No grounds found.")
            return

        # Find the ground
        ground = result[0]

        print(
            f"\nGround found: "
            f"{ground['venue_name']}, {ground['city']}"
        )

        # Confirm deletion
        choice = input("Are you sure you want to delete this ground? (y/n): ").strip().lower()

        if choice not in ["y", "yes"]:
            print("Deletion cancelled.")
            return

        # Delete ground
        self.db_connection.execute_query(
                """
                DELETE FROM venues
                WHERE venue_id = %s
                """,
                (ground_id,)
            )

        print("Ground deleted successfully.")
        
# --------------------------------------------------------------------------------------------------------
# from this method work in api fetching and read the data 
    def fetch_weather(self, latitude, longitude):
        url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
        )

        try:
            response = requests.get(url,timeout=10)

            if response.status_code !=200:
                print("whather API request failed.")
                return None

            # Convert response to JSON
            data = response.json()
            # Get current weather
            weather = data.get("current_weather")

            if not weather:
                print("Current weather data not available.")
                return None

            temperature = weather.get("temperature")
            wind = weather.get("windspeed")
            code = weather.get("weathercode")

            if temperature is None or wind is None or code is None:
                print("Incomplete weather data received.")
                return None

            return {
                "temperature": temperature,
                "wind": wind,
                "code": code
            }
        
        except requests.RequestException:
            print("Unable to connect to weather API.")
            return None

        except ValueError:
                print("Invalid response received from weather API.")
                return None
        

    
    def match_day_report(self):
        # Check whether database contains any grounds
        all_ground = self.db_connection.fetch_query(
                """
                SELECT
                    venue_id,
                    venue_name,
                    city,
                    latitude,
                    longitude
                FROM venues
                ORDER BY venue_id
                """
        )
        
        if not all_ground:
            print("No grounds found.")
            return

        # Display grounds
        # Display available grounds
        print("\n" + "-" * 75)
        print(
                f"{'ID':<5}"
                f"{'Ground':<25}"
                f"{'City':<15}"
                f"{'Latitude':<15}"
                f"{'Longitude':<15}"
            )
        print("-" * 75)

        for ground in all_ground:
                print(
                    f"{ground['venue_id']:<5}"
                    f"{ground['venue_name']:<25}"
                    f"{ground['city']:<15}"
                    f"{ground['latitude']:<15.5f}"
                    f"{ground['longitude']:<15.5f}"
                )
        
        print("-" * 75)
        # Get ground ID
        try:
            ground_id = int(input("Enter ground ID: "))
        except ValueError:
            print("Please enter a valid ground ID.")
            return

        # Fetch selected ground from database
        result = self.db_connection.fetch_query(
                """
                SELECT
                    venue_id,
                    venue_name,
                    city,
                    latitude,
                    longitude
                FROM venues
                WHERE venue_id = %s
                """,
                (ground_id,)
            )

        # ground not found
        if not result:
                print("Ground not found.")
                return

        ground = result[0]

        latitude = ground["latitude"]
        longitude = ground["longitude"]

        # Fetch weather
        weather = self.fetch_weather(
            latitude,
            longitude
        )

        if weather is None:
                print(
                    "Unable to fetch weather. "
                    "Please check your internet connection."
                )
                return
        # Get weather code
        code = weather["code"]

        if not isinstance(code,int):
            print("invalid weather data receive")
            return
        
        if code == 0:
            condition = "Clear sky"
        elif code in [1, 2, 3]:
            condition = "Partly cloudy"
        elif code in [45, 48]:
            condition = "Fog"
        elif 51 <= code <= 67:
            condition = "Rain"
        elif 80 <= code <= 82:
            condition = "Rain showers"
        elif 95 <= code <= 99:
            condition = "Thunderstorm"
        else:
            condition = "Unknown"

        # Match-day advice
        if condition in ["Rain", "Rain showers", "Thunderstorm"]:
            advice = "Rain may stop play. Captains may prefer to bowl first."
        elif weather["wind"] > 20:
            advice = "Windy - helpful for swing bowlers."
        elif weather["temperature"] > 33:
            advice = "Very hot - keep drinks breaks ready."
        else:
            advice = "Good conditions for cricket."


        # Display report
        print("\n" + "=" * 50)
        print(f"MATCH-DAY REPORT - {ground['venue_name']}, {ground['city']}")
        print("=" * 50)
        print(f"Temperature : {weather['temperature']} C")
        print(f"Wind        : {weather['wind']} km/h")
        print(f"Condition   : {condition}")
        print(f"Advice      : {advice}")
        print("=" * 50)

    def back_to_menu(self):
        print("Returning to main menu...")
        return

    def display_ground_menu(self):

        while True:
            print("\n" + "-" * 30)
            print("      GROUND MENU")
            print("-" * 30)
            print("1. Add a ground")
            print("2. View all grounds")
            print("3. Edit a ground")
            print("4. Delete a ground")
            print("5. Match-day weather reports")
            print("0. Back to main menu")
            print("-" * 30)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_ground()

            elif choice == "2":
                self.view_ground()

            elif choice == "3":
                try:
                    ground_id = int(input("Enter ground ID: "))
                    self.edit_ground(ground_id)
                except ValueError:
                    print("Please enter a valid ground ID.")

            elif choice == "4":
                try:
                    ground_id = int(input("Enter ground ID: "))
                    self.delete_ground(ground_id)
                except ValueError:
                    print("Please enter a valid ground ID.")

            elif choice == "5":
                self.match_day_report()

            elif choice == "0":
                self.back_to_menu()
                break

            else:
                print("Invalid choice. Please try again")


ground = Manage_grounds()
ground.display_ground_menu()
