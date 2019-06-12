function clear_caches
    sync; and echo 1 > /proc/sys/vm/drop_caches
    sync; and echo 2 > /proc/sys/vm/drop_caches
    sync; and echo 3 > /proc/sys/vm/drop_caches
end

function h5_perftest
    set num_iters $argv[1]
    set perfprofile_path $argv[2]

    clear_caches
    h5perf -A phdf5            \
           -i $num_iters       \
           -d 7                \
           --chunk             \
           > $perfprofile_path
end

function posix_perftest
    set num_iters $argv[1]
    set perfprofile_path $argv[2]

    clear_caches
    h5perf -A posix            \
           -i $num_iters       \
           -d 7                \
           --chunk             \
           > $perfprofile_path
end

# ------------------------------
# Main

set perfdir benchmarks/h5perf-parallel
mkdir -p $perfdir

for single_test_seq in (seq 10)
    set single_h5_testpath    $perfdir/single-phdf5.$single_test_seq.profile
    set single_posix_testpath $perfdir/single-posix.$single_test_seq.profile

    h5_perftest    1 $single_h5_testpath
    posix_perftest 1 $single_posix_testpath
end

for batch_test_seq in (seq 10)
    set batch_h5_testpath    $perfdir/batch-phdf5.$batch_test_seq.profile
    set batch_posix_testpath $perfdir/batch-posix.$batch_test_seq.profile

    h5_perftest    10 $batch_h5_testpath
    posix_perftest 10 $batch_posix_testpath
end
