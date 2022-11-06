def entity_parser(text):
    dic = {'&apos;': "'",
           '&gt;': '>',
           '&lt;': '<',
           '&frasl;': '/'}
    for key, value in dic.items():
        text = text.replace(key, value)
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    return text


print(entity_parser(text="x &gt; y &amp;&amp; x &lt; y is always false"))
