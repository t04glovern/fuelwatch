# Fuel Watch

## Requirements

- Install [python3](https://www.python.org/downloads/) (I used version 3.9 here).

## Setup Environment

```bash
python3 -m venv ./venv
source venv/bin/activate

python3 -m pip install --upgrade pip
pip install requirements.txt
```

## Run the Code

```bash
python fuelwatch.py
[{'address': '66 Sylvia St',
  'date': '2021-10-12',
  'price': 151.7,
  'suburb': 'NOLLAMARA'},
 {'address': '66 Sylvia St',
  'date': '2021-10-11',
  'price': 153.7,
  'suburb': 'NOLLAMARA'},
 {'address': '174 Balcatta Rd',
  'date': '2021-10-12',
  'price': 155.9,
  'suburb': 'BALCATTA'},

...

]
```

## Attribution

Based off of the work by [Volk101](https://github.com/Volk101) in [https://github.com/Volk101/fuelwatch_parser.py](https://github.com/Volk101/fuelwatch_parser.py)
