# Timestamp Converter

A simple Python package that converts a Unix timestamp to an ISO formatted timestamp.

## Usage
1. Clone this repo
```bash
   git clone https://github.com/alinali87/timestamp-converter.git
   cd timestamp-converter 
```
2. Install the package using poetry
```bash
poetry install
```
3. Use it
```python
from timestamp_converter import unix_to_timestamp, is_unixtimestamp

print(unix_to_timestamp(1609459200))  # Output: '2021-01-01T00:00:00'
print(is_unixtimestamp(1609459200))    # Output: True

```

## Development
This project uses Poetry and a Makefile to streamline common tasks.

Activate virtual environment  # TODO: check alternative command, this one doesn't work
```bash
poetry shell
```
Run code:
```bash
make run
```
Run tests with pytest
```bash
make test
```
Install the Package
```bash
make install
```
Build the Package
```bash
make build
```
Publish the Package to test.pypi
```bash
make publish
```
Add a dependency
```bash
poetry add <package_name>
```
Add a dev dependency
```bash
poetry add -D <package-name>
```
Remove a dependency
```bash
poetry remove --dev <package-name>
```