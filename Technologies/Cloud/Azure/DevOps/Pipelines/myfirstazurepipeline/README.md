This folder contains the code to build and run an Azure Pipeline from Azure DevOps.

This lab follows step by step this link: https://menziess.github.io/howto/run/databricks-notebooks-from-devops/

Note thet it requires an existing csv document in the specified routes with the especific data

The datalake routes are:
- /mnt/crm_bronze/test_ppl/input_data/sample.csv
- /mnt/crm_bronze/test_ppl/output_data/output.csv

Sample csv must be a csv file with the following data:
Name,Age
Guzman,26

The provided python files must be on a databricks workspace. Note that you will have to change the variable values in the yaml file if the notebooks are uploaded to a different path.

Steps:
1- Create notebook.py
2- Create test.py: which checks the output of notebook.py is correct
3- Create .yaml file that executes test.py on Azure Pipelines
4- Run the Pipeline