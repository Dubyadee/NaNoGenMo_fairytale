!pip install markovify
import markovify

!pip install weasyprint==52.5
import markdown
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

with open('/content/drive/MyDrive/Defined/grimmstales.txt') as f:
    text1 = f.read()

with open('/content/drive/MyDrive/Defined/realitysurflyrics.txt') as f:
    text2 = f.read()

mastertext = text1 + text2
mastertext = markovify.Text(mastertext)

import random

novel = """


#Once Within a Time


"""

for chapter in range(0, 777):
  novel += f"""

  Epoch {chapter}...

  """

  for i in range(7):
    novel += " " + mastertext.make_sentence()


html = markdown.markdown(novel)

font_config = FontConfiguration()
rendered_html = HTML(string=html)

css = CSS(string='''
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Dancing+Script&display=swap');
body {
font-family: 'Architects Daughter', cursive;
}

hr {
  break-after: recto; 
}

h1 {
  font-size: 45pt;
  text-align:center;
  margin-top: 1in;
  font-family: 'Dancing Script', cursive;
}


h3 {
  font-size: 20pt;
  text-align:center;
}


@page {
  font-family: 'Architects Daughter', cursive;
  margin: 1in;
  size: letter;
  counter-increment: page;
  @bottom-center {
    content: "SUGAR-ISH";
    text-align:center;
    font-style: italic;
    color: #666666;
  }
}


@page :right {
  @bottom-right{
    content: "[" counter(page) "]";
    text-align:right;
    color: #666666;
    visibility: invisible;
  }
}


@page :left {
  @bottom-left{
    content: "[" counter(page) "]";
    text-align:left;
    color: #666666;
  }
}





''', font_config=font_config)

rendered_html.write_pdf('/content/Novelproject.pdf', stylesheets=[css],font_config=font_config)
