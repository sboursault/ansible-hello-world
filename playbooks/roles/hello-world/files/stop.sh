#!/usr/bin/env bash

set -e # stop script on error
#set -x # print commands

HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#source $HOME/config

if pgrep -f "$HOME/app.py" >/dev/null 2>&1;
then
  pkill -f "$HOME/app.py"
  sleep 2
  echo "stopped"
else
  echo "not running"
fi
