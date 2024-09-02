cd ..
# Source the environment variables from the secrets file
set -a
. secrets-output/secrets.env
set +a
ls secrets-output/secrets.env
# Change directory to where the Python script is located
cd python-script-repo

# Run the Python script with environment variables
python test.py
