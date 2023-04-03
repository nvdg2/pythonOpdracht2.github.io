import jinja2
import convert
import pathlib

def generatePostPages():
    postContent, postMetaData = convert.getPostData()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    template = env.get_template("postTemplate.html")
    for i in range(0,len(postContent)):
        renderedPage=template.render(
            postMetaData[i],
            content=postContent[i]
        )

        destFolder = pathlib.Path(f"_site/posts/{postMetaData[i]['filename']}")
        destFolder.mkdir(parents=True,exist_ok=True)
        with open(f"{destFolder}/index.html","w") as htmlPost:
            htmlPost.write(renderedPage)
