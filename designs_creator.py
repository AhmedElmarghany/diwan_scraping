from html2image import Html2Image
from PIL import Image
import time

htmi = Html2Image(output_path="designs")

def crop_image(path):
    img = Image.open("designs\\" + path)

    # Deminisions
    width, height = 1473, 1080
    x, y = 447, 9

    # Select area to crop
    area = (x, y, width, height)

    # Crop and save image
    cropped_img = img.crop(area)
    cropped_img.save("designs\\" + path)

def create_design(quote, id):
    if len(quote) == 4:
        one_line_design =f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      text-align: center;
    }}
    .first{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      bottom: 565px;
      right: 548px;
    }}
    .second{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 535px;
      left: 548px;
    }}
    .logo {{
      position: absolute;
      top: 300px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      width: 10%;
    }}
   .author-name {{
      position: absolute;
      top: 780px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      color: #366b89;
    }}

  </style>
  <title>Quote Design</title>
</head>
<body>
  <div class="container">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\template.png" style="width:54%;">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\logo.png" class="logo">
    <div class="first">{quote[0]}</div>
    <div class="second">{quote[1]}</div>
    <div class="author-name">{quote[-1]}</div>
  </div>
  
</body>
</html>
"""
        htmi.screenshot(html_str = one_line_design, save_as=f'{id}.png')
        crop_image(f'{id}.png')
    elif len(quote) == 6:
        two_lines_design =f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      text-align: center;
    }}
    .first{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 350px;
      right: 548px;
    }}
    .second{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 450px;
      left: 548px;
    }}
    .third{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 550px;
      right: 548px;
    }}
    .forth{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 650px;
      left: 548px;
    }}

    .logo {{
      position: absolute;
      top: 220px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      width: 10%;
    }}
   .author-name {{
      position: absolute;
      top: 863px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      color: #366b89;
    }}

  </style>
  <title>Quote Design</title>
</head>
<body>
  <div class="container">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\template.png" style="width:54%;">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\logo.png" class="logo">
    <div class="first">{quote[0]}</div>
    <div class="second">{quote[1]}</div>
    <div class="third">{quote[2]}</div>
    <div class="forth">{quote[3]}</div>
    <div class="author-name">{quote[-1]}</div>
  </div>
  
</body>
</html>
"""
        htmi.screenshot(html_str= two_lines_design, save_as=f'{id}.png')
        crop_image(f'{id}.png')
    elif len(quote) == 8:
        three_lines_design =f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      text-align: center;
    }}
    .first{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 238px;
      right: 548px;
    }}
    .second{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 338px;
      left: 548px;
    }}
    .third{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 438px;
      right: 548px;
    }}
    .forth{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 538px;
      left: 548px;
    }}
    .fifth{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 638px;
      right: 548px;
    }}
    .sixth{{
      color: #366b89;
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      position: absolute;
      top: 738px;
      left: 548px;
    }}


    .logo {{
      position: absolute;
      top: 163px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      width: 10%;
    }}
   .author-name {{
      position: absolute;
      top: 921px;       /* Edit this only */
      left: 50%;
      transform: translate(-50%, -50%);
      font-family: 'Aref Ruqaa', Bold;
      font-size: 60px;
      color: #366b89;
    }}

  </style>
  <title>Quote Design</title>
</head>
<body>
  <div class="container">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\template.png" style="width:54%;">
    <img src="C:\\Users\\Ahmad\\Desktop\\projects\\Diwan qoutes\\design\\logo.png" class="logo">
    <div class="first">{quote[0]}</div>
    <div class="second">{quote[1]}</div>
    <div class="third">{quote[2]}</div>
    <div class="forth">{quote[3]}</div>
    <div class="fifth">{quote[4]}</div>
    <div class="sixth">{quote[5]}</div>
    <div class="author-name">{quote[-1]}</div>
  </div>
  
</body>
</html>
"""
        htmi.screenshot(html_str= three_lines_design, save_as=f'{id}.png')
        crop_image(f'{id}.png')
    else :
        pass
quote = []
counter = 0

start = time.time()

with open("quotes.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        
        if (line != "====================\n") and (line != ""):
            quote.append(line.strip("\n"))
        elif line == "====================\n":
            counter += 1
            if counter % 10 == 0:
              print(f"{counter} designs created")
            create_design(quote, counter)
            quote = []
        elif line == "":
            print("__ Done __")
            break

print(f"__ It took {time.time() - start} sec __ or __ {(time.time() - start) / 60} min __")