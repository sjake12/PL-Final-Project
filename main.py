import pl

while True:
    text = input('pl > ')
    result, error = pl.run('<stdin>'.text)

    if error: print(error.as_string())
    else: print(result)