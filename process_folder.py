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
    getEntitiesFromAllTextsInFolder("test_data", "test_output")