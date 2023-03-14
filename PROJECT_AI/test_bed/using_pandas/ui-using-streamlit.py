import streamlit as st

import pandas as pd

import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

import os

from  tuple_type_read import ReadFile

with st.sidebar:
    st.title("Project AI")
    choice=st.radio("Navigation",["Upload","Profiling"])
    st.info("This application allows you to build an Auto ML")
from reading_extension import ExtractFileExtension
if choice=="Upload":
    st.title("Upload your data here")
    file=st.file_uploader("Upload your file here")
    #===================================================
    # code snippet for extracting the file extension
    if file:
        file_name=file.name
        _,file_extension=os.path.splitext(file_name)
        file_extension=st.write("File Extension: ", file_extension)
    #====================================================

    #=====================================================
    # Drop down menu for the type of read_ on pandas
        read_file=ReadFile
        read_tup=read_file.type_of_read()
        option=st.selectbox('please select the type of read prompt: ',
                            read_tup) 
    #======================================================

    #======================================================
    # once selected it is concatanated here
        type_of_read="read_"+option
        st.write("you have selceted: ",type_of_read) 
        a=type_of_read
        def func():
            c = 'pd.'
            d = c + a

            # Calling globals()
            globals()['a'] = d
            return d

    # Driver Code
        df=func()
        st.write("your data frame is being processed using:",df)
        #df=pd.concat("."type_of_read)
    #======================================================
        #print(file)
        df_strp=df.strip()
        st.title("For an overview of the data you should refer below:")
        profile_report=df_strp.profile_report()
        st_profile_report(profile_report)
        #
if choice=="Profiling":
    st.title("For an overview of the data you should refer below:")
    profile_report=df.profile_report()
    st_profile_report(profile_report)