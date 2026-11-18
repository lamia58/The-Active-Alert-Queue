# SOC Alert Queue Lab

alert_queue = []

while True:
    print()
    print("1. Log New Alert")
    print("2. View Active Queue")
    print("3. Resolve Oldest Alert")
    print("4. Exit System")
    choice = input("Enter your choice: ")

    if choice == "1":
        alert = input("Enter threat description: ")
        alert_queue.append(alert)
        print("Alert logged successfully!")

    elif choice == "2":
        print("--- Current Pending Alerts ---")
        for alert in alert_queue:
            print(alert)

    elif choice == "3":
        if len(alert_queue) > 0:
            resolved_threat = alert_queue.pop(0)
            print("Resolved and cleared: " + resolved_threat)
        else:
            print("There are no alerts to resolve.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
