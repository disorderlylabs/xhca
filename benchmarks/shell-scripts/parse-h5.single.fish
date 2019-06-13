set simple_write_marker    "Write (1 iteration(s)):"
set openclose_write_marker "Write Open-Close (1 iteration(s)):"
set simple_read_marker     "Read (1 iteration(s)):"
set openclose_read_marker  "Read Open-Close (1 iteration(s)):"
            
            

function find_marker_data
    set data_marker $argv[1]
    set datapath    $argv[2]

    grep -m 1 -A1 $data_marker $datapath
end

# ------------------------------
# Main
set readwrite_markers $simple_write_marker    \
                      $openclose_write_marker \
                      $simple_read_marker     \
                      $openclose_read_marker

for readwrite_marker in $readwrite_markers
    for profile_ndx in (seq 10)
        find_marker_data $readwrite_marker "h5perf-parallel/cord-blood.single-phdf5.$profile_ndx.profile"
    end
end
