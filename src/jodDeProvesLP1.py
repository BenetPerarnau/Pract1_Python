#!/usr/bin/env python
import sys
import re
moduleName='lp1'
import lp1

niuList=[]


scoresMax=dict({('NIU',.1),
        ('Syntax',0.1),
        ('getWordFreq',0.25),
        ('mergeWordFreqDict',0.25),
        ('wordCount',0.1),
        ('uniqueWordCount',0.1),
        ('__str__',0.1),
        ('getWordsByProbabillity',.1),
        ('isPalindrome',.05)})

obtainedScores=dict({('NIU',0.0),
        ('Syntax',0.0),
        ('getWordFreq',0.0),
        ('mergeWordFreqDict',0.0),
        ('wordCount',0.0),
        ('uniqueWordCount',0.0),
        ('__str__',0.0),
        ('getWordsByProbabillity',.0),
        ('isPalindrome',.0)})

warnings=[]
groups=['NA']
subgroups=['NA']

def conclude(msg='Terminated normally'):
    exceptionMsg='\n\t\t  '+'\n\t\t  '.join([str(m) for m in sys.exc_info() if m != None])
    if exceptionMsg=='\n\t\t  ':
        exceptionMsg=''
    res='Joc-de-proves for '+moduleName+':\n-------------\n\t'
    res=res+'Group    : '+groups[0]
    res=res+'\n\tSubgroup : '+subgroups[0]+'\n\t'
    res=res+'\n\t'.join(['Student  : '+str(niu) for niu in niuList])
    res+='\n-------------\n\tStatus : '+msg+exceptionMsg
    if len(warnings)>0:
        res+='\n'+'Warnings:\n\t'+'\n\t'.join(warnings)
    gradeSum=0
    res+='\n-------------'
    for stage in obtainedScores.keys():
        res+='\n\t'+stage+' : '+str(obtainedScores[stage]/scoresMax[stage])
        gradeSum+=obtainedScores[stage]
    res+='\n-------------\nTotal grade:'+str(10.0*min(gradeSum,1.0))+'/10\n'
    if gradeSum>1:
        res+= 'Bonus points :'+str(10*(gradeSum-1))+'\n'
    else:
        res+='No Bonus.\n'
    res+='\n\nThis grade is an indication of the final grade of this laboratory and can be lower depending on comments, style, etc.'
    print res
    sys.exit(exceptionMsg!='')

def setTaskGrade(taskName,val):
    obtainedScores[taskName]=val*scoresMax[taskName]

def addTaskGrade(taskName,val):
    obtainedScores[taskName]+=val*scoresMax[taskName]



################################################### NIU CORRECT ########################################################
try:
    solutionLines=open(moduleName+'.py').read()
except:
    conclude('Could not read file '+moduleName+'.py')

niuList=list(set([niu[1:-1] for niu in re.findall('[^0-9][0-9]{7,9}[^0-9]',open(moduleName+'.py').read())]))

groups=re.findall('[^b]group\s*[:=]?\s*[0-9]{3}',' '+open(moduleName+'.py').read().lower())
groups=[re.findall('[0-9]{3}',g)[0] for g in groups]
subgroups=re.findall('subgroup\s*[:=]?\s*[0-9][0-9]?',open(moduleName+'.py').read().lower())
subgroups=[re.findall('[0-9][0-9]?',sg)[0] for sg in subgroups]

if len(groups)!=1 or not (groups[0] in ["411","412","413","414","415","416","417","418","419","511","512","513"]):
    print groups
    conclude("Wrong group "+groups[0])

if len(subgroups)!=1 or not int(subgroups[0]) in range(1,14):
    conclude("Wrong subgroup "+subgroups[0])

if(len(niuList)<1):
    conclude('No NIU of participating students Aborting')
elif(len(niuList)>2):
    conclude('More than 2 NIU of participating students found. Aborting')
else:
    if(len(niuList)==1):
        warnings.append('Attention only one student appears in this team')
    setTaskGrade('NIU',1.0)

################################################### SYNTAX CORRECT ########################################################
try:
    exec('import '+moduleName)
    setTaskGrade('Syntax',1.0)
except:
    conclude(' Could not import lp1')

################################################### getWordFreq CORRECT ########################################################
try:
    d=lp1.LanguageModel.getWordFreq('The dog likes the cat, but does the dog like the rooster?')
    addTaskGrade('getWordFreq',.1)
    if d=={'the':4,'dog':2,'likes':1,'cat':1,'but':1,'does':1,'like':1,'rooster':1}:
        addTaskGrade('getWordFreq',.9)
