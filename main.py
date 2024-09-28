class TrainingSchedule:
    def _init_(self):
        self.schedules = []

    def add_schedule(self):
        sport = input("Enter the sport: ")
        days = input("Enter training days (separated by commas): ").split(",")
        time = input("Enter training time (e.g., 5:00 PM - 7:00 PM): ")
        coach = input("Enter the coach's name: ")

        schedule = {
            'sport': sport,
            'days': [day.strip() for day in days],
            'time': time,
            'coach': coach
        }

        self.schedules.append(schedule)
        print(f"\nSchedule for {sport} has been added!\n")

    def display_schedules(self):
        if not self.schedules:
            print("No schedules available.")
            return
        
        for idx, schedule in enumerate(self.schedules):
            print(f"{idx + 1}. Training Schedule for {schedule['sport']}:")
            print(f"   Days: {', '.join(schedule['days'])}")
            print(f"   Time: {schedule['time']}")
            print(f"   Coach: {schedule['coach']}")
            print("-" * 30)

    def update_schedule(self):
        self.display_schedules()
        if not self.schedules:
            return
        
        index = int(input("Enter the schedule number to update: ")) - 1
        if index < 0 or index >= len(self.schedules):
            print("Invalid schedule number.")
            return
        
        sport = input("Enter the new sport (leave blank to keep current): ")
        days = input("Enter new training days (separated by commas, leave blank to keep current): ")
        time = input("Enter new training time (leave blank to keep current): ")
        coach = input("Enter new coach's name (leave blank to keep current): ")

        if sport:
            self.schedules[index]['sport'] = sport
        if days:
            self.schedules[index]['days'] = [day.strip() for day in days.split(",")]
        if time:
            self.schedules[index]['time'] = time
        if coach:
            self.schedules[index]['coach'] = coach

        print(f"\nSchedule for {self.schedules[index]['sport']} has been updated!\n")

    def delete_schedule(self):
        self.display_schedules()
        if not self.schedules:
            return

        index = int(input("Enter the schedule number to delete: ")) - 1
        if index < 0 or index >= len(self.schedules):
            print("Invalid schedule number.")
            return
        
        deleted_schedule = self.schedules.pop(index)
        print(f"\nSchedule for {deleted_schedule['sport']} has been deleted!\n")


# Creating an instance of the class
academy = TrainingSchedule()

# Loop to allow users to add, update, display, or delete schedules
while True:
    print("1. Add a new training schedule")
    print("2. Display all training schedules")
    print("3. Update an existing training schedule")
    print("4. Delete an existing training schedule")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        academy.add_schedule()
    elif choice == '2':
        academy.display_schedules()
    elif choice == '3':
        academy.update_schedule()
    elif choice == '4':
        academy.delete_schedule()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
