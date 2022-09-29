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

1. Run the bandwidth test to download the original images size

        python ./bandwidth-test/run.py --service SERVICE

1. Run the bandwidth test to download the decreased images size

    On the fly the maximum image dimension will be decreased to 700px and
    compression with 50% of quality will be used.

        python ./bandwidth-test/run.py --service SERVICE
