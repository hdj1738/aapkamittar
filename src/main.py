def main():
    print("AapkaMitter is alive.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AapkaMitter: Bye!")
            break

        print(f"AapkaMitter: You said '{user_input}'")


if __name__ == "__main__":
    main()