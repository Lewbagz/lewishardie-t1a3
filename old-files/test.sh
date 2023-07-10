python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pytest

deactivate

rm -rf .venv .__pycache__

# check if python is installed or not
# install it if not
# check if pip is installed
# install if not

# create virtual environment
# activate
# install packages
# run python program
# deactive