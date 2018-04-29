from polyglot.text import Text
import sys
import os
import xmlHandler
from sandboxLogger import SandboxLogger
import nltk
tekst_fil = "test.txt"
with open(tekst_fil) as f:
    test_string = f.read()


class entity_recognizer():
    def __init__(self):
        self.text = None
        self.entities = None
        self.tags = None
        self.prettyEntities = None
        self.entity_logger = SandboxLogger("entity-recognizer-testlogger", "logging_config.config")
        self.entity_logger.info("Entity object intialized.")
    def extractEntities(self, text = None, filePath = None):
        if text and filePath:
           self.entity_logger.error("Fatal error: text (string) and file-input cannot be input at the same time. Undefined behavior")
           sys.exit(0)
        if text:
            self.text =text
            self.entities = Text(text).entities
            self.entity_logger.info(message = "Ekstraksjon av entiteter gjennomført fra tekst-string")
        if filePath:
            if  os.path.isfile(filePath):
                with open(filePath) as f:
                    self.text = f.read()
                self.entities = Text(text).entities
                self.entity_logger.info("Entities extracted from {}".format( filePath))
                self.entity_logger.debug("Follow entitites: {} was extracted from file: {}".format(self.entities, filePath))
        self.formatEntities()

    def formatEntities(self):
        tags = {"I-LOC" : "Lokasjon", "I-PER" : "Person", "I-ORG" : "Organisasjon"}
        self.prettyEntities = []
        for entity in self.entities:
            self.prettyEntities.append((str(tags[entity.tag]) , ' '.join((entity))))

    def extractPositionOfEntity(self):
        print("Her skal posisjonene til entitetene ekstraheres")
        tokenized_text = nltk.word_tokenize(self.text, language = "norwegian")
        entity_indexes = []
        for entity in self.entities:
            print(' '.join(entity))
            positions_of_entity = []
            print(' '.join(entity).split()[0])
            for word in enumerate(tokenized_text):

                if ' '.join(entity).split()[0] == word[1]:
                    positions_of_entity.append(word[0])
            entity_indexes.append(positions_of_entity)
        print(entity_indexes)

    def getLengthOfEntity(self, entity):
        return(len(entity.split()))

    def printEntitiesToFile(self,output_file):
        with open(output_file, "w") as f:
            for entity in self.prettyEntities:
                f.write(' '.join(entity) + "\n")
        self.entity_logger.info("Entites printed to {}".format(output_file))

    def printAsXML(self, printToScreen=True, printToFile = False, output_file_name = None):
        xml = xmlHandler.xmlHandler(rootNodeName="entities")
        root = xml.getRootNode()
        for entity in self.prettyEntities:
            entity_length = self.getLengthOfEntity(entity[1])
            xml.addSubElement(root,"entity", attr= {"entity-type":entity[0], "entitet":entity[1], "entity_length" : str(entity_length)})
        if printToScreen:
            xml.prettyPrintToScreen()
        if printToFile:
            if output_file_name:
                xml.printTreeToFile(output_file_name)
            else:
                self.entity_logger.error("FATAL ERROR: Filepath not defined. XML cannot be printed")

test_class = entity_recognizer()
test_class.extractEntities(test_string)
test_class.printEntitiesToFile("test_output.txt")
test_class.printAsXML(True,False, "test.xml")
test_class.extractPositionOfEntity()
#print(test_class.entities)