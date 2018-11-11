# Setup and execution process

## System Pre-requisite:
  - nodejs and npm should be installed

## Project setup
  - Run ```npm install ``` in the project directory, this installs all the required dependencies.
  - Make sure input filename is same as the filename mentioned in the index.js line no. 13 or Change the input filename to 'edi-contacts.csv'.
  - The path of the file should be set as well or else move the file to project directory.

## About
Columns present in the input file are 'id', 'firstname', 'lastname' 

The input CSV is read in stream and new JSON object is created for each row. we are converting each row to JSON object for ease of processing. After processing, each object is converted to CSV row line item.

Three new columns are added to the output file, i.e: 'flag', 'raw_firstname', 'raw_lastname'

Each row is pattern matched, if valid then flag is set to true.
if invalid, then flag is set to false, data is corrected and also old/previous content of the firstname and lastname is moved to 'raw_firstname' and 'raw_lastname' respectively fro reference.

  ### Pattern to be matched:
  Allow alphanumeric characters, single space, semi-colon, single quote, & sign, and hyphen.
  No special characters are allowed other than the above mention.

## Usage
```sh
$ node app.js
```

### Note: The output file generated will be in the same project directory and name of the file would be 'output.csv'
  