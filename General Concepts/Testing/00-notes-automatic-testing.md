# Testing

Automated testing uses software to execute your code and compare the actual results with the results you expect.

With automated testing, there comes a tradeoff. Although automated testing enables testers to focus their time
verifying the end-user experience, developers might need to dedicate more time to writing and maintaining their test code.

Types of testing:
1- Development testing: tests you can run before you deploy the application to a test or production environment.
        - lint testing: form of static code analysis, checks your source code to determine whether it conforms to your team's style guide.

        - unit testing: verifies the most fundamental components of your program or library, such as an individual function or method.
          You specify one or more inputs along with the expected results. The test runner performs each test and checks to see whether
          the actual and expected results match.

        - Code coverage testing: computes the percentage of your code that's covered by your unit tests.

# What makes a good test?

- Don't test for the sake of testing
- Keep your tests short
- Ensure that your tests are repeatable
- Keep your tests focused: focus on your own code
- Choose the right granularity