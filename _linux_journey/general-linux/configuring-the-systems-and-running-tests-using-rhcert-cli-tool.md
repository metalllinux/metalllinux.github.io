---
title: "Chapter 7. Configuring the systems and running tests using RHCert CLI Tool"
category: "general-linux"
tags: ["configuring", "systems", "running", "tests", "rhcert"]
---

# Chapter 7. Configuring the systems and running tests using RHCert CLI Tool

## Chapter 7. Configuring the systems and running tests using RHCert CLI Tool

___

To proceed with the RHEL hardware certification process, configure the systems to run the certification tests.

To complete the RHEL hardware certification process by using CLI, you must prepare the host under test (HUT) and test server, run the tests, and retrieve the test results.

Running the provision command performs a number of operations, such as setting up passwordless SSH communication with the test server, installing the required packages on your system based on the certification type, and creating a final test plan to run, which is a list of common tests taken from both the test plan provided by Red Hat and tests generated on discovering the system requirements.

For instance, required hardware or software packages will be installed if the test plan is designed for certifying a hardware or a software product.

**Prerequisites**

-   You have the hostname or the IP address of the test server.

**Procedure**

1.  Run the provision command in either way. The test plan will automatically get downloaded to your system.
    
    -   If you have already downloaded the test plan:
        
        Copy to Clipboard Toggle word wrap
        
        ```
        # rhcert-provision <path_to_test_plan_document>
        ```
        
        Replace <path\_to\_test\_plan\_document> with the test plan file saved on your system.
        
        Follow the on-screen instructions.
        
    -   If you have not downloaded the test plan:
        
        Copy to Clipboard Toggle word wrap
        
        ```
        # rhcert-provision
        ```
        
        Follow the on-screen instructions and enter your **Certification ID** when prompted.
        
    
2.  When prompted, provide the hostname or the IP address of the test server to set up passwordless SSH. You are prompted only the first time you add a new system.

Running the Provision command enables and starts the `rhcertd` service, which configures services specified in the test suite on the test server, such as iperf for network testing, and an nfs mount point used in kdump testing.

**Prerequisites**

-   You have the hostname or IP address of the host under test.

**Procedure**

1.  Run the provision command by defining the role, “test server”, to the system you are adding.
    
    This is required only for provisioning the test server.
    
    Copy to Clipboard Toggle word wrap
    
    ```
    # rhcert-provision --role test-server <path_to_test_plan_document>
    ```
    
    Replace <path\_to\_test\_plan\_document> with the test plan file saved on your system.
    

**Procedure**

1.  Run the following command:
    
    Copy to Clipboard Toggle word wrap
    
    ```
    # rhcert-run
    ```
    
2.  When prompted, choose whether to run each test by typing `yes` or `no`.
    
    You can also run particular tests from the list by typing `select`.
    

After a test reboot, `rhcert` is running in the background to verify the image. Use `tail -f /_var_/log/rhcert/RedHatCertDaemon.log` to see the current progress and status of the verification.

**Procedure**

1.  Log in to authenticate your device.
    
    Logging in is mandatory to submit the test results file.
    
    Copy to Clipboard Toggle word wrap
    
    ```
    # rhcert-cli login
    ```
    
    1.  Open the generated URL in a new browser window or tab.
    2.  Enter the login and password and click **Log in**.
    3.  Click **Grant access**.
        
        Device log in successful message displays.
        
    4.  Return to the terminal and enter `yes` to the **Please confirm once you grant access** prompt.
    
2.  Submit the result file.
    
    Copy to Clipboard Toggle word wrap
    
    ```
    # rhcert-submit
    ```
    
    When prompted, enter your Certification ID.
    

To proceed with the RHEL AI hardware certification process, configure the systems to run the certification tests.

**Prerequisites**

-   You have the hostname or IP address of the host under test.

**Procedure**

1.  Run the command
    
    Copy to Clipboard Toggle word wrap
    
    ```
    rhcert-provision
    ```
    
    For the question - `Would you like to download the test plan with a certification ID?`, enter `yes`.
    
2.  When prompted, enter your certification ID. You can get this ID from the certification case that you previously created.
    
    After verification, the test suite discovers the supported tests in the HUT. You can view a list of all the supported RHEL AI tests:
    
    1.  `ilab_inferencing`
    2.  `ilab_validation`
    3.  `self_check`
    4.  `supportable`
    5.  `sosreport`
    
3.  Execute the discovered tests.
    
    Copy to Clipboard Toggle word wrap
    
    ```
    rhcert-run
    ```
    
4.  When prompted, choose whether to run all or each test by typing `yes` or `no`.
5.  Submit the RHEL AI test results file, by using any of the following steps:
    
    1.  Run the command
        
        Copy to Clipboard Toggle word wrap
        
        ```
        rhcert-submit
        ```
        
    2.  If your HUT isn’t having internet connectivity, run the command
        
        Copy to Clipboard Toggle word wrap
        
        ```
        rhcert-cli save
        ```
        
        The results file gets saved at the default location. Upload it later by using the [Red Hat Certification Portal](https://rhcert.connect.redhat.com/#/home).
        
    

**Verification**

You get a confirmation message about the results file submission. The results file is submitted for the Red Hat certification team’s review.
