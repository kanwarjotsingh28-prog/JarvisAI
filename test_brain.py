from backend.brain.brain import Brain

brain = Brain()

print("=" * 50)
print("           JARVIS AI TEST")
print("=" * 50)

while True:
    command = input("\nYou: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    result = brain.think(command)

    print("\nJarvis Analysis")
    print("------------------------------")
    print(f"Command     : {result['command']}")
    print(f"Intent      : {result['intent']}")
    print(f"Entity      : {result['entity']}")
    print(f"Destination : {result['destination']}")