SRC_URL=https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt
DATA_DIR=./files/data
DEST_PATH=${DATA_DIR}/global-temps-data.original.txt


mkdir -p ${DATA_DIR}
curl -o ${DEST_PATH} \
    ${SRC_URL}


(>&2 echo "Wrote to: ${DEST_PATH}")
