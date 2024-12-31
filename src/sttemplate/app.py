import streamlit as st


def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def demo() -> None:
    st.title("Welcome!")
    st.markdown(
        """

    Make this page *yours*!
    You can make changes in you editor and see the changes in the browser right
    away

    Be sure to see what else is possible with
    [Streamlit](https://streamlit.io/)


    """
    )


def main() -> None:
    print("This file was run directly")


if __name__ == "__main__":
    main()
    demo()
