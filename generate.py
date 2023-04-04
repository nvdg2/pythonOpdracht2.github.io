import jinja2
import convert
import pathlib

navbar=""
def generateNavbar():
    global navbar
    pageContent, pageMetaData = convert.getPagesData()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    template= env.get_template("navTemplate.html")
    navbar = template.render(
        pages=pageMetaData
    )

def generatePostHtml():
    postContent, postMetaData = convert.getPostData()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    template = env.get_template("postTemplate.html")
    for i in range(0,len(postContent)):
        renderedPage=template.render(
            postMetaData[i],
            navbar=navbar,
            content=postContent[i]
        )

        destFolder = pathlib.Path(f"site/posts/{postMetaData[i]['filename']}")
        destFolder.mkdir(parents=True,exist_ok=True)
        with open(f"{destFolder}/index.html","w") as htmlPost:
            htmlPost.write(renderedPage)

def generatePageHtml():
    pageContent, pageMetaData = convert.getPagesData()
    for i in range(0,len(pageContent)):
        match pageMetaData[i]["filename"]:
            case "main":
                postMetaData = convert.getPostData()
                env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
                template= env.get_template("mainTemplate.html")
                renderedPage = template.render(
                    pages=pageMetaData,
                    navbar=navbar,
                    posts=postMetaData[1],
                    title=pageMetaData[i]["title"],
                    content=pageContent[i]
                )
                destFolder = pathlib.Path(f"site/pages/{pageMetaData[i]['filename']}")
                destFolder.mkdir(parents=True,exist_ok=True)
                with open(f"{destFolder}/index.html","w") as htmlPost:
                    htmlPost.write(renderedPage)
                            
            case _:
                env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
                template= env.get_template("defaultTemplate.html")
                renderedPage = template.render(
                    navbar=navbar,
                    title=pageMetaData[i]["title"],
                    content=pageContent[i]
                )
                destFolder = pathlib.Path(f"site/pages/{pageMetaData[i]['filename']}")
                destFolder.mkdir(parents=True,exist_ok=True)
                with open(f"{destFolder}/index.html","w") as htmlPost:
                    htmlPost.write(renderedPage)