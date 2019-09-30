# Managing environments

To record the state of the conda environment in a yml file:
conda env export > environment.yml

To create an environment from this:
conda env create --prefix ./env --file environment.yml

To update an environment:
conda env update --prefix ./env --file enviornemtn.yml --prune
