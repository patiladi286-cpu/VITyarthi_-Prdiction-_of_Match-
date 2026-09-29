__Cricket Match Predictor__

[All the inputs should be in small letters]

__Overview__

This is my beginner student project for predicting the likely winner of a cricket match. The program asks for each team's batting, bowling, and recent-form ratings, then uses the match conditions and toss result to calculate points and estimated chances of winning.

It is a simple points-based estimate made for learning and practice. It does not use real match statistics or guarantee the result.

__Features__

- Enter two team names and rate each team's batting, bowling, and recent form from 1 to 5.
- Choose the pitch, weather, and boundary size.
- Enter the toss winner and whether they chose to bat or field, or choose no toss winner.
- Calculate points and estimated winning chances for both teams.
- Save each prediction and its match details to `Cricket_predictor.json` beside the Python file.
- Check inputs such as empty team names, duplicate team names, invalid ratings, and unsupported choices.

__Technologies and tools used__

- Python 3.14
- Python standard-library modules: `datetime`, `json`, `pathlib`, and `math`
- A terminal or command prompt to run the program

No extra packages need to be installed.



__Run the Program__
## Run the project

### Requirements

- Python 3 installed
- Git installed

This project uses only Python’s standard library, so no extra packages need to be installed.

### 1. Clone the repository

Open Terminal, Command Prompt, or PowerShell and run:

```bash
git clone https://github.com/patiladi286-cpu/VITyarthi_-Prdiction-_of_Match-
```

### 2. Go to the project folder

```bash
cd VITyarthi_-Prdiction-_of_Match-
```

Make sure this folder contains `main.py`. If `main.py` is inside a subfolder, go into that folder before continuing.

### 3. Check that Python is available

On Windows:

```bash
py 3.14version
```


### 4. Start the program

On Windows:

```bash
py main.py
```

If `py` is unavailable, try:

```bash
python main.py
```


### 5. Enter the match details

Follow the prompts in the terminal. Enter two different team names, ratings from 1 to 5, and the match conditions. Use the options shown by the program for the pitch, weather, boundary size, and toss.[All the inputs should be in small letters]

The program displays the teams’ points, estimated chances, and predicted winner. After a prediction is saved, the program creates or updates `Cricket_predictor.json` in the same folder as `main.py`.


__Testing instructions__

There is no separate automated test file in this project. To check the program manually:

1. Run it and enter two different team names with ratings from 1 to 5.
2. Try an invalid rating, such as `0` or a word, and check that the program asks again.
3. Try entering the same team name twice and check that it asks for a different opponent.
4. Complete a prediction using different pitch, weather, and boundary choices. Try toss choices for team A, team B, and `none`.
5. Confirm that the program prints points and estimated chances, and that `Cricket_predictor.json` is created or updated with the prediction.
   # Algorithm and Pseudocode: Cricket Match Predictor

__Algorithm__

**Inputs:** Two team names; each team’s batting, bowling, and recent-form ratings; pitch, weather, and boundary conditions; toss winner and toss choice, if applicable.

**Output:** Each team’s points and estimated winning chance, the predicted winner or a points tie, and a saved prediction-history record.

1. Ask the user for two non-empty team names. If the names are identical when compared without regard to letter case, ask for a different opponent name.
2. For each team, collect batting, bowling, and recent-form ratings. Accept only whole numbers from 1 to 5.
3. Collect the match conditions:
   - Pitch: batting, balanced, or bowling
   - Weather: sunny, cloudy, or humid
   - Boundary size: small or large
4. Ask who won the toss. If Team A or Team B won, ask whether they chose to bat or field.
5. Calculate each team’s base score:

   `Base score = (batting rating × 3) + (bowling rating × 3) + (form rating × 2)`

6. Apply condition bonuses to the team with the higher rating in the relevant skill:
   - Batting pitch: +4 to the team with the higher batting rating
   - Bowling pitch: +4 to the team with the higher bowling rating
   - Sunny weather: +2 to the team with the higher batting rating
   - Cloudy weather: +3 to the team with the higher bowling rating
   - Humid weather: +2 to the team with the higher bowling rating
   - Small boundaries: +2 to the team with the higher batting rating
   - Large boundaries: +2 to the team with the higher bowling rating
   - If the relevant ratings are equal, award no points for that condition.
7. If Team A or Team B won the toss, add 1 point to that team. Add 1 more point if the toss choice matches at least one favorable condition:
   - Batting conditions: batting pitch, sunny weather, or small boundaries
   - Fielding conditions: bowling pitch, cloudy or humid weather, or large boundaries
8. Find the point difference and calculate the estimated chances:

   `Team A chance = 100 / (1 + exp(-(Team A points - Team B points) / 12))`

   `Team B chance = 100 - Team A chance`

9. Predict the team with more points as the winner. If the points are equal, report a points tie.
10. Display the scores, estimated chances, prediction, and notes. The current program displays Team B’s notes and shared notes, but not Team A’s notes.
11. Try to load the existing `Cricket_predictor.json` history. If it is missing, invalid JSON, or not a list, start with an empty history.
12. Append the current prediction, including its date, teams, conditions, points, rounded chances, and predicted winner. Save the updated history. If saving fails due to an operating-system error, display a save-failure message.

The percentage calculation is a points-based estimate; it is not a trained or empirically calibrated prediction model.

__Pseudocode__

