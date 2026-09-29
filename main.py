# This is a cricket match predictor (My first big python program)
#First I will import all necessary modules required for the project

import datetime 
import json
from pathlib import Path
import math

#then the history file is created in the same folder as this program
His_file=Path(__file__).with_name("Cricket_predictor.json")

# making all the functions that we are gonna need

def team_name(generate):
    while True:
        name = input(generate).strip()
        if name:
            return name
        print("Please enter the team Name: ")

def rating_instar(get_team,skill):
    while True:
        try:
            rating = int(input(f"{get_team} {skill} rating (1-5): "))
            if 1 <= rating <=5:
                return rating
            print("Choose a number from 1 to 5")
        except ValueError:
            print("Please Enter the Whole number")

def get_option(generate,options):
# Returning one of the listed options
    option_ = "/".join(options)
    while True:
        answer=input(f"{generate} {option_}.").strip().lower()
        if answer in options:
            return answer
        print(f"Please choose one of the following: {option_}")

def team_n(get_team):
    print("\n")
    print(f"Rating for {get_team}")
    print("Rate based on your Judgement, on the scale of 1 to 5")
    return{"name": get_team, 
           "batting" : rating_instar(get_team, "batting"), 
          "bowling": rating_instar(get_team, "bowling"),
          "form" : rating_instar(get_team, "recent Form")}

def get_conditions(team1,team2,skill,points,reason,scores,notes):
    if team1[skill]>team2[skill]:
        scores["A"] = scores["A"] + points
        notes["A"].append(f"+{points}: stronger {reason}")
    elif (team2[skill] > team1[skill]):
        scores["B"] = scores["B"] + points
        notes["B"].append(f"+{points}: stronger {reason}")
    else:
        notes["shared"].append(f"No {reason} points: both teams have the same rating")

def claci_prediction(team1,team2,pitch,weather,boundary,toss_team,toss_choice):
    scores={"A" : team1["batting"]*3 + team1["bowling"]*3 + team1["form"]*2,
            "B" : team2["batting"]*3 + team2["bowling"]*3 + team2["form"]*2}

    notes = {"A":[] , "B":[] , "shared": []}

    if pitch == "batting":
        get_conditions(team1,team2,"batting",4,"Batting on friendly pitch",scores,notes)

    elif pitch =="bowling":
        get_conditions(team1,team2,"bowling",4,"Bowling on bowling-friendly pitch",scores,notes)

    if weather =="sunny":
        get_conditions(team1,team2,"batting",2,"Batting in sunny weather",scores,notes)

    elif weather == "cloudy":
        get_conditions(team1,team2,"bowling",3,"Bowling in Cloudy weather",scores,notes)

    else: #Humid weather or any other
        get_conditions(team1,team2,"bowling",2,"Bowling in Humid weather",scores,notes)

    if boundary == "small":
        get_conditions(team1,team2,"batting",2,"Batting on a ground with Small boundaries" , scores , notes)
    else:
        get_conditions(team1,team2,"bowling",2,"Bowling on a ground with large boundaries",scores,notes)

    #Toss also gets a small bonus advantage
    if toss_team in ("A","B"):
        scores[toss_team] += 1
        toss_name=team1["name"] if toss_team == "A" else team2["name"]
        notes[toss_team].append("+1: Won the Toss")

        batt_condition = pitch=="batting" or weather=="sunny" or boundary =="small"
        field_conditions = pitch == "bowling" or weather in ("cloudy", "humid") or boundary == "large"

        if (toss_choice == "bat" and batt_condition) or (toss_choice == "field" and field_conditions):
            scores[toss_team] +=1
            notes[toss_team].append(f"+1: chose to {toss_choice} in conditions that suit it")

        notes["shared"].append(f"{toss_name} won the toss and chose to {toss_choice}")

    #now formula for points we calculated into rough percentage.
    diff_points = scores["A"] - scores["B"]
    chance_a = 100 / (1+ math.exp(-diff_points / 12)) 
    chance_B = 100 - chance_a 

    if scores["A"] > scores["B"]:
        predicted_winner = team1["name"]
    elif scores["B"] > scores["A"]:
        predicted_winner = team2["name"]
    else:
        predicted_winner = "Tie in the points."

    return scores,notes,chance_a,chance_B,predicted_winner

def savemyprediction(team1,team2,pitch,weather,boundary,scores,chance_a,chance_B,winner):
    #add this to the JSON history file.
    try:
        with open(His_file,"r", encoding ="utf-8") as history_file:
            history = json.load(history_file)
        if not isinstance(history,list):
            history =[]
    except (FileNotFoundError, json.JSONDecodeError):
            history =[]

    entry={"Date": datetime.datetime.now().strftime("%Y-%m-%d %H-%M"),
           "teams": [team1["name"],team2["name"]],
           "conditions": {"pitch": pitch, "weather": weather,"boundary": boundary},
           "points": {team1["name"]: scores["A"],team2["name"]:scores["B"]},
           "Estimated_chances": {team1["name"]: round(chance_a), team2["name"]: round(chance_B)},
           "predicted_winner": winner}
    history.append(entry)

    with open(His_file,"w",encoding="utf-8") as history_file:
        json.dump(history,history_file,indent=2)

def main():
    print("*"*50)
    print("____________CRICKET MATCH PREDICTOR____________")
    print("*"*50)
    print("A Student project which predicts on probability if your team can win")
    print("It is only a rough guess, please don't take it to heart and loose hope in your favorites")

    name_a = team_name("Enter your team name: ")
    name_B = team_name("Enter your opponent team: ")
    while name_a.casefold() == name_B.casefold():
        print("Please enter two different team names.")
        name_B = team_name("Enter your opponent team: ")

    team1 = team_n(name_a)
    team2 = team_n(name_B)

    print("\n")
    print("Match conditions")
    pitch = get_option("Pitch", ("batting" ,"balanced", "bowling"))
    weather = get_option("weather", ("sunny", "cloudy","humid"))
    boundary = get_option("boundary size", ("small","large"))

    print(f"\nToss team : A = {name_a}, B={name_B}")
    toss_team = get_option("Who won the toss", ("a", "b","none")).upper()
    toss_choice="none"
    if toss_team != "NONE":
        toss_choice = get_option("Toss winner choose to",("bat","field"))

    scores,notes,chance_a,chance_B,winner = claci_prediction(team1,team2,pitch,weather,boundary,toss_team,toss_choice)

    print("\n")
    print("*"*50)
    print("                  PREDICTION") 
    print("*"*50)
    print(f"\n{name_a}: {scores['A']} points | estimated chance : {chance_a:.1f}%")
    print(f"\n{name_B}: {scores['B']} points | estimated chance : {chance_B:.1f}%")
    for note in notes ["B"]:
        print(f"{note}")

    for note in notes["shared"]:
        print(f"  {note}")

    if winner == "Tie in the points.":
        print("\n")
        print("Both Have same probability of winning ")
    else:
        print(f"\n My prediction: {winner} is more likely to win based on your input")
    print("Remember: this is a points based estimation and not a garanteed result")

    try:
        savemyprediction(team1,team2,pitch,weather,boundary,scores,chance_a,chance_B,winner)
        print(f"Prediction saved in {His_file.name}")
    except OSError:
        print("I could not save the prediction history file ")

if __name__== "__main__":
    main() 