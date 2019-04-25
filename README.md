# SandboxDataGenerator
Generate json file of sandbox data

## Setup
Start a virtual environment
```
virtualenv -p python3 venv
. venv/bin/activate
```

## Run
Only for Mexico now
Generate main sandbox data including users, 
banks, branches, accounts, atms, products and transactions
Generate customer data
```
$ python run_script/GenerateMexico.py
```

Generate counterparty data
```
$ python run_script/GenerateCounterpartyJson.py
```
