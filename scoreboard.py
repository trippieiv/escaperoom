def get_scores(game_id, player_scores):
    with open("scoreboard.txt", "r+") as file:
        scores_list = file.readlines()
    names = []
    times = []
    names.append(game_id)
    times.append(player_scores)
    for line in scores_list:
        if line[-1] == "\n":
            line = line[:-1]
        line = line.split()
        names.append(line[0])
        times.append(line[1])
    print("\t\t\t\t\t\t\t" , "SCOREBOARD" )
    print("\t\t\t\t" , "NAME" , "\t\t" , "TIME(s)")

    zipped = list(zip(names, times))
    zipped = sorted(zipped, key= lambda times : int(times[1]))

    for line in zipped:
        print("\t\t\t\t" , str(line[0]) , "\t\t", line[1])
    

#get_scores("jake", "124")
"""lines = inputfile.readlines()
        names = []
        times = []
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split()
            names.append(line[0])
            times.append(line[1])"""