except:
    conclude('Unhadled exception at getWordFreq')

################################################### mergeWordFreqDict CORRECT ########################################################
try:
    d1={'the':4,'dog':2,'likes':1,'cat':1,'but':1,'does':1,'like':1,'rooster':1}
    d2={'the':4,'rooster':1,'batman':3}
    d=lp1.LanguageModel.mergeWordFreqDict(d1,d2)
    addTaskGrade('mergeWordFreqDict',.1)
    if d=={'the':8,'dog':2,'likes':1,'cat':1,'but':1,'does':1,'like':1,'rooster':2,'batman':3}:
        addTaskGrade('mergeWordFreqDict',.9)
except:
    conclude('Unhadled exception at mergeWordFreqDict')

################################################### wordCount CORRECT ########################################################
text="""I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight.  Do you understand this
feeling?  This breeze, which has travelled from the regions towards
which I am advancing, gives me a foretaste of those icy climes.
Inspirited by this wind of promise, my daydreams become more fervent
and vivid.  I try in vain to be persuaded that the pole is the seat of
frost and desolation; it ever presents itself to my imagination as the
region of beauty and delight.  There, Margaret, the sun is forever
visible, its broad disk just skirting the horizon and diffusing a
perpetual splendour.  There for with your leave, my sister, I will put
some trust in preceding navigators there snow and frost are banished;
and, sailing over a calm sea, we may be wafted to a land surpassing in
wonders and in beauty every region hitherto discovered on the habitable
globe.  Its productions and features may be without example, as the
phenomena of the heavenly bodies undoubtedly are in those undiscovered
solitudes.  What may not be expected in a country of eternal light?  I
may there discover the wondrous power which attracts the needle and may
regulate a thousand celestial observations that require only this
voyage to render their seeming eccentricities consistent forever. I
shall satiate my ardent curiosity with the sight of a part of the world
never before visited, and may tread a land never before imprinted by
the foot of man. These are my enticements, and they are sufficient to
conquer all fear of danger or death and to induce me to commence this
laborious voyage with the joy a child feels when he embarks in a little
boat, with his holiday mates, on an expedition of discovery up his
native river. But supposing all these conjectures to be false, you
cannot contest the inestimable benefit which I shall confer on all
mankind, to the last generation, by discovering a passage near the pole
to those countries, to reach which at present so many months are
requisite; or by ascertaining the secret of the magnet, which, if at
all possible, can only be effected by an undertaking such as mine.
"""

extendedText=text+"\nThe preveus passage is from Mary Shelley's Frankenstein."

try:
    lm=lp1.LanguageModel([text])
    wc=lm.wordCount()
    setTaskGrade('wordCount',.1)
    if wc == 384:
        addTaskGrade('wordCount',.2)
        lm.addText(extendedText)
        wc=lm.wordCount()
        if wc == 776:
            addTaskGrade('wordCount',.7)
        else:
            print 'WC = ',wc
except:
    conclude('Exception thrown while testing wordCount')

################################################### uniqueWordCount CORRECT ########################################################
try:
    lm=lp1.LanguageModel([text])
    uwc=lm.uniqueWordCount()
    setTaskGrade('uniqueWordCount',.1)
    if uwc == 226:
        addTaskGrade('uniqueWordCount',.2)
        lm.addText(extendedText)
        uwc=lm.uniqueWordCount()
        if uwc == 230:
            addTaskGrade('uniqueWordCount',.7)
except:
    conclude('Exception thrown while testing uniqueWordCount')


################################################### __str__ CORRECT ########################################################
try:
    out1="LanguageModel\n\t#texts:1\n\t#words:384\n\t#unique words:226\n"
    out2="LanguageModel\n\t#texts:2\n\t#words:776\n\t#unique words:230\n"
    lm=lp1.LanguageModel([text])
    description=str(lm)
    setTaskGrade('__str__',.1)
    if description == out1:
        addTaskGrade('__str__',.2)
        lm.addText(extendedText)
        description=str(lm)
        if description == out2:
            addTaskGrade('__str__',.7)
    else:
        print '{',out1,'}\n{',description,'}'
except:
    conclude('Exception thrown while testing __str__')

