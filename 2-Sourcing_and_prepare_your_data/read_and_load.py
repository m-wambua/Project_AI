# So in general:Pyspark,Tensorflow,PyTorch,Scikit-learn,Beam,Pandas,Dask,Xarray,Numpy
import sys
import os
import requests
import tkinter as tk
from tkinter import ttk

#filename =  sys.argv[1]
from tkinter import filedialog as fd


# filename=fd.askopenfilename()
# ==============================================

# Uploading so far works
root = tk.Tk()

root.title('Please upload a file')


# text=tk.Text(root,height=12)
# text.grid(column=0,row=0,sticky='nsew')
a_label = ttk.Label(root, text="upload your files here")
a_label.grid(column=0, row=0)


def open_text_file():

    f = fd.askopenfilename()
    open_button.configure(text="** YOURFILES HAVE BEEN UPLOADED!**")
    a_label.configure(foreground='blue')
    a_label.configure(text='A blue label')

    # text.insert('1.0',f.readlines)


open_button = ttk.Button(
    root,
    text='locate your files here!!',
    command=open_text_file

)

open_button.grid(column=1, row=0)
open_button.pack()
#action=ttk.Button(root,text='click here to upload your files', command= open_text_file)
# action.grid(column=1,row=0)

root.mainloop()


#filename= open_text_file()

#print("you file has been uploaded!!")


# =============================================

# Loading different formats of files

# Pyspark
# ==============================================
# Import the PySpark library
def choice_pyspark():
    from pyspark.sql import SparkSession

    # Create a SparkSession
    spark_csv = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the CSV file
    df_spark_csv = spark_csv.read.csv("/path/to/file.csv")

    # Print the schema of the DataFrame
    spark_json = SparkSession.builder.appName("MyApp").getOrCreate()

    df_spark_json = spark_json.read.json("/path/to/file.json")

    # ==============================================
    spark_parquet = SparkSession.builder.appName("MyApp").getOrCreate()

    df_spark_parquet = spark_parquet.read.parquet("/path/to/file.parquet")

    # ===============================================
    spark_orc = SparkSession.builder.appName("MyApp").getOrCreate()

    df_spark_orc = spark_orc.read.orc("/path/to/file.orc")

    # ================================================
    spark_hive = SparkSession.builder.appName(
        "MyApp").enableHiveSupport().getOrCreate()

    # Read the Hive table
    df_spark_hive = spark_hive.table("my_table")
    # ===============================================================

    spark_hbase = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the HBase table
    df_spark_hbase = spark_hbase.read.options(
        catalog="hbase", table="my_table")

    # ===============================================================
    spark_avro = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the Avro file
    df_spark_avro = spark_avro.read.format("avro").load("/path/to/file.avro")

    # ===============================================================
    spark_seq = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the sequence file
    df_spark_seq = spark_seq.read.format("sequence").load("/path/to/file.seq")

    # ==================================================================

    spark_pb = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the Protocol Buffer file
    df_spark_pb = spark_pb.read.format("protobuf").load("/path/to/file.pb")
    # =====================================================================
    spark_txt = SparkSession.builder.appName("MyApp").getOrCreate()

    # Read the text file
    df_spark_txt = spark_txt.read.text("/path/to/file.txt")


# Tensorflow
# ==============================================
def choice_tensorflow():
    import tensorflow as tf
    import pandas as pd

    # Load the CSV file into a tensor
    data_csv = tf.io.decode_csv("/path/to/file.csv", record_defaults=[0, 0])

    # Convert the tensor to a DataFrame
    df_ts_csv = pd.DataFrame(data_csv)
    # =====================================================================
    data_json = tf.io.decode_json_example("/path/to/file.json")

    # Convert the tensor to a DataFrame
    df_ts_json = pd.DataFrame(data_json)


# ==============================================

# Pytorch
# ===============================================

# ===============================================

# Scikit-learn
# ===============================================

# ===============================================

# Beam
# ===============================================

# ===============================================

# Pandas
# ===============================================

# ===============================================

# Dask
# ===============================================

# ===============================================

# Xarray
# ===============================================

# ===============================================

# Numpy
# ===============================================

# ===============================================
