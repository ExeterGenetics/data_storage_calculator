<!-- dx-header -->
# Data Storage Calculator
This is the source code for an applet that runs on the DNAnexus Platform. This applet calculates the total storage for each user in a given folder in a given project on the UK Biobank Research Analysis Platform (UKB-RAP).
<!-- /dx-header -->

## Applet inputs
The applet has three inputs:
1. **project:** the name of the UKB-RAP project in which to calculate the data storage.
2. **folder:** the name of the folder in the UKB-RAP project to be searched (if not a top-level folder then the full path should be given e.g., top_level_folder/folder_to_search).
3. **upload_path:** the directory to upload results to. This should include the UKB-RAP project name (e.g., project_name:/path/to/directory/) and the output directory should be located in the same project in which the applet is run.

All three inputs are mandatory.

## Applet outputs
The applet produces three outputs:
1. **\<datetime\>\_\<project\>\_\<folder\>_data_files.json:** a file containing the details for all the files found in the folder that was searched.
2. **\<datetime\>\_\<project\>\_\<folder\>_total_data_storage.json:** a file containing the total data storage for each user in the folder that was searched.
3. **\<datetime\>\_\<project\>\_\<folder\>_total_data_storage.pdf:** a plot of the total data storage for each user in the folder that was searched.

All output files are uploaded to the location provided in input 3.

## Building this applet
To run this applet in DNAnexus, you need to: 
1. Clone this repo using:  
`git clone https://github.com/ExeterGenetics/data_storage_calculator.git`.
2. Log in to the UKB-RAP via the command line using either an authentication token that you have already set up or using:  
`dx login`.  
Note that this requires the [dx-toolkit](https://documentation.dnanexus.com/downloads#dnanexus-platform-sdk) to be installed and you can find more information on the [dx-toolkit command line utilities](https://documentation.dnanexus.com/user/helpstrings-of-sdk-command-line-utilities) and options available in the documentation.
3. Select the UKB-RAP project you want to work in using:  
`dx select <project_name>`.
4. Move to the folder in the UKB-RAP project that you want to build the applet in using:  
`dx cd <folder_name>`.
5. Build the applet to the UKB-RAP using:  
`dx build data_storage_calculator`.
6. You can then run the applet in the UKB-RAP web browser or via the command line e.g.,:  
`dx run data_storage_calculator -iproject="UKB-RAP_project_name" -ifolder="folder_to_search" -iupload_path="UKB-RAP_project_name:/path/to/folder/"`  
This will run the data_storage_calculator on "folder_to_search" in the UKB-RAP project "UKB-RAP_project_name" and upload the outputs to /path/to/folder/ in the provided UKB-RAP project.


## Contact
If you have any questions about running this applet, contact Chris Tibbs ([c.t.tibbs@exeter.ac.uk](mailto:c.t.tibbs@exeter.ac.uk)).

