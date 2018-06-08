from entity_recog  import entity_recognizer
import os
input_dir = "/home/ubuntu/PycharmProjects/entity_recog/test_data"


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
        with open(txt_file, "r") as f:
            input_txt_file = f.read()
        entities.extractEntities(input_txt_file)
        output_file_name = "test_output"+txt_file.replace(".txt",".entity")
        output_file_name = os.path.split(output_file_name)[1]
        entities.printAsXML(False, True,output_folder+"/" + output_file_name)
if __name__ == "__main__":
    getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT01", "/disk1/aw_experiments/entity_recognized/test_folder")
   # getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT02", "/disk1/aw_experiments/entity_recognized/radio_entities/ENT02_len3")
  #  getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/radio_transcripts/TXT03", "/disk1/aw_experiments/entity_recognized/radio_entities/ENT03_len3")

#    getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/tv_transcripts/TXT01", "/disk1/aw_experiments/entity_recognized/tv_entities/ENT01_len3")
 #   getEntitiesFromAllTextsInFolder("/disk1/aw_experiments/tv_transcripts/TXT02", "/disk1/aw_experiments/entity_recognized/tv_entities/ENT02_len3")   
