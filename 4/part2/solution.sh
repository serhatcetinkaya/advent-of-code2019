#!/bin/bash

declare -i MIN
declare -i MAX
declare -i NUM
declare -i PREV
declare -i DIGIT
declare -i COUNT
declare -i FLAG

MIN=$(awk -F- '{ print $1 }' $1)
MAX=$(awk -F- '{ print $2 }' $1)
PREV=0
COUNT=0
FLAG=1

for NUM in $(seq $MIN $MAX)
do
  for ((DIGIT=0; DIGIT < ${#NUM}; DIGIT++))
  do
    if [ "$PREV" -gt "${NUM:$DIGIT:1}" ]
    then
      FLAG=0
      break
    else
      PREV=${NUM:$DIGIT:1}
    fi
  done
  PREV=0
  if [ "$FLAG" -eq 1 ]
  then
    for match in $(grep -oE '(.)\1+' <<< $NUM)
    do
      if [ ${#match} -eq 2 ]
      then
        COUNT=$COUNT+1
        break
      fi
    done
  fi
  FLAG=1
done

echo "Result: ${COUNT}"
