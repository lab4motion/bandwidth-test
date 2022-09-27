# Setup environment

1. Configure virtual environment

        python3.8 -m venv ./venv
        source ./venv/bin/activate
        python3 -m pip install -r requirements.txt


1. Fill environments config

    Navigate to `./environments.py` and fill in the environment data.  
    If you don't know how to fill it, contact the author of this bandwidth test.


# Run environment

1. Run virtual environment

        source ./venv/bin/activate
        export PYTHONPATH=${PYTHONPATH}:${PWD}


# Bandwidth test

1. Run the bandwitch test

        python ./bandwidth-test/run.py --service SERVICE
