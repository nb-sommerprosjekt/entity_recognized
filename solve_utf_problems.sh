#!/bin/sh

find "$1" -type f -name "*.txt" | while read txt; do
  sed -i -e 's/[\00\01\02\03\04\05\06\07\08\0b\0e\0f\10\11\12\13\14\15\16\17\18\19\1a\1b\1c\1d\1e\1f\7f\80\81\82\83\84\85\86\87\88\89\8a\8b\8c\8d\8e\8f\90\91\92\93\94\95\96\97\98\99\9a\9b\9c\9d\9e\9f]//' $txt
  sed -i -e 's/[^a-zA-ZÆØÅæøå0-9.-\ ]//g' $txt
  echo "$txt is done";
done

