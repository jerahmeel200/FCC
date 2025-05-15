const character = "!"; // Character used to build the pyramid
const count = 10; // Number of rows in the pyramid
const rows = []; // Array to store each row of the pyramid
let inverted = false; // Flag to determine if the pyramid should be inverted

function padRow(rowNumber, rowCount) { // Function to generate a single row of the pyramid
    return " ".repeat(rowCount - rowNumber) // Add leading spaces for alignment
        + character.repeat(2 * rowNumber - 1) // Add the pyramid characters
        + " ".repeat(rowCount - rowNumber); // Add trailing spaces for alignment
}

for (let i = 1; i <= count; i++) { // Loop through each row number
    if (inverted) { // If inverted is true
        rows.unshift(padRow(i, count)); // Add the row to the beginning of the array
    } else {
        rows.push(padRow(i, count)); // Add the row to the end of the array
    }
}

let result = "" // Initialize the result string

for (const row of rows) { // Loop through each row in the rows array
    result = result + row + "\n"; // Add the row and a newline to the result
}

console.log(result); // Output the final pyramid to the console