import importlib
import json
import math
import os
import sys


class TestCase:
    input: any
    output: any
    passed: bool

    def __init__(self, input: any, output: any):
        self.input = input
        self.output = output
        self.passed = False


def test_solution(solution_dir):
    solution = get_solution_method(solution_dir)
    test_cases = get_test_cases(solution_dir)
    run_tests(solution, test_cases, solution_dir)


def get_solution_method(solution_dir):
    solution_module = importlib.import_module(f"solutions.{solution_dir}.solution")
    return getattr(solution_module, "solution")


def get_test_cases(solution_dir):
    test_cases = []
    with open(f"./solutions/{solution_dir}/test_cases.json") as file:
        for test in json.load(file)["test_cases"]:
            test_cases.append(TestCase(test["input"], test["output"]))
    return test_cases


def run_tests(solution, test_cases, solution_dir):
    os.system("clear" if os.name == "posix" else "cls")
    print(f'> Running tests for "{solution_dir}"\n')
    for index, test in enumerate(test_cases):
        if test.input:
            print(f"# TEST {index+1}:")
            output = solution(**test.input)
            test.passed = output == test.output
            success_message = "SUCCESS ✅"
            failed_message = f"FAILED ❌ \n - Input:    {test.input} \n - Output:   {output} \n - Expected: {test.output}"
            print(
                "# Result: "
                + (success_message if test.passed else failed_message)
                + "\n---"
            )
        else:
            print("⚠️ You need to add the input/output into the test_cases.json file\n")
            return
    show_result(test_cases)


def show_result(test_cases):
    total_tests = len(test_cases)
    tests_passed = sum(test.passed for test in test_cases)
    passed_rate = math.trunc(tests_passed * 100 / total_tests)

    print(f"👉 Result: {tests_passed} of {total_tests} Tests passed ({passed_rate}%)")
    if tests_passed == total_tests:
        print("🚀 Solution Accepted! 🚀")


if __name__ == "__main__":
    problem_num = sys.argv[1]
    directories = [
        dir for dir in os.listdir("./solutions") if dir.startswith(f"{problem_num} -")
    ]

    if len(directories):
        test_solution(directories[0])
    else:
        print("Invalid number")
