import textwrap
# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

word_list = wrapper.wrap(text=value)

# Print each line.
for element in word_list:
    print(element)

#error
