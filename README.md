# Airflow Log Analyzer

The following code is an extension of the project titled **pyfinance_data_orchestration**, which comprises a DAG that downloads data from PyFinance at a given time interval, moves the data to a specific directory, and performs a basic query of the data. This project focuses on analyzing the log files that are generated during the Airflow run, usually located within the Airflow project and respective DAG directory.



This code recursively searches all relevant sub-directories using the ***Path*** object from the **pathlib** class (Python 3.4+ required) and reads each file to identify, count, and store the 'ERROR' logs that were generated throughout the Airflow run. The final ouput is printed to terminal and contains (1) the total number of errors and (2) the content of the error messages.



Given that the previous project is downloaded and run using Airflow, the only user input required is the path for the relevant logs folder. This would be be used as a command line argument in the following format:



```bash
python3 logAnalyzer.py <path_to_dag_log_folder>
```



The expected output would look as follows:



