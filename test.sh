 #!/bin/bash

 ARRAY=(`systeminfo.exe /fo list`)
 SDate=(`echo ${ARRAY[46]} | perl -pe 's/,//g; s/\r\n//m'`)
 STime=${ARRAY[47]}
 SUTC=(`date -d "$SDate $STime" '+%s'`)
 NDate=(`date "+%Y/%m/%d"`)
 NTime=(`date "+%H:%M:%S"`)
 NUTC=(`date "+%s"`)
 DiffTime=(`expr \( $NUTC - $SUTC \) / 60 / 60`)

 echo "起動は" $SDate $STime
 echo "現在は" $NDate $NTime
 echo "経過時間は" $DiffTime "時間"