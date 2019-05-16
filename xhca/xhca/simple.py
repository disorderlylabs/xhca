import os
import sys

import numpy
import pandas
import scanpy

scanpy.settings.verbosity = 3
scanpy.logging.print_versions()

results_file = 'simple.output.h5ad'

if __name__ == '__main__':
    ann_from_h5 = scanpy.read_10x_h5('resources/data/matrix.h5', gex_only=True)
    ann_from_h5.var_names_make_unique()

    ann_from_mtx = scanpy.read_10x_mtx('resources/data/raw-feature-bc-matrix', gex_only=True)
    ann_from_mtx.var_names_make_unique()

    print('h5 data: {}'.format(repr(ann_from_h5)))
    #print(ann_from_h5.chunk_X(select=[0, 1, 2, 3, 4, 5]))
    #print(ann_from_mtx.chunk_X(select=5))
    print('MTX data: {}'.format(repr(ann_from_mtx)))

    scanpy.pl.highest_expr_genes(ann_from_h5, n_top=10)
    scanpy.pl.highest_expr_genes(ann_from_h5, n_top=10)
