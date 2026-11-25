def vacuum_cleaner(room_state, start="A"):
    """Clean a two-room world; room_state maps room names to 'Dirty' or 'Clean'."""
    room = start
    actions = []
    while "Dirty" in room_state.values():
        if room_state[room] == "Dirty":
            room_state[room] = "Clean"
            actions.append(f"Suck dirt in room {room}")
        else:
            room = "B" if room == "A" else "A"
            actions.append(f"Move to room {room}")
    return actions


if __name__ == "__main__":
    rooms = {"A": "Dirty", "B": "Dirty"}
    for action in vacuum_cleaner(rooms):
        print(action)
    print("Final state:", rooms)
