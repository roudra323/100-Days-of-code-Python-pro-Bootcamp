s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# ENCODER
st = input('Enter text without spaces: ').upper()
st = st.replace(' ', '')
shift = 1
cy = ''
cyD = ''
code = input('Which code? ').upper()
if code == 'EN':
    for i in st:
        cy += s[s.index(i) + shift]
    print(cy)
# DECODER
else:
    for i in st:
        cyD += s[s.index(i) - shift]
    print(cyD)
