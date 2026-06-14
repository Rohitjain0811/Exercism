def translate(text):
    if ' ' in text:
        return ' '.join(translate(word) for word in text.split())

    vowels = 'aeiou'
    if text[0] in vowels or text.startswith('xr') or text.startswith('yt'):
        return text + 'ay'
    
    for i in range(len(text)):
        if text[i] in vowels or (i > 0 and text[i] == 'y'):
            if text[i] == 'u' and i > 0 and text[i-1] == 'q':
                return text[i+1:] + text[:i+1] + 'ay'
            return text[i:] + text[:i] + 'ay'
            
    return text + 'ay'