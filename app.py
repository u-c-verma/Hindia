from flask import Flask, render_template, request, redirect, send_file

from trans import eng_to_hindi, wrrite_to_doc

app = Flask(__name__)


@app.route('/')
def index():
  #return '<h2> Hello from Replit and Github </h2>'
  return render_template('index.html')


@app.route('/converter', methods=['GET', 'POST'])
def converter():
  if request.method == 'POST':
    letterto = request.form.get('letterto')
    letterdate = request.form['letterdate']
    letteradd = request.form.get('letteradd')
    subject = request.form.get('subject')
    reference = request.form.get('reference')
    letterbody = request.form.get('letterbody')

    # convert input
    letterto = eng_to_hindi(letterto)
    letterdate = eng_to_hindi(letterdate)
    letteradd = eng_to_hindi(letteradd)
    subject = eng_to_hindi(subject)
    reference = eng_to_hindi(reference)
    letterbody = eng_to_hindi(letterbody)

    return render_template('eng_to_hindi_converted.html',
                           letterto=letterto.text,
                           letterdate=letterdate.text,
                           letteradd=letteradd.text,
                           subject=subject.text,
                           reference=reference.text,
                           letterbody=letterbody.text)

  return render_template('eng_to_hindi.html')


@app.route('/convertedDOC', methods=['GET', 'POST'])
def convertedDOC():
  if request.method == 'POST':
    letterto = request.form.get('letterto')
    letterdate = request.form['letterdate']
    letteradd = request.form.get('letteradd')
    subject = request.form.get('subject')
    reference = request.form.get('reference')
    letterbody = request.form.get('letterbody')
    print(letterto)
    """
        # convert input
        letterto = eng_to_hindi(letterto)
        letterdate = eng_to_hindi(letterdate)
        letteradd = eng_to_hindi(letteradd)
        subject = eng_to_hindi(subject)
        reference = eng_to_hindi(reference)
        letterbody = eng_to_hindi(letterbody)
        """

    lst = [
      letterto + '\t\t\t\t\t\t\t' + eng_to_hindi('date').text + ': ' +
      letterdate, letteradd + '\n\n',
      eng_to_hindi('Subject').text + ': ' + subject,
      eng_to_hindi('reference').text + ': ' + reference + '\n\n',
      '\t' + letterbody
    ]

    print(lst)
    wrrite_to_doc(lst)

    path = "Demo.docx"

    #return render_template('eng_to_hindi_converted.html', letterto=letterto, letterdate=letterdate,letteradd=letteradd, subject=subject, reference=reference, letterbody=letterbody)
    #return redirect('/converter')
    return send_file(path, as_attachment=True)

  return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
