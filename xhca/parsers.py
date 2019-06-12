import os
import sys

import pandas

from xhca.util import files_from_dir

class GeneSetParser(object):
    MSI_GENE_DB_PATH = 'resources/data/gene-sets/msigdb-v6.2'

    @classmethod
    def gene_ids_from_msi(cls):
        data_dir = os.path.join(cls.MSI_GENE_DB_PATH, 'gene-id-maps')

        msi_gene_id_df = None
        for dir_entry, dir_abspath in files_from_dir(data_dir):
            if not msi_gene_id_df:
                msi_gene_id_df = cls.parse_file_gene_matrix_transposed(dir_abspath)
            else:
                msi_gene_id_df.append(cls.parse_file_gene_matrix_transposed(dir_abspath))

        return msi_gene_id_df

    @classmethod
    def parse_file_gene_matrix_transposed(cls, path_to_gmt):
        gene_symbols = []
        mapped_vals  = []

        with open(path_to_gmt, 'r') as gmt_handle:
            for line in gmt_handle:
                gmt_fields = line.split()

                gene_symbols.append(gmt_fields[0])
                mapped_vals.append(gmt_fields[2:])

        return pandas.DataFrame(
            data=mapped_vals,
            index=gene_symbols
        )

class H5PerfParser(object):
    marker_end_of_param = '==== End of Parameters ===='

    @classmethod
    def from_perf_profile(cls, perf_profile_path):
        with open(perf_profile_path) as perf_handle:
            for param_line in perf_handle:
                # advance file handle until the interesting data
                if cls.marker_end_of_param in param_line: break
