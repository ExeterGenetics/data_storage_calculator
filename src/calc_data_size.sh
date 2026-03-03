#!/bin/bash
# Find dataset sizes in a given folder in a given UKB-RAP project


main() {
  ##Define input and output file names
  datetime=$(date +"%Y%m%dT%H%M")
  project_str=${project// /_} #convert any spaces in the project name to underscores
  folder=${folder##/} # remove any leading slashes from the folder name
  if [[ ${folder} == */ ]]; then
    folder=${folder%/} #remove any trailing slash from the folder name
  fi
  folder_str=${folder//[\/ ]/_} #convert any slashes or spaces in the folder name to underscores
  data_details=${datetime}_${project_str}_${folder_str}_"data_files.json"
  analysed_data_details=${datetime}_${project_str}_${folder_str}_"total_data_storage.json"
  analysed_data_plot=${datetime}_${project_str}_${folder_str}_"total_data_storage.pdf"

  ##Make the Python script executable
  chmod u+x calculate_total_data_storage.py
     
  ##Find all data
  echo " "
  echo "########## Finding all data in the selected UKB-RAP project folder ###########"		
  identify_datasets
    
  ##Analyse json file to compute total data storage
  echo " "
  echo "########### Computing total data storage ###########"
  analyse_datasets	

  echo " "
  echo "########### Finished running ###########"
  echo " "
}


identify_datasets() {
  # find data files and output details to a json file
  folder_path="${project}:/${folder}/"
  dx find data --path "${folder_path}" --verbose --json > "${data_details}"
  
  # upload output file to UKB-RAP project
  output_file1=$(dx upload "${data_details}" --path "${upload_path}/" --brief)
  dx-jobutil-add-output output_file1 "${output_file1}" --class=file
}

analyse_datasets() {
  # go through the data_details.json file and calculate the total storage
  python3 calculate_total_data_storage.py "${project_str}" "${folder_str}" "${data_details}" "${analysed_data_details}" "${analysed_data_plot}"
  
  # upload output files to UKB-RAP project
  output_file2=$(dx upload "${analysed_data_details}" --path "${upload_path}/" --brief)
  dx-jobutil-add-output output_file2 "${output_file2}" --class=file

  output_file3=$(dx upload "${analysed_data_plot}" --path "${upload_path}/" --brief)
  dx-jobutil-add-output output_file3 "${output_file3}" --class=file
}

