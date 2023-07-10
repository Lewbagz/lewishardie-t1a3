#!/bin/bash


# Check if Python is installed
if ! command -v python3 & /dev/null; then
    echo "Python3 is not installed, Intalling now"
    sudo apt-get update
    sudo apt-get install python3 -y
fi

# source .venv/bin/activate

# pip install -r requirements.txt

# python3 main.py

# echo "Setting execute permission on the script..."
# chmod +x "$0"
# chmod +x run.sh 
# deactivate

# chmod
# Create a virtual environment so the file is in a controlled reproducable environment

echo "Creating a virtual environment..."
Python3 -m venv .venv
source venv/bin/activate

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Installing..."
    # Install pip
    sudo apt-get install python3-pip -y
fi

# Install required dependencies
echo "Installing required dependencies..."
pip3 install -r requirements.txt


# Set execute permission on the script
echo "Setting execute permission on the script..."
chmod +x "$0"


# Run the Python script
echo "Running the Python script..."
python3 main.py

# rm -rf .venv .pytest_cache






# install venv

# make sure requirements

# install packages

# then run the program

# check if python is installed or not
# install it if not
# check if pip is installed
# install if not

# create virtual environment
# activate
# install packages
# run python program
# deactive