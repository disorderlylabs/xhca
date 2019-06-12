#HDF5_VOL_CONNECTOR=provenance under_vol=0;under_info={};path=$YOUR_TRACE_FILE_PATH;level=2;format=
set trace_file_path    "resources/outputs/gene-expression.h5-provenance"
set HDF5_VOL_CONNECTOR provenance
#set HDF5_VOL_CONNECTOR "provenance under_vol=0;under_info={};path=$trace_file_path;level=2;format="
# set under_vol          0
# set under_info         {}
# set path               resources/outputs/gene-expression.h5-provenance
# set level              2
# set format

echo "HDF5 Plugin path: $HDF5_PLUGIN_PATH"
echo "HDF5 VOL plugin:  $HDF5_VOL_CONNECTOR"
poetry run python xhca/gene-expression.py
