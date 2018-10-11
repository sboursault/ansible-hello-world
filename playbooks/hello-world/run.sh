#!/usr/bin/env bash

if pgrep -f "hello-world/app.py" >/dev/null 2>&1;
then
  echo "already running"
else
  nohup python ~/hello-world/app.py &
fi