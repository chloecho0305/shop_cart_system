@echo off
echo Running Robot Framework tests...
robot --outputdir tests/robot/reports tests/robot/test_sample.robot

echo Running Pytest tests...
pytest tests/unit --html=tests/unit/reports/report.html --self-contained-html

echo All tests completed.
pause