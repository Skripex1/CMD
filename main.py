from commands import handle_command
from exceptions import CustomError , handle_exception
def main():
    print("Simple CMD . Use 'exit' to leave. ")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "exit":
            print("Exited")
            break
        try:
            handle_command(user_input)
        except CustomError as ce :
            handle_exception(ce)
        except Exception as e:
            print(f"Eroare: {e}")

if __name__ == "__main__":
    main()
