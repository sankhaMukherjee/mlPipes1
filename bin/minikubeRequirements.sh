#!/bin/bash

CPU=0
MEM=0
DISK=0
INTERNET=0
DOCKER=0

result=''
nCPU=$(("$(nproc)" + 0))

memory="$(free -m | grep 'Mem')"
memory=($memory) # convert into a string array
freeMemory=${memory[1]}
freeMemory=$(("$freeMemory" / 1024))


if [[ $nCPU -ge 2 ]]
then
    CPU=1
    temp=''
    temp="$temp\n+-------------[CPU Pass]-----------------"
    temp="$temp\n|    CPU needed = 2 or more"
    temp="$temp\n|    nummbr of CPUs = $nCPU"
    temp="$temp\n+----------------------------------------"
    result="$result\n$temp"
else
    temp=''
    temp="$temp\n+-------------[CPU FAIL]-----------------"
    temp="$temp\n|    CPU needed = 2 or more"
    temp="$temp\n|    nummbr of CPUs = $nCPU"
    temp="$temp\n+----------------------------------------"
    result="$result\n$temp"
fi

if [[ $freeMemory -ge 2 ]]
then
    MEMORY=1
    temp=''
    temp="$temp\n+-------------[memory Pass]-----------------"
    temp="$temp\n|    memory needed = 2GB or more"
    temp="$temp\n|    you have = $freeMemory GB of memory"
    temp="$temp\n+----------------------------------------"
    result="$result\n$temp"
else
    temp=''
    temp="$temp\n+-------------[memory Fail]-----------------"
    temp="$temp\n|    memory needed = 2GB or more"
    temp="$temp\n|    you have = $freeMemory GB of memory"
    temp="$temp\n+----------------------------------------"
    result="$result\n$temp"
fi


echo -e $result