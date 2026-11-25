from itertools import permutations


def solve_send_more_money():
    letters = "SENDMORY"
    for digits in permutations(range(10), len(letters)):
        value = dict(zip(letters, digits))
        if value["S"] == 0 or value["M"] == 0:
            continue
        send = 1000 * value["S"] + 100 * value["E"] + 10 * value["N"] + value["D"]
        more = 1000 * value["M"] + 100 * value["O"] + 10 * value["R"] + value["E"]
        money = (10000 * value["M"] + 1000 * value["O"] + 100 * value["N"]
                 + 10 * value["E"] + value["Y"])
        if send + more == money:
            return send, more, money, value
    return None

if __name__ == "__main__":
    result = solve_send_more_money()
    if result:
        send, more, money, _ = result
        print(f"{send} + {more} = {money}")
    else:
        print("No solution found")
