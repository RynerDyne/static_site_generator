from textnode import TextType, TextNode

def main():
    name = TextNode("created test text", TextType.LINK, "http://boot.dev")
    print(name)

main()
