# SandboxDataGenerator
Generate json file of sandbox data

## Setup
Start a virtual environment
```
virtualenv -p python3 venv
. venv/bin/activate
```

## installization
```bash
$ pip install --editable .
```

## Run
Only for Mexico now
Generate main sandbox data including users, 
banks, branches, accounts, atms, products and transactions
Generate customer data
### Initialization
```
$ obpfaker init
```

### Generate counterparty data
```
$ obpfaker generate-counterparty-file
```

### Generate Main data
```bash
$ obpfaker generate-main-file
```

### Import web initialization
```
$ obpfaker web-init
```

### Import main file to Sandbox Server
```
$ obpfaker import-main
```

### Import counterparty file to Sandbox Server
```
$ obpfaker import-counterparty
```

### Import customer file to Sandbox Server
```
$ obpfaker import-customer
```