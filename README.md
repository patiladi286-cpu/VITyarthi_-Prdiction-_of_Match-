# Cricket Match Predictor

## Overview

This is my beginner student project for predicting the likely winner of a cricket match. The program asks for each team's batting, bowling, and recent-form ratings, then uses the match conditions and toss result to calculate points and estimated chances of winning.

It is a simple points-based estimate made for learning and practice. It does not use real match statistics or guarantee the result.

## Features

- Enter two team names and rate each team's batting, bowling, and recent form from 1 to 5.
- Choose the pitch, weather, and boundary size.
- Enter the toss winner and whether they chose to bat or field, or choose no toss winner.
- Calculate points and estimated winning chances for both teams.
- Save each prediction and its match details to `Cricket_predictor.json` beside the Python file.
- Check inputs such as empty team names, duplicate team names, invalid ratings, and unsupported choices.

## Technologies and tools used

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
cd VITyarthi_(Prdiction _of_Match)
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

Follow the prompts in the terminal. Enter two different team names, ratings from 1 to 5, and the match conditions. Use the options shown by the program for the pitch, weather, boundary size, and toss.

The program displays the teams’ points, estimated chances, and predicted winner. After a prediction is saved, the program creates or updates `Cricket_predictor.json` in the same folder as `main.py`.


## Testing instructions

There is no separate automated test file in this project. To check the program manually:

1. Run it and enter two different team names with ratings from 1 to 5.
2. Try an invalid rating, such as `0` or a word, and check that the program asks again.
3. Try entering the same team name twice and check that it asks for a different opponent.
4. Complete a prediction using different pitch, weather, and boundary choices. Try toss choices for team A, team B, and `none`.
5. Confirm that the program prints points and estimated chances, and that `Cricket_predictor.json` is created or updated with the prediction.

