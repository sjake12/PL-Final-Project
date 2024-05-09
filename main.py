import pl

while True:
    text = input('pl > ')
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)