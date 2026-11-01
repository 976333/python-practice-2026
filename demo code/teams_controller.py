def display(self) -> None:

    while True:

        print("\n" + "-" * 10, "MANAGE TEAMS", "-" * 10)
        print("1. Load starting data from file ->")
        print("2. Add a team ->")
        print("3. View all teams ->")
        print("4. View squad for a team ->")
        print("5. Edit team name/city ->")
        print("6. Delete a team ->")
        print("0. Back to main menu <-")
        print("-" * 35)

        choice = input("Enter your choice: ").strip()

        # Load starting data
        if choice == "1":

            input_path = Path("data/teams.csv")

            try:
                data = self.csv_parser(input_path)

                print(f"{len(data)} records loaded successfully.")

            except FileNotFoundError:
                print("CSV file not found.")

            except (ValueError, IndexError) as error:
                print(f"Error while reading CSV: {error}")

        # Add team
        elif choice == "2":

            team_name = input("Enter team name: ").strip()
            short_name = input("Enter short name: ").strip()
            home_city = input("Enter home city: ").strip()

            self.add_team(
                team_name,
                short_name,
                home_city
            )

        # View all teams
        elif choice == "3":

            self.view_teams()

        # View squad
        elif choice == "4":

            self.view_squad()

        # Edit team
        elif choice == "5":

            self.edit_team()

        # Delete team
        elif choice == "6":

            self.delete_team()

        # Back to main menu
        elif choice == "0":

            print("Returning to main menu...")
            break

        else:

            print("Invalid choice. Please try again.")