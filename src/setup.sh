#!/bin/bash
 
# Check if Python is installed
echo "Checking to see if python is installed..."
if ! command -v python3 &/dev/null; 
    then
        echo "Python3 is not installed, Intalling now"
        sudo apt-get update
        sudo apt-get install python3 -y
fi
echo "Python 3 is installed.."

echo "Creating a virtual environment..."
python3 -m venv .venv

echo "Openning virtual environment..."
source .venv/bin/activate

# Check if pip is installed
if ! command -v pip3 &> /dev/null; 
    then
        echo "pip is not installed. Installing..."
        # Install pip
        sudo apt-get install python3-pip -y
fi

# Install required dependencies
echo "Installing required dependencies..."
pip3 install -r requirements.txt

# Set execute permission on the script
echo "Setting execute permission on the script..."
chmod +x "main.py"

echo "Setting up complete, all dependencies has been installed"

echo "------------------------------"
echo "------------------------------"
echo "Please run ./run.sh to execute"
echo "------------------------------"
echo "------------------------------"
