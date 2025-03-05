import re
import sys

def convert_ordered_lists(text):
  
    lines = text.splitlines()
    output = []
    inside_list = False
    for line in lines:
        # See if the line matches an ordered list item pattern
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if m:
            if not inside_list:
                output.append("<ol>")
                inside_list = True
            output.append(f"<li>{m.group(2)}</li>")
        else:
            if inside_list:
                output.append("</ol>")
                inside_list = False
            output.append(line)
    if inside_list:
        output.append("</ol>")
    return "\n".join(output)

def MD_to_HTML(text):
    #Headers
    text =re.sub(
        r"^(?P<hashes>#{1,6})\s+(?P<text>.+)$",
        lambda m: f"<h{len(m.group('hashes'))}>{m.group('text')}</h{len(m.group('hashes'))}>",
        text)
    #Bold
    text = re.sub(
        r"\*\*(?P<text>.+)\*\*",
        lambda m: f"<b>{m.group('text')}</b>",       
        text)
    #Italic
    text = re.sub(
        r"\*(?P<text>.+)\*",
        lambda m: f"<i>{m.group('text')}</i>",       
        text)
    #numbered list
    text = convert_ordered_lists(text)
    #link
    text = re.sub(
        r"[^\!]\[(?P<text>.*?)\]\((?P<link>.*\)",
        lambda m: f'<a href="{m.group('link')}"> {m.group('text')} </a>',
        text
    )
    #image
    text = re.sub(
        r"\!\[(?P<text>.*)\]\((?P<link>.*\)",
        lambda m: f'<img src="{m.group('link')}"> alt={m.group('text')} />',
        text
    )

    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ex3.py <markdown_text>")
        sys.exit(1)

    
    html = MD_to_HTML(sys.argv[1])
    print(html)