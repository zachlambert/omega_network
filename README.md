# Managing environments

Create a virtual environment with:<br>
python3 -m venv env

Activate the environment with:
cource env/bin/activate
!Note, if using conda too, make sure to deactivate it with "conda deactivate"

To record the installed packages:
pip freeze > requirements.txt

To install packages from the requirements file:
pip install -r requirements.txt

# Setting up configuration

To set environment variables for configuration, create a file called<br>
.flaskenv

Within this, set the following:
SECRET_KEY="<some secret key>"
DATABASE_URI="<sqlalchemy connection string>"
