#!/usr/bin/env bash

set -e # stop script on error
#set -x # print commands

HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$HOME/stop.sh
$HOME/start.sh
