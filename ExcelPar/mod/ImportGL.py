import pandas as pd
import os

import dask.dataframe as dd

from ExcelPar.mylib import myFileDialog as myfd
from ExcelPar.mylib.ErrRetry import ErrRetry
from ExcelPar.mod.SetGlobal import SetGlobal

class ImportGL :
    @classmethod
    @ErrRetry
    def ImportGL(cls) -> dd.DataFrame|pd.DataFrame:

        flag = input("Select multi-gl files with dask?(Y) >>")
        if flag == 'Y':
            SetGlobal.bDask = True #Flag처리

            glPath = myfd.askdirectory("Select GL Folder to read *.parquet") #PHW            

            ext = input("확장자 parquet or tsv(기본 parquet)>>") or 'parquet'
            match ext:
                case 'parquet':
                    glTgt = glPath + "/*.parquet"
                    gl = dd.read_parquet(glTgt) #return gl
                case 'tsv':
                    glTgt = glPath + "/*.tsv"
                    encod = input("인코딩 (기본 utf8)>>") or 'utf8'
                    gl = dd.read_csv(glTgt, encoding=encod, sep='\t'
                                    , dtype={'DetailCode': 'object'
                                    ,'계정과목코드': 'object'}) #return gl
                case _:
                    print("ERROR...")
            
        else:
            SetGlobal.bDask = False #Flag처리

            glFile = myfd.askopenfilename("Select GL File") #PHW
            #glFile = './imported/dfGL.parquet'

            ext = os.path.splitext(glFile)
            match ext[1]:
                case '.tsv' | 'txt':
                    gl = pd.read_csv(glFile, encoding="utf-8-sig", sep="\t", low_memory=False)
                case '.parquet':
                    gl = pd.read_parquet(glFile)
                case _:
                    print("TSV 또는 Parquet를 선택하세요")
        
        return gl