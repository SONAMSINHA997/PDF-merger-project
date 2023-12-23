from pypdf import PdfMerger
import pyttsx3
if __name__=='__main__':
 robo=pyttsx3.init()
 pdfs = ['file1.pdf', 'file3.pdf']

 merger = PdfMerger()

 for pdf in pdfs:
     merger.append(pdf)
    
 merger.write("result.pdf")
 robo.say(" thanku for giving me a chance to merge the file")
 robo.runAndWait()
 robo.say("result.pdf is ready ")
 robo.runAndWait()
 merger.close()
