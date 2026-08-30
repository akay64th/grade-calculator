This program calculates the final grade for ENPM 611. It is also your first hands-on look at a real Python codebase — how it is structured, how its modules depend on each other, and how small changes ripple through the code.

The program is split across four files in the `app/` directory:

- `grades.py` — the `Grades` class that stores each individual grade (quizzes, midterm, project, final)
- `grade_weights.py` — the `GradeWeights` class that holds the percentage weight assigned to each grade category
- `grade_calculator.py` — the `GradeCalculator` class with three static methods: one that computes the overall percentage from grades and weights, one that computes an optimistic percentage (assuming 100% on any missing grades), and one that converts a percentage to a letter grade
- `run.py` — the entry point that wires everything together and prints the result

<!-- markdownlint-disable MD024 -->
# Prerequisites

Before you can run this program you need three tools installed. Follow the instructions for your operating system.

## Python 3

Python is the language this program is written in.

### Windows

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest Python 3 installer.
2. Run the installer. On the first screen, **check the box "Add Python to PATH"** before clicking *Install Now*.
3. Open **Command Prompt** (`Win + R`, type `cmd`, press Enter) and verify the install:

   ```text
   python --version
   ```

   You should see something like `Python 3.12.x`.

### macOS

1. Open **Terminal** (Applications → Utilities → Terminal).
2. Install via [Homebrew](https://brew.sh) (recommended):

   ```bash
   brew install python3
   ```

   Or download the macOS installer from [https://www.python.org/downloads/](https://www.python.org/downloads/) and run the `.pkg` file.
3. Verify the install:

   ```bash
   python3 --version
   ```

   You should see something like `Python 3.12.x`.

---

## Visual Studio Code

VS Code is a free code editor well-suited to Python development.

### Windows

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com) and download the Windows installer (`.exe`).
2. Run the installer and accept the default options. Leave "Add to PATH" checked so you can open VS Code from the terminal.

### macOS

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com) and download the macOS `.zip`.
2. Unzip it, then drag **Visual Studio Code.app** into your **Applications** folder.
3. To open VS Code from the terminal, open VS Code, press `Cmd + Shift + P`, type `shell command`, and select **"Shell Command: Install 'code' command in PATH"**.

---

## Git

Git is the version control tool you will use to fork, clone, and submit your work.

### Windows

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) and download the installer.
2. Run the installer. The default options are fine — just click *Next* through each screen.
3. Open **Command Prompt** or **Git Bash** and verify:

   ```text
   git --version
   ```

### macOS

1. Open **Terminal** and run:

   ```bash
   git --version
   ```

   If Git is not installed, macOS will automatically prompt you to install the **Xcode Command Line Tools** — click *Install* and wait for it to finish.
   Alternatively, install via Homebrew:

   ```bash
   brew install git
   ```

2. Verify the install:

   ```bash
   git --version
   ```

---

## VS Code Extensions

Once VS Code is open, install these two extensions to get Python support and debugging:

1. Open the Extensions panel: `Ctrl+Shift+X` (Windows) or `Cmd+Shift+X` (macOS).
2. Search for and install each of the following:

| Extension | Publisher ID | What it does |
| --- | --- | --- |
| **Python** | `ms-python.python` | Syntax highlighting, IntelliSense, linting, and code navigation |
| **Python Debugger** | `ms-python.debugpy` | Breakpoints and step-through debugging in VS Code |

After installing, VS Code may ask you to select a Python interpreter. Click the notification (or press `Ctrl+Shift+P` / `Cmd+Shift+P` and type "Python: Select Interpreter") and choose the Python 3 version you just installed.

---

# Getting Started

Make sure you have Python 3 installed. You can check by running:

```bash
python3 --version
```

Fork this repository on GitHub, then clone your fork to your machine:

```bash
git clone https://github.com/<your-username>/grade-calculator
cd grade-calculator
```

Run the program:

```bash
python3 app/run.py
```

You should see output like:

```
GRADES --- Quiz 1: 0.78
Can't calculate final grade without all assignments graded
Can't calculate overall course grade without all individual grades.
If all other assignments are 100%, the overall course would be 98.9%, which is a A
```

