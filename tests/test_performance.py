import warnings
import unittest

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    from xhca.gene_expression import ClusteringWorkflow

resources = {
    '10kpbmc-mtx': 'resources/data/raw-feature-bc-matrix',
    '10kpbmc-h5' : 'resources/data/10k-pbmc.h5'          ,
    'cord-blood' : 'resources/data/ica-cord-blood.h5'    ,
    'bone-marrow': 'resources/data/ica-bone-marrow.h5'   ,
}

def benchmark_hdf5_dataread(benchmark, resource_path):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        benchmark.pedantic(
            ClusteringWorkflow.from_matrix_h5,
            kwargs={ 'path_to_matrix': resource_path },
            rounds=15
        )

def benchmark_hdf5_dataprocessing(benchmark, resource_path):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        workflow_obj = ClusteringWorkflow.from_matrix_h5(resource_path)
        benchmark.pedantic(
            workflow_obj.filtered_clustering,
            kwargs={ 'copy': True },
            rounds=15
        )

def benchmark_mtx_dataread(benchmark, resource_path):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        benchmark.pedantic(
            ClusteringWorkflow.from_matrix_mtx,
            kwargs={ 'path_to_matrix': resource_path },
            rounds=15
        )

def benchmark_mtx_dataprocessing(benchmark, resource_path):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        workflow_obj = ClusteringWorkflow.from_matrix_mtx(resource_path)
        benchmark.pedantic(
            workflow_obj.filtered_clustering,
            kwargs={ 'copy': True },
            rounds=15
        )

# ------------------------------
# feature-count matrix | HDF5 Format
def skip_test_performance_10kpbmc_h5_read(benchmark):
    benchmark_hdf5_dataread(benchmark, resources.get('10kpbmc-h5'))

def skip_test_performance_10kpbmc_h5_process(benchmark):
    benchmark_hdf5_dataprocessing(benchmark, resources.get('10kpbmc-h5'))

# ------------------------------
# feature-count matrix | MTX Format
def skip_test_performance_10kpbmc_mtx_read(benchmark):
    benchmark_mtx_dataread(benchmark, resources.get('10kpbmc-mtx'))

def skip_test_performance_10kpbmc_mtx_process(benchmark):
    benchmark_mtx_dataprocessing(benchmark, resources.get('10kpbmc-mtx'))


# ------------------------------
# larger feature-count matrices | HDF5 Format
def skip_test_performance_cordblood_h5_read(benchmark):
    benchmark_hdf5_dataread(benchmark, resources.get('cord-blood'))

def skip_test_performance_cordblood_h5_process(benchmark):
    benchmark_hdf5_dataprocessing(benchmark, resources.get('cord-blood'))


def skip_test_performance_bonemarrow_h5_read(benchmark):
    benchmark_hdf5_dataread(benchmark, resources.get('bone-marrow'))

def skip_test_performance_bonemarrow_h5_process(benchmark):
    benchmark_hdf5_dataprocessing(benchmark, resources.get('bone-marrow'))
