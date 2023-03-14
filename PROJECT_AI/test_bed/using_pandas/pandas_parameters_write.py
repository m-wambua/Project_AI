import pandas as pd

class OutPutParameters(object):
    #================================
    # CSV writing parameters
    def csv_params_write(dataframe):

        return params_csv_write
    #================================

    #================================
    # JSON writing parameters
    def json_params_write(dataframe):

        return params_json_write

    #================================

    #================================
    # HTML writing parameters
    def html_params_write(dataframe):

        return params_html_write

    #=================================

    #=================================
    # LaTex writing parameters
    def latex_params_write(dataframe):

        return params_html_write
    #==================================

    #==================================
    # XMl writing paramters
    def xml_params_write(dataframe):

        return params_xml_write
    #==================================

    #==================================
    #  clipboard writing parameters
    def clipboard_params_write(dataframe):

        return params_clipboard_write

    #===================================

    #===================================
    # excel writing parameters
    def excel_params_write(dataframe):

        return params_excel_write

    #===================================

    #===================================
    # HDF5 writing parameters
    def hdf_params_write(dataframe):

        return params_excel_write
    #====================================

    #====================================
    # feather writing parameters
    def feather_params_write(dataframe):
        return params_feather_write

    #====================================

    #====================================
    # Parquet writing parameters
    def parquet_params_write(dataframe):

        return params_feather_write

    #====================================

    #====================================
    # ORC writing parameters
    def orc_params_write(dataframe):

        return params_orc_write
    #=====================================

    #=====================================
    # stata writing parameters
    def stata_params_write(dataframe):

        return params_stata_write
    #=====================================

    #=====================================
    # pickle write parameters
    def pickle_params_write(dataframe):

        return params_pickle_write
    #======================================

    #======================================
    # sql write parameters
    def sql_params_write(dataframe):

        return params_sql_write

    #======================================

    #======================================
    # google big query parameters
    def gbq_params_write(dataframe):

        return params_gbq_write
    #======================================