from stack import Stack
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"


def reverse_string(string):
    st = Stack()
    for c in string:
        st.push(c)


    reversed_string = ""
    while not st.is_empty():
        reversed_string += st.peek()
        st.pop()
    

    return reversed_string


if __name__ == "__main__":
    string = "We will conquere COVID-19"

    result = reverse_string(string)
    print(result)

