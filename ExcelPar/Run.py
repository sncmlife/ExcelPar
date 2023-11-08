import ExcelPar as ep

def run(): #LOWER CASE
    Text = """
read README.md
1. TB 전처리부 : PreGL.RunPreTB() 
2-1. Excel 합치기 : ConcatExcelFiles.RunConcateExcelFiles()
2-2. Text 합치기 : ConcatTextFiles.RunConcateTextFiles()
2-3. Text를 Slicing해서 합치기 : SliceAndSaveGL.RunSliceAndSaveGL()
2-4. BKPF+BSEG Join : JoinBKPFBSEG
3. GL 전처리부 : PreGL.RunPreGL()
4. Excel Par Main분석부 : ExcelPar.RunEP()
    """
    print(Text)

    while True:
        match input("input number>>"):
            case '1':
                ep.RunPreTB()
            case '2-1':
                ep.RunConcatExcelFiles()
            case '2-2':
                ep.RunConcatTextFiles()
            case '2-3':
                ep.RunSliceAndSaveGL()        
            case '2-4':
                print("아직 메서드로 구현하지 않았습니다.") 
            case '3':
                ep.RunPreGL()
            case '4':
                ep.RunEP()
            case _:
                print("END")

if __name__=='__main__':
    run()