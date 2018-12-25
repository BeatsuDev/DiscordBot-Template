
#!/usr/bin/env bash

# activate the python virtualenv
source ".venv/Scripts/activate"

# check if the virtualenv is activated
if [[ "$VIRTUAL_ENV" != "" ]] ; then
  echo "Virtual Environment activated"
else
  echo "Error activating Virtual Environment"
  exit 1
fi

# execute the bot
exec python run.py
