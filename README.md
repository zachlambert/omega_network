# Managing environments

I'm developing this using conda on my laptop, but the host site pythonanywhere
doesn't support conda.
Therefore, need to export an requirements.txt file from conda, then create
the virtualenv from that.

To record the state of the conda environment:
conda list -e > requirements.txt 

To install these modules in a virtualenv:
source .../venv/bin/activate
(venv) pip -r requirements.txt
