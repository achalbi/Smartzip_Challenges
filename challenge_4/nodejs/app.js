const fs = require('fs');
const csv = require('csv-stream');
const through2 = require('through2');
var csvWriter = require('csv-write-stream')

var writer = csvWriter()
// Preparing the output stream
writer.pipe(fs.createWriteStream('output.csv'))

console.time("Time_taken");

// Reading the input CSV file in Stream
const stream = fs.createReadStream('edi-contacts.csv')
  .pipe(csv.createStream({
    endLine: '\n',
    columns: ['id', 'firstname', 'lastname']
  }))
  .pipe(through2({
    objectMode: true
  }, (row, enc, cb) => {
    // - `row` holds the first row of the CSV,
    //   as: `{ id: '28660041', firstname: 'Shannon', lastname: 'Simpson' }`
    // - The stream won't process the *next* item unless you call the callback
    //  `cb` on it.
    // - This allows us to save the row in our process it and when
    //   we're done, we call `cb()` to move on to the *next* row.
    processEachRow(row);
    cb(null, true);
  }))
  .on('data', data => {
    // console.log('row processed');
  })
  .on('end', () => {
    // after completing the execution, close the write stream 
    writer.end();
    // Printing the time taken to complete execution
    console.timeEnd("Time_taken");
  })
  .on('error', err => {
    // print if error is thrown
    console.error(err);
  })

  const processEachRow = row => {
    // Match pattern to set flag
    // Pattern: allow alphanumeric characters, single space, semi-colon, single quote, & sign, and hyphen 
    // no special characters are allowed other than the above mentioned.
      const pattern = /^[A-Za-z0-9 ;&.'-]+$/;
      row.flag = pattern.test(row.firstname) && pattern.test(row.lastname);
      // row.raw_firstname = ''
      // row.raw_lastname = ''

      // Sanitizing Firstname and Lastname
      if (row.flag === false){
        // const sanitizing_pattern = /[^A-Za-z0-9& ;'-]/g;
        // row.raw_firstname = String(row.firstname)
        // row.raw_lastname = String(row.lastname)
        // row.firstname = String(row.firstname).replace(sanitizing_pattern, '');
        // row.lastname = String(row.lastname).replace(sanitizing_pattern, '');

        writer.write(row);

      }
      
      // if (row.id != 'id'){ // skip first row heading
      //   // write in stream also getting converted from json object to CSV
      //   writer.write(row);
      // }
  }