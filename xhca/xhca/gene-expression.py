import os
import sys

import numpy
import pandas
import scanpy

scanpy.settings.verbosity = 3
scanpy.logging.print_versions()

results_file = 'simple.output.h5ad'

class ClusteringWorkflow(object):
    @classmethod
    def from_matrix_h5(cls, path_to_matrix):
        """
        Factory function for reading gene expression matrix from hdf5 formatted
        10x output.
        """

        anndata_matrix = scanpy.read_10x_h5(path_to_matrix, gex_only=True)
        anndata_matrix.var_names_make_unique()

        return cls(anndata_matrix)

    @classmethod
    def from_matrix_mtx(cls, path_to_matrix):
        """
        Factory function for reading gene expression matrix from mtx formatted
        10x output.
        """

        anndata_matrix = scanpy.read_10x_mtx(path_to_matrix, gex_only=True)
        anndata_matrix.var_names_make_unique()

        return cls(anndata_matrix)

    def __init__(self, data_matrix, **kwargs):
        super().__init__(**kwargs)

        self._data_matrix = data_matrix

    def filter_top_expressive_genes(self, count=10):
        scanpy.pp.highest_expr_genes(self._data_matrix, n_top=count)
        
        return self

    def filter_top_variable_genes(self, count=None):
        scanpy.pp.highly_variable_genes(self._data_matrix, n_top_genes=count)

        return self

    def normalize_expression(self):
        scanpy.pp.normalize_total(self._data_matrix)

        return self

    def logarithmize(self):
        scanpy.pp.log1p(self._data_matrix)

        return self

    def preprocess_by_10x_method(self):
        """
        Provided preprocessing recipe:
            https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.recipe_zheng17.html

        That is based on the methods in the paper:
            Massively parallel digital transcriptional profiling of single cells
            https://www.nature.com/articles/ncomms14049.pdf
        """
        scanpy.pp.recipe_zheng17(self._data_matrix)

        return self

    def compute_neighborhood_graph(self):
        scanpy.pp.neighbors(self._data_matrix)

        return self

    def cluster_by_leiden(self):
        scanpy.tl.leiden(self._data_matrix)

        return self

    def interpret_clusters(self):
        print(self._data_matrix.obs)

if __name__ == '__main__':
    data = (
        ClusteringWorkflow.from_matrix_h5('resources/data/matrix.h5')
                          .preprocess_by_10x_method()
                          .compute_neighborhood_graph()
                          .cluster_by_leiden()
    )

    data.interpret_clusters()
