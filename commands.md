# Terminal Record: Cloudstep Software

## 1. Building the project: 
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
touch business_rules.py main.py .gitignore requirements.txt
mkdir tests
touch tests/test_business_rules.py
pip install pytest
pip freeze > requirements.txt
git init
git add .
git commit -m "initial commit with project structure"
git push
## 2. The virtual environment:
/Users/jrhodes17/ism3232-midterm/.venv/bin/python3
## 3. The project structure:
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init.py
    ├── __pycache__
    └── test_business_rules.py
## 4. Every function and test:
business_rules.py
3:def calculate_license_cost(seat_price: float, seats: int) -> float: 
7:def get_seat_discount(seats: int, education: bool = False) -> float:
21:def calculate_license_total(seat_price: float, seats: int, education: bool = False) -> float:
32:def needs_contract_review(total: float) -> bool:
36:def gets_trainer(seats: int, total: float) -> bool: 
40:def total_licensed(orders: list) ->float:
47:def largest_license( orders: list) -> str:
70:def format_license_line(company: str, total: float, contract_review: bool, trainer: bool) -> str:

tests/test_business_rules.py
13:def test_claculate_license_total_basic():
18:def test_calculate_license_total_education_flag():
24:def test_tier_one_limit_below():
29:def test_tier_one_limit_at():
34:def test_tier_one_limit_above():
39:def test_tier_two_limit_at():
44:def test_tier_two_limit_above():
49:def test_fee_limit_below():
54:def test_fee_limit_at():
59:def test_fee_limit_above():
64:def test_needs_contract_review_below():
68:def test_needs_contract_review_at():
72:def test_needs_contract_review_above():
76:def test_gets_trainer_seat_limit_at():
80:def test_gets_trainer_seat_limit_above():
84:def test_gets_trainer_total_limit_at():
88:def test_gets_trainer_total_limit_above():
92:def test_total_licensed_short_list():
101:def test_largest_license_standard():
109:def test_largest_license_with_tie():
## 5. Which files print:
commands.md
main.py
## 6. The commit history:
I have committed a total of 7 times. After the first commit only 3 files were changed. I had to change main.py once, business_rules.py 3 times, and test_business_rules.py 2 times after the inital commit.