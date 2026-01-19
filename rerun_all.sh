#!/bin/bash

## RERUN Physics Lecture Notes

# Directory containing the .qmd files
TARGET_DIR="Lecture_Notes/Physics"

# Check if the directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist."
  exit 1
fi

# Change to the target directory
cd "$TARGET_DIR" || exit

# Iterate over all .qmd files in the directory
for qmd_file in *.qmd; do
  # Check if there are any .qmd files
  if [ -e "$qmd_file" ]; then
    echo "Rendering $qmd_file..."
    quarto render "$qmd_file"
  else
    echo "No .qmd files found in $TARGET_DIR."
    exit 0
  fi
done

# Change back to the original directory
cd ../../

# Automatyczne ustawienie katalogu głównego na bieżący katalog
ROOT_DIR=$(pwd)

# print the current directory
echo "Current directory: $ROOT_DIR"

# Tworzenie linków w katalogu Mechanics
cd "$ROOT_DIR/docs/Physics/Mechanics" || exit
ln -sf ../../../Lecture_Notes/Physics/Language_of_physics.html Language_of_physics.html
ln -sf ../../../Lecture_Notes/Physics/Mechanics.html Mechanics.html
ln -sf ../../../Lecture_Notes/Physics/Waves.html Waves.html

# Tworzenie linków w katalogu Electromagnetism
cd "$ROOT_DIR/docs/Physics/Electromagnetism" || exit
ln -sf ../../../Lecture_Notes/Physics/Electromagnetism.html Electromagnetism.html
ln -sf ../../../Lecture_Notes/Physics/Circuits.html Circuits.html

# Tworzenie linków w katalogu Experiments_Statistics
cd "$ROOT_DIR/docs/Physics/Experiments_Statistics" || exit
ln -sf ../../../Lecture_Notes/Physics/Measurement.html Measurement.html
ln -sf ../../../Lecture_Notes/Physics/Statistics.html Statistics.html

# Tworzenie linków w katalogu Modern_Physics
cd "$ROOT_DIR/docs/Physics/Modern_Physics" || exit
ln -sf ../../../Lecture_Notes/Physics/Quantum_mechanics.html Quantum_mechanics.html
ln -sf ../../../Lecture_Notes/Physics/Cosmology.html Cosmology.html
ln -sf ../../../Lecture_Notes/Physics/Relativity.html Relativity.html

# Powrót do katalogu głównego
cd "$ROOT_DIR" || exit

## RERUN Mathematics Lecture Notes

# Directory containing the .qmd files
TARGET_DIR="Lecture_Notes/Mathematics"

# Check if the directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist."
  exit 1
fi

# Change to the target directory
cd "$TARGET_DIR" || exit

# Iterate over all .qmd files in the directory
for qmd_file in *.qmd; do
  # Check if there are any .qmd files
  if [ -e "$qmd_file" ]; then
    echo "Rendering $qmd_file..."
    quarto render "$qmd_file"
  else
    echo "No .qmd files found in $TARGET_DIR."
    exit 0
  fi
done

# Change back to the original directory
cd ../../

# Automatyczne ustawienie katalogu głównego na bieżący katalog
ROOT_DIR=$(pwd)

# print the current directory
echo "Current directory: $ROOT_DIR"

# Tworzenie linków w katalogu Mathematics
cd "$ROOT_DIR/docs/Mathematics" || exit

ln -sf ../../Lecture_Notes/Mathematics/Linear_Algebra.html Linear_Algebra.html
ln -sf ../../Lecture_Notes/Mathematics/Analytic_Geometry.html Analytic_Geometry.html
ln -sf ../../Lecture_Notes/Mathematics/Calculus.html Calculus.html

# Powrót do katalogu głównego
cd "$ROOT_DIR" || exit

## RERUN Discrete Mathematics Lecture Notes

# Directory containing the .qmd files
TARGET_DIR="Lecture_Notes/Discrete_Mathematics"

# Check if the directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory $TARGET_DIR does not exist."
  exit 1
fi

# Change to the target directory
cd "$TARGET_DIR" || exit

# Iterate over all .qmd files in the directory
for qmd_file in *.qmd; do
  # Check if there are any .qmd files
  if [ -e "$qmd_file" ]; then
    echo "Rendering $qmd_file..."
    quarto render "$qmd_file"
  else
    echo "No .qmd files found in $TARGET_DIR."
    exit 0
  fi
done

# Change back to the original directory
cd ../../

# Automatyczne ustawienie katalogu głównego na bieżący katalog
ROOT_DIR=$(pwd)

# print the current directory
echo "Current directory: $ROOT_DIR"

# Tworzenie linków w katalogu Discrete_Mathematics
cd "$ROOT_DIR/docs/Discrete_Mathematics" || exit

ln -sf ../../Lecture_Notes/Discrete_Mathematics/Discrete_Mathematics.html Discrete_Mathematics.html

# Powrót do katalogu głównego
cd "$ROOT_DIR" || exit


# Deploy using mkdocs
echo "Deploying site with mkdocs..."

# print the current directory
pwd

mkdocs gh-deploy
#
#echo "All tasks completed successfully."
