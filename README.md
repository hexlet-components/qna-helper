# qna-helper

CLI-utility for answering questions stored in `.csv` using davinci-003. Output file is also `.csv`.

## Requirements

* Docker, Docker compose
* input filename should be _questions.csv_
* delimiter should be `;`

## Usage

Setup OPENAI_API_KEY in `.env` file.

```bash
make compose-setup
make compose
```

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
