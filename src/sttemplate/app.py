# import streamlit as st

# def main():
#     st.title("sttemplate")


# if __name__ == "__main__":
#     main()


def hello():
    print("Hello world")


def show_count(count, word) -> str:
    if count == 1:
        return f"1 {word}"
    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"


print(show_count(99, "bird"))

print(show_count(1, "bird"))

print(show_count(0, "bird"))


def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b
