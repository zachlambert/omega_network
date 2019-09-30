# Managing environments

Create a virtual environment with:
python3 -m venv env

Activate the environment with:
cource env/bin/activate
!Note, if using conda too, make sure to deactivate it with "conda deactivate"

To record the installed packages:
pip freeze > requirements.txt

To install packages from the requirements file:
pip install -r requirements.txt
