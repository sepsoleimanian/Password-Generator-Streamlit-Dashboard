import streamlit as st 
from password_generator import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

st.image("/mnt/c/users/snapp/desktop/Password-Generator-Streamlit-Dashboard/images/banner.png", width = 700)
st.title(":zap: Password Generator")

option = st.radio(
  "Select a password generator:",
  ("Random Password", "Memorable Password", "Pin Code")
)

if option == 'Pin Code':
  length = st.slider("Select the length of the pin code", 4, 32)
  generator = PinGenerator(length)
  password = generator.generate()

elif option == 'Random Password':
    length = st.slider("Select the length of the password", 6, 32)
    include_symbols = st.toggle("include symbols:")
    include_numbers = st.toggle("include number:")
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
    password = generator.generate()

elif option == 'Memorable Password':
    number_of_words = st.slider("Number of words", 2, 8)
    seperator = st.text_input("Seperator", value = '-')
    capitalization = st.toggle("capitalization:")
    generator = MemorablePasswordGenerator(number_of_words, seperator, capitalization)
    password = generator.generate()

st.write(fr"Your password is: ‍‍‍`{password}` ")
