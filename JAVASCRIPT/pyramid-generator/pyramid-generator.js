const character = "!"; // The symbol used to build the pyramid
const count = 10; // Number of rows in the pyramid
const rows = []; // Array to store each row of the pyramid
let inverted = false; // If true, the pyramid is upside down

function padRow(rowNumber, rowCount) { // Builds one row of the pyramid
    return " ".repeat(rowCount - rowNumber) // Add spaces to center the row
        + character.repeat(2 * rowNumber - 1) // Add the pyramid symbols
        + " ".repeat(rowCount - rowNumber); // Add spaces after the symbols
}

for (let i = 1; i <= count; i++) { // Loop through each row number
    if (inverted) { // If the pyramid should be upside down
        rows.unshift(padRow(i, count)); // Add the row to the beginning
    } else {
        rows.push(padRow(i, count)); // Add the row to the end
    }
}

let result = "" // String to hold the full pyramid

for (const row of rows) { // Loop through each row in the array
    result = result + row + "\n"; // Add the row and a line break
}

console.log(result); // Show the pyramid in the console