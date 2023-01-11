# qna-helper

CLI-utulite for answering questions stored in `.csv` using davinci-003. Output file is also `.csv`.

## Requirements

- python = "^3.11"
- pandas = "^1.5.2"
- openai = "^0.26.0"
- alive-progress = "^3.0.1"

## Installation

```bash
make fast-install
```

## Usage

```bash
usage: qna-helper [options]

answer questions using davinci-003

options:
  -h, --help            dispaly help for command
  -i INPUT_FILE, --input_file INPUT_FILE
                        csv file to parse
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        csv file to save answers
```
