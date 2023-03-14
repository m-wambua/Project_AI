import pandas as pd

#===================================
# CVS and Text files
# read_csv()
class ReadData(object):

    def read_from_csv(filepath,parameter):
        df_csv=pd.read_csv()
        return df_csv
        # Basic
        # 1. parameter is the filepath_or_buffer 
        # path
        # 2. parameter is the sep seperator
        # 3. is the delimiter which is an alternative argument to the  separeter
        # 4. delim_whitespace : boolean, default False: specifies 
        # whether or not whitespace will be used as the delimiter. if this
        # option is set True, nothing should be passed in for the delimiter parameter.


        # Column and Index locations and names
        # 1. Header: int or list of ints, default 'infer'
        # Row number(s) to us as the column names and the start of the data. Default behavior
        # is to infer the column names: if no names are passed the behavior is identical to header=0 and column 
        # names are inferred from the first line of the file, if column
        # names are passed explicitly then the behavior is identical to header=None. Explictly pass
        # header=0 to be able to replace existing names. The header can be a list if ints that specify
        # row locations for a MultiIndex on the columns. intervining rows
        # that are not specified will be skipped. Header=0 denotes the first line of data rather than the first line of the 
        # file.
        # 
        # 2. names: array-like,default None
        # list of column names to use. if file contains no header row, then you should explicitly pass hearder=None. Duplicates in this list are not allowed#




        #==============================
        # Reading JSON
    def read_from_json(filepath,parameters):
        df_json=pd.read_json()
        return df_json
        #===============================

        #===============================
        # Reading Fixed width text
    def read_from_fwf(filepath,parameters):
        df_fwf=pd.read_fwf()
        return df_fwf
        #===============================

        #===============================
        # Reading HTML
    def read_from_html(filepath,parameters):
        df_hmtl=pd.read_html()
        return df_hmtl
        #================================

        #================================
        # Reading XML
    def read_from_xml(filepath,parameters):
        df_xml=pd.read_xml()
        return df_xml
        #================================

        #================================
        # Reading local clipboard
    def read_from_clipboard(filepath,parameters):
        df_clipboard=pd.read_clipboard()
        return df_clipboard
        #================================

        #================================
        # Read MS EXCEL
    def read_from_excel(filepath,parameters):
        df_excel=pd.read_excel()
        return df_excel
        #=================================

        #=================================
        # Read Open Document
    def read_from_opendoc(filepath,parameters):
        df_opendoc=pd.read_excel()
        return df_opendoc

        #===================================

        #===================================
        # Reading HDF5
    def read_from_hdf(filepath,parameter):
        df_hdf=pd.read_hdf()
        return df_hdf

        #====================================

        #====================================
        #  Reading Feather format
    def read_from_feather(filepath,parameter):
        df_feather=pd.read_feather()
        return df_feather
        #=====================================

        #=====================================
        # Reading Parquet
    def read_from_parquet(filepath,parameters):
        df_parquet=pd.read_parquet()
        return df_parquet
        #======================================

        #======================================
        # Read ORC
    def read_from_orc(filepath,parameters):
        df_orc=pd.read_orc
        return df_orc

        #=======================================

        #=======================================
        # Read Stata
    def read_from_stata(filepath,parameters):
        df_stata=pd.read_stata()
        return df_stata
        #=======================================

        #=======================================
        #  Read SAS
    def read_from_sas(filepath,parameters):
        df_sas=pd.read_sas()
        return df_sas
        #=======================================

        #=======================================
        # Read SPSS
    def read_from_spss(filepath,parameters):
        df_spss=pd.read_spss()
        return df_spss
        #========================================

        #========================================
        # read Python Pickle Format
    def read_from_pickle(filepath,parameters):
        df_pickle=pd.read_pickle()
        return df_pickle
        #=========================================

        #=========================================
        # Read SQL
    def read_from_sql(filepath,parameters):
        df_sql=pd.read_sql()
        return df_sql
        #==========================================

        #==========================================
        # Read SQL query
    def read_from_sql_query(filepath,parameters):
        df_sql_query=pd.read_sql_query()
        return df_sql_query
        #==========================================

        #==========================================
        # Read SQL table
    def read_from_sql_table(filepath,parameters):
        df_sql_table=pd.read_sql_table()
        return df_sql_table
        #==========================================

        #===========================================
        # Read Google BigQuery
    def read_from_gbq(filepath,paraeters):
        df_gbq=pd.read_gbq()
        return df_gbq
        #============================================