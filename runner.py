# sample behave
# behave -f allure -o ./results .\src\functionality_test\test_search_item.feature
# behave -f allure -f plain -o ./results .\src\mock_api\api_1_test.feature
import subprocess
import argparse

if __name__ == '__main__':
    # argparse
    subprocess.run("behave -f allure -f plain -o ./results .\src\mock_api\api_1_test.feature")