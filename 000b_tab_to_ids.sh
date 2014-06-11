#!/usr/bin/bash 

if [ $# -eq 0 ]
 then
    echo "for each media_cloud_document*.tab file, remove the first line, cut for the first column, and write to stdout"
    echo "usage: bash $0 {input_folder} > {output_file}"
 exit
fi 

for f in `ls $1/media_cloud_documents*.tab` 
do
    tail -n +2 "$f" | cut -f1
done
