#!/usr/bin/env bash

set -e # stop script on error
#set -x # print commands

HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source $HOME/config

if pgrep -f "$HOME/app.py" >/dev/null 2>&1;
then
  echo "already running"
else
  nohup python $HOME/app.py &
  sleep 2
  if pgrep -f "$HOME/app.py" >/dev/null 2>&1;
  then
    echo "service started"
  else
    echo "failed to start"
    exit 1
  fi
fi