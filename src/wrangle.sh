DATA_DIR=./files/data
SRC_PATH=${DATA_DIR}/global-temps-data.original.txt
DEST_PATH=${DATA_DIR}/global-temps-data.wrangled.csv
HEADERS='year,annual_mean,lowess'

# set headers
echo  ${HEADERS} > ${DEST_PATH}



cat ${SRC_PATH} \
    | ack '^(.+?)\s+(.+?)\s+(.+)' \
        --output '$1,$2,$3'    \
    >> ${DEST_PATH}

(>&2 echo "Wrote to: ${DEST_PATH}")
