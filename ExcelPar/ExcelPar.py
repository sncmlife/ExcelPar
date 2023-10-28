#####################################################################
# Excel PAR
# v0.0.7 DD 231026
#####################################################################

# v0.0.4, 231019 : 세부계정 월별순증분석 상단/하단 Logic 변경.
# (기존) 순차기평균 + 순대기(절대값)평균  ==> 문제점. "가중"평균이 아니라 평균을 단순 합산하기때문에 Range가 과도하게 표시됨
# (수정후) 0이 아닌 월 절대값 평균
# v0.0.5, 231019 : FS Line 추가생성 구현
# v0.0.6, 231023 : 상하단 Logic 재변경_이예린SM (Mean ± 2Std)
#####################################################################

# Step1 - Detail

### 1. 전역변수 설정
# ./mod/SetGlobal.py

### 2. Import_GL
# ./mod/ImportGL.py

### 3. PreProcess_GL
# ./mod/PreProcessGL.py

### 4. Import TB
# ./mod/ImportTB.py

### 5. PreprocessTB
# ./mod/PreprocessTB.py

### 6. 분석적검토 자동문구 생성
# ./mod/AnalyzeAccounts.py

### 7. 월별증감/누적월별증감을 계산하여 파일로 추출하는 부
# ./mod/SummarizeMonthlyVarAmount.py

### 8. Lead 생성
# ./mod/CreateLeadReport.py

########################################################

# Step2 - FSLine

### 9.
# ./mod/ChangeTBGL.py

#####################################################################

#####################################################################
class ExcelPar:

    @classmethod
    def Handler(cls):

        #HANDLER
        print("###EXCEL PAR BEGIN:")

        print("\n###Phase1 : Detail")
        
        print("\n#1. 기초정보를 설정합니다.")     
        from ExcelPar.mod.SetGlobal import SetGlobal        
        SetGlobal.SetGlobal()

        print("\n#2-1. GL을 Import합니다.")
        from ExcelPar.mod.ImportGL import ImportGL
        gl = ImportGL.ImportGL() #import하여 gl 객체 선언

        print("\n#2-2. GL을 전처리합니다.")
        from ExcelPar.mod.PreprocessGL import PreprocessGL
        gl = PreprocessGL.PreprocessGL(gl) #gl 객체 가공함

        print("\n#3-1. TB를 Import합니다.")
        from ExcelPar.mod.ImportTB import ImportTB
        tb = ImportTB.ImportTB() #import하여 tb 객체 선언

        print("\n#3-2. TB를 전처리합니다.")
        from ExcelPar.mod.PreprocessTB import PreprocessTB
        tb = PreprocessTB.PreprocessTB(tb) #tb 객체 가공, 일부 STATIC변수 정의(to analyze)

        print("\n#4. 계정별 분석을 실시하고 계정별 분석보고서를 생성합니다.")
        from ExcelPar.mod.AnalyzeAccounts import AnalyzeAccounts
        AnalyzeAccounts.AnalyzeAccounts(gl) #gl을 넣어서 STATIC변수(분석문구)를 업데이트한다.    

        print("\n#5. 계정별 월별/누적월별증감액 보고서를 생성합니다.")
        from ExcelPar.mod.SummarizeMonthlyVarAmount import SummarizeMonthlyVarAmount
        tb_월별 = SummarizeMonthlyVarAmount.SummarizeMonthlyVarAmount(gl,tb) #gl과 tb를 넣어 STATIC WORK, tb_월별을 반환

        print("\n#6. 총괄 분석보고서를 생성합니다.")    
        from ExcelPar.mod.CreateLeadReport import CreateLeadReport
        LeadFileName = CreateLeadReport.CreateLeadReport(tb, tb_월별)

        print("\n#7. 후처리 후 파일을 정리합니다.")    
        from ExcelPar.mod.PostProcess import Postprocess
        Postprocess.Postprocess(LeadFileName)

        print("\n\n###Phase2 : FS Line")

        SetGlobal.Level = "FSLine" #Set class var

        print("\n#0. GL과 TB의 계정과목을 FS Line으로 대체합니다.")    
        from ExcelPar.mod.ChangeTBGL import ChangeTBGL
        tb = ChangeTBGL.ChangeTBGL(gl,tb) #gl은 object reference로 조작, tb는 반환하여 재설정

        print("\n#3-2. TB를 전처리합니다.")
        PreprocessTB.PreprocessTB(tb)    

        print("\n#4. 계정별 분석을 실시하고 계정별 분석보고서를 생성합니다.")
        AnalyzeAccounts.AnalyzeAccounts(gl)

        print("\n#5. 계정별 월별/누적월별증감액 보고서를 생성합니다.")
        tb_월별 = SummarizeMonthlyVarAmount.SummarizeMonthlyVarAmount(gl,tb)    

        print("\n#6. 총괄 분석보고서를 생성합니다.")    
        LeadFileName = CreateLeadReport.CreateLeadReport(tb, tb_월별)

        print("\n#7. 후처리 후 파일을 정리합니다.")    
        Postprocess.Postprocess(LeadFileName)

        print("###EXCEL PAR END:...")        

def RunEP():
    ExcelPar.Handler()

if(__name__=="__main__"):
    pass    