import os, re, shutil

datePattern = re.compile(r"""^(.*?)
            ((0|1)?\d)-
            ((1|2|3)?\d)-
            ((19|20)?\d\d)
            ((.*?)$)
            """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue

    beforePart = mo.group(1)
    mounthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + mounthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilepath = os.path.join(absWorkingDir, amerFilename) 
    euroFilepath = os.path.join(absWorkingDir, euroFilename)

    print('Change name: "%s", to name: "%s"...'
          % (amerFilepath, euroFilepath))
    shutil.move(amerFilepath, euroFilepath)

