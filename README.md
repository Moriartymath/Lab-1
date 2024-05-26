# Lab 2

## Author : Strelia Illia

## Group id : IM-23

## This is console application written in Python to convert _Markdown_ file to _HTML_ or _ANSI_ formats

## Requirements: Python 3.X version

## Input parameterts :

- **_Required argument_** (first parameter) : Path to the input Markdown file

## Optional arguments

### flag --out :

- **_Optional argument_** to specify the output file otherwise converted text will be displayed in console : **Path to the output file**

### flag --format :

- **_Optional argument_** if present the result of executing program will be in HTML format otherwise in ANSI: **Specify the format of resulting text**

## Example of using:

- ### **With Optional argument**

  #### **flag --out**

  ```console
  python main.py  markdown_file.md --out  text_file.txt
  ```

  - **The result will be in ANSI format and saved to text_file.txt**

  #### **flag --format**

  ```console
  python main.py  markdown_file.md  --format
  ```

  - **The result will be in HTML format in the output of console**

  #### **flag --out and --format**

  ```console
  python main.py  markdown_file.md  --out html_file.html --format
  ```

  - **The result will be in HTML format and saved to the html_file.html**

- ### **Without optional argumenet**

  ```console
  python main.py  markdown_file.md
  ```

  - **The result will be in HTML(mistake) format in the output of console**

  - Added redundant text for revert commit

### [Link to Revert commit](https://github.com/Moriartymath/Lab-1/commit/e09040369e38e7443fd29d60dd7a216999cb0438) - e09040369e38e7443fd29d60dd7a216999cb0438
