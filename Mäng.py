import random
robot_win_counts = 0
user_win_counts = 0
viik = 0
ring = 0
while ring != 3:
    robot = ["kivi", "käärid", "paber"]
    random.shuffle(robot)
    user = input(("kivi... käärid... paber... üks... kaks... kolm, Valige: käärid, paber, kivi: "))
    print(f"Sinu valik on: {user}.\nRoboti valik on: {robot[0]}")
    if user not in robot:
        print("Palun valige kolmest variantidest: kivi, käärid,paber")
    else:
        if robot[0] == user:
            ring = ring +1
            viik = viik +1
            print("Viik")
        elif robot[0] == "kivi":
            if user == "käärid":
                ring = ring +1
                print("Aruvuti võit")
            elif user == "paber":
                user_win_counts = user_win_counts + 1
                ring = ring +1
                print("Inimine võit!")
        elif robot[0] == "käärid":
            if user == "paber":
                robot_win_counts = robot_win_counts + 1
                ring = ring +1
                print("Aruvuti võit")
            elif user == "kivi":
                user_win_counts = user_win_counts + 1
                ring = ring +1
                print("Inimine võit!")
        elif robot[0] == "paber":
             if user == "kivi":
                robot_win_counts = robot_win_counts +1
                ring = ring +1
                print("Aruvuti võit") 
             elif user == "käärid":
                user_win_counts = user_win_counts +1
                ring = ring +1
                print("Inimine võit!")    
print(f"Total:\nARVUTI VÕIT:{robot_win_counts}\nINIMINE VÕIT: {user_win_counts}\nVIIK:{viik}")

            
        


