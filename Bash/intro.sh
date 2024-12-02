#!/bin/bash
#enviroment setup, make bash folder
echo 'test'

#chmod +x intro
#./intro to execute

age=30
echo $age

#Case sensitive
#Space sensitive
#linux/unix
#everything in strings

#input
read age
echo $age

read -p "What is the password? " password
echo $password

#arithmetic expressions
y=5
x=10
echo $((x+y))

#rounding
echo "scale=2; $x/$y" | bc
#in terminal scale=2

expr $x + $y
let "answer $x + $y"

#if
if [ "$password" = "test" ]
then
    echo "Correct"
else
    echo "Incorrect"
fi

if (( 1 < 5 ))
then
    echo "true"
fi

#string escape sequences
echo "\$"

#loops
for i in {1..3}
do
    read -p "name: " name
    read -p "score: " score
    echo $score > testfolder/$name
done

#functions
grade () {
    read -p "name: " name
    read -p "score: " score
    echo $score > testfolder/$name
}

for i in {1..3}
do
    grade
done