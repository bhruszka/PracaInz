import ImageProcessing as ip
import glob, os
os.chdir("E:\\testSet")
i = 1
for file in glob.glob("*.jpg"):
    print(i)
    ip.processImage(file, "E:\\testResults\\", True)
    i += 1





