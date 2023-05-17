#pip install googletrans==4.0.0-rc1
#pip uninstall googletrans==4.0.0-rc1
#pip install googletrans==3.1.0a0

from googletrans import Translator
import docx


def eng_to_hindi(cmd):

  translator = Translator()
  result = translator.translate(
    cmd,
    src='auto',
    dest='hi',
  )

  return result


def wrrite_to_doc(st):

  doc = docx.Document()
  for s in st:
    doc.add_paragraph(s)

  doc.save('Demo.docx')


if __name__ == '__main__':

  cmd = """
        Operations & Maintenance 
        """

  result = eng_to_hindi(cmd)
  #print(result)
  print(type(result.text))
  print(result.text)

  lst = [cmd]
  wrrite_to_doc(lst)
