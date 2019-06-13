import numpy
import pandas
import scanpy

import warnings
import unittest

scanpy.settings.verbosity = 3
scanpy.logging.print_versions()

resources = {
    '10kpbmc-mtx': 'resources/data/raw-feature-bc-matrix',
    '10kpbmc-h5' : 'resources/data/10k-pbmc.h5'          ,
    'cord-blood' : 'resources/data/ica-cord-blood.h5'    ,
    'bone-marrow': 'resources/data/ica-bone-marrow.h5'   ,
}

# ------------------------------
# Convenience Methods
def matrix_from_mtx(resource_path):
    anndata_matrix = scanpy.read_10x_mtx(resource_path, gex_only=True)
    anndata_matrix.var_names_make_unique()

    return anndata_matrix

def matrix_from_h5(resource_path):
    anndata_matrix = scanpy.read_10x_h5(resource_path, gex_only=True)
    anndata_matrix.var_names_make_unique()

    return anndata_matrix

def cluster_gene_expression(anndata_matrix):
    scanpy.pp.recipe_zheng17(anndata_matrix)
    scanpy.pp.neighbors(anndata_matrix)
    scanpy.tl.leiden(anndata_matrix)

def benchmark_h5_matrix_construction(benchmark, resource_path):
    benchmark.pedantic(matrix_from_h5, args=(resource_path,), rounds=1)

def benchmark_mtx_matrix_construction(benchmark, resource_path):
    benchmark.pedantic(matrix_from_mtx, args=(resource_path,), rounds=1)

def benchmark_clustering(benchmark, anndata_matrix):
    benchmark.pedantic(cluster_gene_expression, args=(anndata_matrix,), rounds=1)

def test_performance_matrix_construction_10kpbmc_h5(benchmark):
    benchmark_h5_matrix_construction(benchmark, resources.get('10kpbmc-h5'))

def test_performance_matrix_construction_10kpbmc_mtx(benchmark):
    benchmark_mtx_matrix_construction(benchmark, resources.get('10kpbmc-mtx'))

def test_performance_matrix_construction_cordblood_h5(benchmark):
    benchmark_h5_matrix_construction(benchmark, resources.get('cord-blood'))

def test_performance_matrix_construction_bonemarrow_h5(benchmark):
    benchmark_h5_matrix_construction(benchmark, resources.get('bone-marrow'))

def test_performance_end_to_end_10kpbmc_h5(benchmark):
    data_matrix = matrix_from_h5(resources.get('10kpbmc-h5'))
    benchmark_clustering(benchmark, data_matrix)

def test_performance_end_to_end_10kpbmc_mtx(benchmark):
    data_matrix = matrix_from_mtx(resources.get('10kpbmc-mtx'))
    benchmark_clustering(benchmark, data_matrix)

def test_performance_end_to_end_cordblood_h5(benchmark):
    data_matrix = matrix_from_h5(resources.get('cord-blood'))
    benchmark_clustering(benchmark, data_matrix)

def test_performance_end_to_end_bonemarrow_h5(benchmark):
    data_matrix = matrix_from_h5(resources.get('bone-marrow'))
    benchmark_clustering(benchmark, data_matrix)
