from entity_recog  import entity_recognizer
import os
from pythonlibs.sandboxLogger import SandboxLogger
#input_dir = "/home/ubuntu/PycharmProjects/entity_recog/test_data"
entity_folder_logger = SandboxLogger("entity-recognizer-folder_logger", "logging_config.config")



def getTxtFilePaths(path_to_folder):
    list_of_txt_files = []
    for root, dirs, files in os.walk(path_to_folder):
        for file in files:
            if file.endswith(".txt"):
                list_of_txt_files.append(os.path.join(root, file))
    return list_of_txt_files

def getEntitiesFromAllTextsInFolder(input_folder, output_folder):
    input_files = getTxtFilePaths(input_folder)
    for txt_file in input_files:
        entities =  entity_recognizer()
        entity_folder_logger.info("Initializing Entity extraction from {}".format(txt_file))
        
        with open(txt_file, "r") as f:
            input_txt_file = f.read()
        if len(input_txt_file.split())>5:
          entities.extractEntities(input_txt_file)
          output_file_name = "test_output"+txt_file.replace(".txt",".entity")
          output_file_name = os.path.split(output_file_name)[1]
          entities.printAsXML(False, True,output_folder+"/" + output_file_name)
def getNameOfSubfolders(folder):
    folder_paths = [x[0] for x in os.walk(folder)]    
    folder_paths = folder_paths[1:]
    folder_names = [os.path.basename(os.path.normpath(x[0])) for x in os.walk(folder)]
    folder_names = folder_names[1:]
    return folder_paths, folder_names

def getEntitiesFromAllTextsInSubFolders(input_folder, output_folder):
    folder_paths, folder_names = getNameOfSubfolders(input_folder)
    for i, path in enumerate(folder_paths):
        current_output_folder = output_folder+"/"+folder_names[i]
        if not os.path.exists(current_output_folder):
           os.makedirs(current_output_folder)       

        getEntitiesFromAllTextsInFolder(path, current_output_folder)
        print(str(i) +"/" + str(len(path)) + "is done")
if __name__ == "__main__":
  getEntitiesFromAllTextsInSubFolders("/disk1/aw_experiments/aw_avisText", "/disk1/aw_experiments/entity_recognized/avis_entities")
  #print(getNameOfSubfolders("/disk1/avisText"))    
  #getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT01", "/disk1/aw_experiments/entity_recognized/test_folder")
   # getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT02", "/disk1/aw_experiments/entity_recognized/radio_entities/ENT02_len3")
  #  getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT03", "/disk1/aw_experiments/entity_recognized/radio_entities/ENT03_len3")

#    getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/tv_transcripts/TXT01", "/disk1/aw_experiments/entity_recognized/tv_entities/ENT01_len3")
 #   getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/tv_transcripts/TXT02", "/disk1/aw_experiments/entity_recognized/tv_entities/ENT02_len3")   
