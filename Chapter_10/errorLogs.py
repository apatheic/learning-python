import traceback
try:
    raise Exception('This message about error.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Call stack information was written to the file errorInfo.txt.') 