################################################### getWordsByProbabillity CORRECT ########################################################
try:
    out1=["the","of","and","a","to","i","in","which","my","may","be","with","this","by","are","there","as","all","those","on","me","you","voyage","these","that","shall","region","pole","or","only","never","land","its","is","his","frost","forever","delight","breeze","before","beauty","at","an","am","your","world","wondrous","wonders","without","wind","will","when","what","we","walk","wafted","vivid","visited","visible","vain","upon","up","undoubtedly","undiscovered","undertaking","understand","try","trust","tread","travelled","towards","thousand","they","their","surpassing","supposing","sun","sufficient","such","streets","splendour","some","solitudes","so","snow","skirting","sister","sight","seeming","secret","seat","sea","satiate","sailing","river","requisite","require","render","regulate","regions","reach","put","promise","productions","presents","present","preceding","power","possible","play","phenomena","petersburgh","persuaded","perpetual","passage","part","over","observations","not","northern","north","nerves","needle","near","navigators","native","more","months","mine","mates","margaret","many","mankind","man","magnet","london","little","light","leave","last","laborious","just","joy","itself","it","inspirited","inestimable","induce","imprinted","imagination","if","icy","horizon","holiday","hitherto","heavenly","he","has","habitable","globe","gives","generation","from","foretaste","for","foot","fills","fervent","feels","feeling","feel","features","fear","far","false","expedition","expected","example","every","ever","eternal","enticements","embarks","effected","eccentricities","do","disk","discovery","discovering","discovered","discover","diffusing","desolation","death","daydreams","danger","curiosity","country","countries","contest","consistent","conquer","conjectures","confer","commence","cold","climes","child","cheeks","celestial","cannot","can","calm","but","broad","braces","bodies","boat","benefit","become","banished","attracts","ascertaining","ardent","already","advancing"]
    out2=["the","of","and","a","to","i","in","which","my","may","be","with","this","by","are","there","as","all","those","on","me","is","you","voyage","these","that","shall","region","pole","or","only","never","land","its","his","frost","forever","delight","breeze","before","beauty","at","an","am","passage","from","your","world","wondrous","wonders","without","wind","will","when","what","we","walk","wafted","vivid","visited","visible","vain","upon","up","undoubtedly","undiscovered","undertaking","understand","try","trust","tread","travelled","towards","thousand","they","their","surpassing","supposing","sun","sufficient","such","streets","splendour","some","solitudes","so","snow","skirting","sister","sight","seeming","secret","seat","sea","satiate","sailing","river","requisite","require","render","regulate","regions","reach","put","promise","productions","presents","present","preceding","power","possible","play","phenomena","petersburgh","persuaded","perpetual","part","over","observations","not","northern","north","nerves","needle","near","navigators","native","more","months","mine","mates","margaret","many","mankind","man","magnet","london","little","light","leave","last","laborious","just","joy","itself","it","inspirited","inestimable","induce","imprinted","imagination","if","icy","horizon","holiday","hitherto","heavenly","he","has","habitable","globe","gives","generation","foretaste","for","foot","fills","fervent","feels","feeling","feel","features","fear","far","false","expedition","expected","example","every","ever","eternal","enticements","embarks","effected","eccentricities","do","disk","discovery","discovering","discovered","discover","diffusing","desolation","death","daydreams","danger","curiosity","country","countries","contest","consistent","conquer","conjectures","confer","commence","cold","climes","child","cheeks","celestial","cannot","can","calm","but","broad","braces","bodies","boat","benefit","become","banished","attracts","ascertaining","ardent","already","advancing","shelley","preveus","mary","frankenstein"]
    lm=lp1.LanguageModel([text])
    wbp=lm.getWordsByProbabillity()
    setTaskGrade('getWordsByProbabillity',.1)
    if wbp == out1:
        addTaskGrade('getWordsByProbabillity',.2)
        lm.addText(extendedText)
        wbp=lm.getWordsByProbabillity()
        if wbp == out2:
            addTaskGrade('getWordsByProbabillity',.7)
except:
    conclude('Exception thrown while testing getWordsByProbabillity')

################################################### isPalindrome CORRECT ########################################################
sentences=[
    "A large palindrome is hard to find",
    "Go hang a lasagna Im a salami hog",
    "As I pee, sir, I see Pisa",
]
try:
    resp=[lp1.isPalindrome(sent) for sent in sentences]
    setTaskGrade('isPalindrome',.1)
    if resp == [False,False,True]:
        addTaskGrade('isPalindrome',.9)
except:
    conclude('Exception thrown while testing isPalindrome')

conclude('Testcase Terminated Normally')