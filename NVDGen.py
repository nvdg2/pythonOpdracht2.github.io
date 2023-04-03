import convert
import generate
if __name__=="__main__":
    convert.convertContentFolder("posts")
    convert.convertContentFolder("pages")
    generate.generatePostHtml()
    generate.generatePageHtml()