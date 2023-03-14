import pandas as pd
from pandas_read import ReadData


class WriteData(object):
    #========================
    # Writing to CSV
    def write_to_csv(dataframe, parameters,filepath):
        csv_write=df_csv.to_csv()
        #=========================

        #=========================
        # writing to json
    def write_to_json(dataframe,parameters,filepath):
        json_write=df_json.to_json()
        #==========================

        #==========================
        # writing to html
    def write_to_html(dataframe,parameters,filepath):
        html_write=df_html.to_html()
        #===========================

        #===========================
        #  Writing to LaTex
    def write_to_latex(dataframe,parameters,filepath):
        Latex_write=df_latex.style.to_latex()
        #============================

        #============================
        # Writing to xml
    def write_to_latex(dataframe,parameters,filepath):
        xml_write=df_xml.to_xml()
        #============================


        #=============================
        # writing to excel
    def write_to_excel(dataframe,parameters,filepath):
        excel_write=df_excel.to_excel()
        #=============================

        #=============================
        # writing to HDF5
    def write_to_hdf(dataframe,parameter,filepath):
        hdf_write=df_hdf.to_hdf()
        #=============================

        #=============================
        # writing to feather
    def write_to_feather(dataframe,parameters,filepath):
        feather_write=df_feather.to_feather()
        #=============================

        #=============================
        # writing to parquet
    def write_to_parquet(dataframe,parameters,filepath):
        parquet_write=df_parquet.to_parquet()
        #=============================

        #=============================
        # writing to orc
    def write_to_orc(dataframe,parameters,filepath):
        orc_write=df_orc.to_orc()
        #=============================

        #=============================
        # writing to stata
    def write_to_stata(dataframe,parameters,filepath):
        stata_write=df_stata.to_stata()
        #=============================

        #=============================
        # writing to pickle
    def write_to_pickle(dataframe,parameters,filepath):
        pickle_write=df_pickle.to_pickle()
        #=============================

        #=============================
        # write to sql
    def write_to_sql(dataframe,parameters,filepath):
        sql_write=df_ssql.to_sql()
        #=============================

        #=============================
        #  write to Google BigGuery
    def write_to_gbq(dataframe,parameters,filepath):
        gbq_write=df_gbq.to_gbq()
        #=============================

