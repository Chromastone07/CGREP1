 <!-- Adding, Subtracting, and Dividing Two Numbers -->

<?php
// Function to add two numbers
function add($num1, $num2) {
    return $num1 + $num2;
}


// Function to subtract two numbers
function subtract($num1, $num2) {
    return $num1 - $num2;
}


// Function to divide two numbers
function divide($num1, $num2) {
    if ($num2 == 0) {
        return "Error: Division by zero";
    }
    return $num1 / $num2;
}


// Example usage
$num1 = 10;
$num2 = 5;


echo "Addition: " . add($num1, $num2) . "\n";
echo "Subtraction: " . subtract($num1, $num2) . "\n";
echo "Division: " . divide($num1, $num2) . "\n";
?>






<!-- Creating an Array and Finding Text Using Regex -->

<?php
// Create an array of strings
$strings = [
    "Hello, world!",
    "This is a test string.",
    "Another example string.",
    "PHP is fun.",
    "Regular expressions are powerful."
];


// Function to find a specific text in the array using regex
function findTextInArray($array, $pattern) {
    $results = [];
    foreach ($array as $string) {
        if (preg_match($pattern, $string)) {
            $results[] = $string;
        }
    }
    return $results;
}


// Example usage
$pattern = "/test|example/"; // Regex pattern to find "test" or "example"
$matchedStrings = findTextInArray($strings, $pattern);


echo "Strings matching the pattern:\n";
foreach ($matchedStrings as $matchedString) {
    echo $matchedString . "\n";
}
?>


