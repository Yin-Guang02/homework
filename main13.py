class SmartSwitchMonitor:
    def __init__(self, initial_state=0b00000000):
        self.state = initial_state
        self.switch_names = {
            0: "Living Room Light",
            1: "Kitchen Fan",
            2: "Bedroom AC",
            3: "Main Gate Lock",
            4: "Geyser",
            5: "Balcony Light",
            6: "TV Power",
            7: "Security Camera"
        }

    def display_status(self):
        """Prints the binary representation and the status of each switch."""
        print("\n--- Current Smart Switch Monitor Status ---")
        binary_str = f"{self.state:08b}"
        print(f"Current State (Binary): {binary_str}")
        print("------------------------------------------")
        
        for position, name in self.switch_names.items():
            is_on = (self.state & (1 << position)) != 0
            status = "ON" if is_on else "OFF"
            print(f"Switch {position} [{name}]: {status}")
        print("------------------------------------------\n")

    def turn_on_switch(self, position):
        """Uses bitwise OR (|) to set a specific bit to 1."""
        if 0 <= position <= 7:
            mask = 1 << position
            self.state = self.state | mask
            print(f"✔ Turned ON: {self.switch_names[position]}")
        else:
            print("❌ Invalid switch position. Choose between 0 and 7.")

    def turn_off_switch(self, position):
        """Uses bitwise AND (&) with a inverted mask (~) to clear a specific bit to 0."""
        if 0 <= position <= 7:
            mask = ~(1 << position)
            self.state = self.state & mask
            print(f"✔ Turned OFF: {self.switch_names[position]}")
        else:
            print("❌ Invalid switch position. Choose between 0 and 7.")

if __name__ == "__main__":
    
    monitor = SmartSwitchMonitor()
    monitor.display_status()


    monitor.turn_on_switch(0)
    monitor.turn_on_switch(2)
    monitor.display_status()

    
    monitor.turn_on_switch(7)
    monitor.display_status()

    
    monitor.turn_off_switch(2)
    monitor.display_status()