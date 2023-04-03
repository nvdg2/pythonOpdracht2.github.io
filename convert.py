import yaml
import mistune
import os

postsMetadata=[]
postsHTMLContent=[]
pagesMetadata=[]
pagesHTMLContent=[]

def getPostData():
    return postsHTMLContent, postsMetadata

def getPagesData():
    return pagesHTMLContent, pagesMetadata

def convertContentFolder(pathToFolder):
    files=os.listdir(pathToFolder)
    for file in files:
        yamlData, markdownData = splitMarkdownAndYAML(f"{pathToFolder}/{file}")
        type=convertYAMLToDict(yamlData)
        convertMardownToHTML(markdownData,type)

def splitMarkdownAndYAML(pathToFile):
    partYAML=""
    partMarkdown=""
    with open(pathToFile,"r") as file:
        yamlEnded=False
        while True:
            line = file.readline()
            if len(line)==0:
                break
            if yamlEnded==False:  
                partYAML = partYAML+line
                if partYAML.rfind("---") != 0:
                    yamlEnded=True
            else:
                partMarkdown = partMarkdown+line
        partYAML = partYAML.replace("---","")
        
        return partYAML, partMarkdown

def convertYAMLToDict(inputYAML):
    objectYAML= yaml.safe_load(inputYAML)
    if objectYAML["type"]=="post":
        postsMetadata.append(objectYAML)
        return "post"
    else:
        pagesMetadata.append(objectYAML)
        return "page"

def convertMardownToHTML(markdownInput,inType):
    htmlOutput = mistune.html(markdownInput)
    print(inType)
    if inType=="post":
        postsHTMLContent.append(htmlOutput)
    else:
        pagesHTMLContent.append(htmlOutput)