Now you are ready for the exercises below. You can work on any of them in any order. If you feel up to it, try the advanced exercise.

# Exercises

(1) :green_circle: *EASY* | Before running anything, read `run.py`, `grades.py`, `grade_weights.py`, and `grade_calculator.py`. Based on reading the code alone, determine what percentage and letter grade `calculate_optimistic_course_percentage` would return if `quiz_1 = 0.78` and all other grades are `None`. Write your prediction as a comment in `run.py`, then run the program and check whether you were right. *Trace the call from `run.py` through `GradeCalculator.calculate_optimistic_course_percentage`, then into `calculate_course_percentage`. Follow the arithmetic step by step using the weights in `GradeWeights`: quizzes are 10%, midterm 20%, project 40%, final 30%. An optimistic run sets all `None` grades to `1.0` (100%) before calculating.*

(2) :green_circle: *EASY* | Fill in all five grades in `run.py` with realistic values (something like quiz_1=0.82, quiz_2=0.75, midterm=0.88, project=0.91, final=0.79) and update the program to print the final letter grade. Then change one grade at a time and observe how much the overall percentage moves. Which grade category has the most impact on your final grade, and why? Add a short comment in `run.py` explaining your finding. *Look at the weight assigned to each category in `GradeWeights`. The category with the highest weight moves the needle the most per percentage point gained or lost.*

(3) :thinking: *DOABLE* | The course currently averages `quiz_1` and `quiz_2`. Add a third quiz (`quiz_3`) to the `Grades` class and update `GradeCalculator.calculate_course_percentage` so all three quizzes are averaged together. Make sure the weights in `GradeWeights` still sum to exactly `1.0` after your change. Update `run.py` to set a value for `quiz_3` and verify the output still makes sense. *You will need to add `quiz_3` as a new field in `Grades.__init__` and `Grades.set_all`, update the `None` check and average in `calculate_course_percentage`, update the optimistic fallback in `calculate_optimistic_course_percentage`, and adjust `quizzes` in `GradeWeights` if you want the total weight to remain 10%.*

(4) :thinking: *DOABLE* | The current `calculate_letter_grade` method returns only `A`, `B`, `C`, `D`, or `F`. Extend it to support plus and minus grades (`A+`, `A`, `A-`, `B+`, `B`, `B-`, `C+`, `C`, `C-`, `D`) using the cutoffs below. Then test your implementation by calling the function directly in `run.py` with a handful of boundary values — for example `0.97`, `0.93`, `0.90`, `0.87`, `0.83`, `0.80` — and print each result to confirm the cutoffs are correct.

| Grade | Minimum percentage |
|-------|--------------------|
| A+    | 97%                |
| A     | 93%                |
| A−    | 90%                |
| B+    | 87%                |
| B     | 83%                |
| B−    | 80%                |
| C+    | 77%                |
| C     | 73%                |
| C−    | 70%                |
| D     | 60%                |
| F     | below 60%          |

*Replace the existing `if/elif` chain in `calculate_letter_grade` with one that covers each cutoff in descending order. Test boundary values carefully — off-by-one errors on `>=` vs `>` are the most common bug here.*

(5) :fire: *ADVANCED* | Add a second grading scheme called `ProjectHeavyWeights` where the project is worth 60% and quizzes are reduced to 5%, with midterm at 15% and final at 20%. Add this as a new class in `grade_weights.py` that extends `GradeWeights`. Then update `run.py` to compute and print the letter grade under both the standard scheme and the project-heavy scheme side by side. Finally, add a `# DESIGN REVIEW` comment block at the top of `grade_calculator.py` that answers: if a future grading scheme required replacing the final exam with two smaller exams, what would you have to change in the current design, and is that a lot or a little? *For the class, either inherit from `GradeWeights` and override the four weight attributes in `__init__`, or define `ProjectHeavyWeights` as a standalone class with the same four attributes. In `run.py`, instantiate both weight objects and call `calculate_course_percentage` twice — once with each. The design review is open-ended: there is no wrong answer, but a good one names specific methods and fields that would need to change.*
