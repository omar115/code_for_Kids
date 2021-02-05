def test(text):
    input_text = text1.get("1.0", "end")
    out = translator.translate(input_text, lang_tgt=text)
    print('translated text is ',out)
    text2.insert('end', out)

btn = Button(root, text='arabic', bg='red', fg='black', command=lambda: test('ar'))
btn.grid(row=1, column=2, padx=10, pady=10)