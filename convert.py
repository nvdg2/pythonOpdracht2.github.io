import yaml
import mistune

postsMetadata=[]
postsHTMLContent=[]

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
        postsMetadata.append(objectYAML)
        print(postsMetadata)
def convertMardownToHTML(markdownInput):
    htmlOutput = mistune.html(markdownInput)
    postsHTMLContent.append(htmlOutput)
    print(postsHTMLContent)

yamlData, markdownData = splitMarkdownAndYAML("posts\post1.md")
convertYAMLToDict(yamlData)
convertMardownToHTML(markdownData)