```text
CONSTANT HISTORY_FILE = "Cricket_predictor.json"

FUNCTION GET_TEAM_NAME(prompt):
    REPEAT:
        name = TRIM(INPUT(prompt))
        IF name is not empty:
            RETURN name
        DISPLAY "Please enter the team name"

FUNCTION GET_RATING(team_name, skill):
    REPEAT:
        TRY:
            rating = INTEGER(INPUT(team_name + skill + " rating (1-5)"))
            IF rating >= 1 AND rating <= 5:
                RETURN rating
            DISPLAY "Choose a number from 1 to 5"
        CATCH invalid integer:
            DISPLAY "Please enter a whole number"

FUNCTION GET_OPTION(prompt, allowed_options):
    REPEAT:
        answer = LOWERCASE(TRIM(INPUT(prompt)))
        IF answer is in allowed_options:
            RETURN answer
        DISPLAY the allowed options

FUNCTION GET_TEAM_RATINGS(team_name):
    RETURN a team record containing:
        name = team_name
        batting = GET_RATING(team_name, "batting")
        bowling = GET_RATING(team_name, "bowling")
        form = GET_RATING(team_name, "recent form")

FUNCTION AWARD_CONDITION_POINTS(team_A, team_B, skill, points, reason,
                               scores, notes):
    IF team_A[skill] > team_B[skill]:
        scores[A] = scores[A] + points
        ADD the points and reason to notes[A]
    ELSE IF team_B[skill] > team_A[skill]:
        scores[B] = scores[B] + points
        ADD the points and reason to notes[B]
    ELSE:
        ADD a shared note that neither team receives points for this condition

FUNCTION PREDICT(team_A, team_B, pitch, weather, boundary,
                 toss_team, toss_choice):

    scores[A] = team_A.batting * 3
                + team_A.bowling * 3
                + team_A.form * 2

    scores[B] = team_B.batting * 3
                + team_B.bowling * 3
                + team_B.form * 2

    notes[A] = empty list
    notes[B] = empty list
    notes[shared] = empty list

    IF pitch is "batting":
        AWARD_CONDITION_POINTS(team_A, team_B, "batting", 4,
                               "batting-friendly pitch", scores, notes)
    ELSE IF pitch is "bowling":
        AWARD_CONDITION_POINTS(team_A, team_B, "bowling", 4,
                               "bowling-friendly pitch", scores, notes)

    IF weather is "sunny":
        AWARD_CONDITION_POINTS(team_A, team_B, "batting", 2,
                               "sunny weather", scores, notes)
    ELSE IF weather is "cloudy":
        AWARD_CONDITION_POINTS(team_A, team_B, "bowling", 3,
                               "cloudy weather", scores, notes)
    ELSE:
        AWARD_CONDITION_POINTS(team_A, team_B, "bowling", 2,
                               "humid weather", scores, notes)

    IF boundary is "small":
        AWARD_CONDITION_POINTS(team_A, team_B, "batting", 2,
                               "small boundaries", scores, notes)
    ELSE:
        AWARD_CONDITION_POINTS(team_A, team_B, "bowling", 2,
                               "large boundaries", scores, notes)

    IF toss_team is A OR toss_team is B:
        scores[toss_team] = scores[toss_team] + 1

        batting_conditions =
            pitch is "batting" OR weather is "sunny" OR boundary is "small"

        fielding_conditions =
            pitch is "bowling" OR weather is "cloudy" OR
            weather is "humid" OR boundary is "large"

        IF (toss_choice is "bat" AND batting_conditions) OR
           (toss_choice is "field" AND fielding_conditions):
            scores[toss_team] = scores[toss_team] + 1
            ADD a suitable toss-choice note

        ADD a shared note naming the toss winner and choice

    difference = scores[A] - scores[B]
    chance_A = 100 / (1 + EXP(-difference / 12))
    chance_B = 100 - chance_A

    IF scores[A] > scores[B]:
        winner = team_A.name
    ELSE IF scores[B] > scores[A]:
        winner = team_B.name
    ELSE:
        winner = "Tie in the points."

    RETURN scores, notes, chance_A, chance_B, winner

MAIN:
    DISPLAY the program title and disclaimer

    name_A = GET_TEAM_NAME("Enter your team name")
    name_B = GET_TEAM_NAME("Enter your opponent team")

    WHILE LOWERCASE(name_A) equals LOWERCASE(name_B):
        DISPLAY "Please enter two different team names"
        name_B = GET_TEAM_NAME("Enter your opponent team")

    team_A = GET_TEAM_RATINGS(name_A)
    team_B = GET_TEAM_RATINGS(name_B)

    pitch = GET_OPTION("Pitch", ["batting", "balanced", "bowling"])
    weather = GET_OPTION("Weather", ["sunny", "cloudy", "humid"])
    boundary = GET_OPTION("Boundary size", ["small", "large"])
    toss_team = UPPERCASE(
        GET_OPTION("Who won the toss", ["a", "b", "none"])
    )

    IF toss_team is not "NONE":
        toss_choice = GET_OPTION("Toss winner chose to", ["bat", "field"])
    ELSE:
        toss_choice = "none"

    scores, notes, chance_A, chance_B, winner =
        PREDICT(team_A, team_B, pitch, weather, boundary,
                toss_team, toss_choice)

    DISPLAY each team's points and estimated chance
    DISPLAY notes[B] and notes[shared]
    DISPLAY winner or points-tie message
    DISPLAY that the estimate is not guaranteed

    TRY:
        history = READ_JSON(HISTORY_FILE)
        IF history is not a list:
            history = empty list
    CATCH file missing or invalid JSON:
        history = empty list

    CREATE a history record with:
        current date and time
        both team names
        pitch, weather, and boundary
        both teams' points
        both teams' rounded estimated chances
        predicted winner

    ADD the record to history

    TRY:
        WRITE history as formatted JSON to HISTORY_FILE
        DISPLAY "Prediction saved"
    CATCH operating-system error:
        DISPLAY "Could not save prediction history"
```

