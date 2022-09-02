1. Configure virtual environment

        python3.8 -m venv ./venv
        source ./venv/bin/activate
        python3 -m pip install -r requirements.txt


1. Fill environments config

    Navigate to `configs/environments` and fill in the environment data.  
    If you don't know how to fill it, contact the author of this bandwidth test.


1. Run test

        python3.8 -m venv ./venv
        python ./bandwidth-test.py --service SERVICE
