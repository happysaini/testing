# **Migration utility : TestRail Project Migration from one server/cloud to another server/cloud**

- [Introduction](#introduction)
- [Migration Utility Setup](#migration-utility-setup)
  - [Prerequisites](#prerequisites)
- [Migration utility scripts/files along with their directory structure](#migration-utility-scripts)    
- [Utility Execution and working](#execution-and-working)
    - [Phase-1: Migrate Project and Test Suites](#phase-1)
        - [Introduction](#phase-1-introduction)
        - [Execution Steps/Commands](#execution-step-phase-1)
    - [Phase-2: Manually Import/Export Test Cases and Add Customizations](#phase-2)
        - [Introduction](#phase-2-introduction)
        - [Manual Steps](#execution-step-phase-2)
    - [Phase-3: Migrate Test Runs and Test Plans](#phase-3)
        - [Introduction](#phase-3-introduction)
        - [Execution Steps/Commands](#execution-step-phase-3)
    - [Phase-4: Manually Add Attachments](#phase-4)
        - [Introduction](#phase-4-introduction)
        - [Manual Steps](#execution-step-phase-4)

## **Introduction**<a name="introduction"></a><br/>
The aim of this `Migration Utility` is to migrate the TestRail Project from one TestRail server/cloud to another TestRail server/cloud. It is designed in Python 2.7.

## **Migration Utility Setup** <a name="migration-utility-setup"></a><br/>
To setup this migration utility, user needs to checkout its code base.

  - **Prerequisites:** <a name="prerequisites"></a><br/>
  Below packages must be installed on the Linux node or windows node, where we want to run this `utility`:
      - Python( v2.7 )
      - Python modules named testrail, re, and json

**Note:** To install python modules, user can use requirements.txt file with below command:
      ```
      pip install -r requirements.text
      ```

## **Migration utility scripts/files along with their directory structure** <a name="migration-utility-scripts"></a><br/>
The file directory structure is show below:
```
.
└── conf
    └──config.json
└── testrail_migration
    ├── ___init__.py
	├── testrail.py
    ├── testrail_migration_server_to_cloud.py
    └── utils.py
├── requirements.txt
└── README.md
```
  - **config.json** <br/>This file is one of the important file for in Migration utility. `config.file` stores the configuration needed for this utility like host address of both the old and new TestRail server/cloud along with user credentials which will be used for establishing connection.
  
  - **testrail.py** <br/> This file TestRail API Binding for Python 

  - **testrail_migration_server_to_cloud.py**</br> This the main execution script that serve the purpose of migrating TestRail Project, Test Suites, Milestones, Test Runs and Test Plans from one TestRail server/cloud to another. This file use of another utility file  `utils.py` for simplification of flow of control.

  - **utils.py**</br>This file contains two classes and all the important functions/methods that are been used by the main script `testrail_migration_server_to_cloud.py` for the migration purpose

  - **requirements.txt**</br> This file is to install Python modules needed to be install for this migration utility

## **Ulitity Execution and working** <a name="execution-and-working"></a><br/>
Migration Utility is designed in such a manner that it works in two phases/steps.
### **Phase-1: Migrate Project and Test Suites** <a name="phase-1"></a>
  - **Introduction** <a name="phase-1-introduction"></a><br/>
  In this phase/step, utility will migrate all the important details of TestRail Project, Test Suites in the Project and Milestone. Once it migrate the Test Suites data, user have to manually export and import the Test Cases in the respective Test Suites from old server/cloud to new server/cloud.

  - **Execution Steps/Commands** <a name="execution-step-phase-1"></a>
  Below is the command that needs to be executed for migrating Project, Test Suites and Milestones. We need to give flag `--migrate` along with three or required arguments depends on the number of Test Suites to be migrated `--source_testrail_project_name` , `--destination_testrail_project_name` and `--source_testrail_test_suites`.

  ```
  python testrail_migration_server_to_cloud.py --migrate --source_testrail_project_name <PROJECT_NAME> --destination_testrail_project_name <NEW_PROJECT_NAME> --source_testrail_test_suites <TEST_SUITE_NAME> --source_testrail_test_suites <TEST_SUITE_NAME>
  ```
  Example:
  ```
  python testrail_migration_server_to_cloud.py --migrate --source_testrail_project_name "Sensor Management Platform" --destination_testrail_project_name "Sensor Management Platform" --source_testrail_test_suites "DCO Endpoints" --source_testrail_test_suites "DCO Endpoints Manual Tests Suite" --source_testrail_test_suites "SMP - API Test Suite" --source_testrail_test_suites "SMP - UI - Test Suite"
  ```


### **Phase-2: Manually Import/Export Test Cases and Add Customizations** <a name="phase-2"></a>
  - **Introduction** <a name="phase-2-introduction"></a><br/>
    In this phase/step, we have to manually export test cases from old TestRail server/cloud and then import them in new TestRail server/cloud after making some important changes in the file. Below are the steps that have to be performed:

  - **Manual Steps** <a name="execution-step-phase-2"></a>
 


### **Phase-3: Migrate Test Runs and Test Plans** <a name="phase-3"></a>
  - **Introduction** <a name="phase-3-introduction"></a><br/>
    In this phase/step, utility will migrate Test Runs, Test Plans and Test Results data from old server/cloud to new server/cloud.

  - **Execution Steps/Commands** <a name="execution-step-phase-3"></a>
  Below is the command that needs to be executed to read the bug's required data from JSON to import the issues in GitHub .We need to give flag `--import_issues` along with one required arguments `--project_key`.

  ```
  python testrail_migration_server_to_cloud.py --migrate_test_runs --source_testrail_project_name <PROJECT_NAME> --destination_testrail_project_name <NEW_PROJECT_NAME> --source_testrail_test_suites <TEST_SUITE_NAME> --source_testrail_test_suites <TEST_SUITE_NAME>
  ```
  Example:
  ```
  python testrail_migration_server_to_cloud.py --migrate_test_runs --source_testrail_project_name "Sensor Management Platform" --destination_testrail_project_name "Sensor Management Platform" --source_testrail_test_suites "DCO Endpoints" --source_testrail_test_suites "DCO Endpoints Manual Tests Suite" --source_testrail_test_suites "SMP - API Test Suite" --source_testrail_test_suites "SMP - UI - Test Suite"
  ```


### **Phase-4: Manually Add Attachments** <a name="phase-4"></a>
  - **Introduction** <a name="phase-4-introduction"></a><br/>
    In this phase/step, utility will migrate Test Runs, Test Plans and Test Results data from old server/cloud to new server/cloud.

  - **Manual Steps** <a name="execution-step-phase-4"></a>
  Below is the command that needs to be executed to read the bug's required data from JSON to import the issues in GitHub .We need to give flag `--import_issues` along with one required arguments `--project_key`.

  ```
  python testrail_migration_server_to_cloud.py --migrate_test_runs --source_testrail_project_name <PROJECT_NAME> --destination_testrail_project_name <NEW_PROJECT_NAME> --source_testrail_test_suites <TEST_SUITE_NAME> --source_testrail_test_suites <TEST_SUITE_NAME>
  ```
  Example:
  ```
  python testrail_migration_server_to_cloud.py --migrate_test_runs --source_testrail_project_name "Sensor Management Platform" --destination_testrail_project_name "Sensor Management Platform" --source_testrail_test_suites "DCO Endpoints" --source_testrail_test_suites "DCO Endpoints Manual Tests Suite" --source_testrail_test_suites "SMP - API Test Suite" --source_testrail_test_suites "SMP - UI - Test Suite"
  ```
