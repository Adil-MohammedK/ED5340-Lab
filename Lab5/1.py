def sumRuns(player):
    # print(player)
    sum = 0
    # print(len(player))
    for x in range(player["Matches"]):
        sum += player["Match"+str(x+1)]
    return sum


def avgRuns(player):
    print(player)
    count = 0
    avg = float(player["Total"])/player["Matches"]
    return avg


def highestRun(Players):
    highest, count = Players["player1"]["Total"], "Player1"
    for player in Players:
        if Players[player]["Total"] > highest:
            highest = Players[player]["Total"]
            count = player
    print("Highest is: ", highest, " of ", count)


Players = {"player1": {}, "player2": {},
           "player3": {}, "player4": {}, "player5": {}}

for player in Players:
    print("Enter number of matches for ", player, " : ")
    matches = int(input())
    for x in range(matches):
        print("Enter runs in match ", x+1)
        Players[player]["Match"+str(x+1)] = int(input())
    Players[player]["Matches"] = matches

print(Players)

# Total Runs
for player in Players:
    Total = sumRuns(Players[player])
    Players[player]["Total"] = Total
# print(Players)

for player in Players:
    avg = avgRuns(Players[player])
    Players[player]["AvgRuns"] = avg
print(Players)
print(len(Players))

highestRun(Players)
