from textnode import TextNode, TextType

def main():
    name = TextNode("created test text", TextType.LINK, "http://boot.dev")
    print(name)

main()
