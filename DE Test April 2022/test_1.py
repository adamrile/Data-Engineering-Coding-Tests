"""Programme to check if a log line is valid by checking """
import re

def is_log_line(line:str) -> bool:
    """Takes a log line and returns True if it is a valid log line and returns False
    if it is not.
    """
    pattern = r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2} \w+ +:.*'
    if re.match(pattern, line):
        return True
    return False




def get_dict(line: str) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    timestamp_pattern = r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}'
    error_pattern = r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2} (\w+)'
    message_pattern = r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2} (\w+) +(:.*)'
    timestamp = re.search(timestamp_pattern, line).group(0)
    log_level = re.search(error_pattern, line).group(1)
    message = re.search(message_pattern, line).group(2)
    dict_ = {"timestamp": timestamp, "log_level": log_level, "message": message}
    return dict_



if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_line(log_file: str) -> str:
        """Opens the file, checks if a line is valid"""
        with open(log_file, encoding='utf-8') as file:
            for line in file:
                if is_log_line(line):
                    yield line

    def log_parser_dict(log_file: str) -> dict:
        """Uses the line from the logfile then runs the get_dict function"""
        with open(log_file, encoding='utf-8') as file:
            for line in file:
                if is_log_line(line):
                    yield get_dict(line)


    # ---- TESTS ---- #

    def test_step_1():
        """First test"""
        with open("tests/step1.log", encoding='utf-8') as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_line("sample.log"))

        if actual_out == test_lines:

            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w", encoding='utf-8') as f:
                f.writelines(actual_out)

    def test_step_2():
        """Second test"""
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_dict("sample.log"))
        print(actual)

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
