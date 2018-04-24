from polyglot.text import Text
import sys
import os
import xmlHandler
from sandboxLogger import SandboxLogger
tekst_fil = "test.txt"
with open(tekst_fil) as f:
    test_string = f.read()


class entity_recognizer():
    def __init__(self):
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
            self.entities = Text(text).entities
            self.entity_logger.info(message = "Ekstraksjon av entiteter gjennomført fra tekst-string")
        if filePath:
            if  os.path.isfile(filePath):
                with open(filePath) as f:
                    temp_tekst = f.read()
                self.entities = Text(temp_tekst).entities
                self.entity_logger.info("Entities extracted from {}".format( filePath))
                self.entity_logger.debug("Follow entitites: {} was extracted from file: {}".format(self.entities, filePath))


    def formatEntities(self):
        tags = {"I-LOC" : "Lokasjon", "I-PER" : "Person", "I-ORG" : "Organisasjon"}
        self.prettyEntities = []
        for entity in self.entities:
            self.prettyEntities.append(str(tags[entity.tag]) + ":::"+ ' '.join((entity)))

    def printEntitiesToFile(self,output_file):
        self.formatEntities()
        with open(output_file, "w") as f:
            for entity in self.prettyEntities:
                f.write(entity + "\n")
        self.entity_logger.info("Entites printed to {}".format(output_file))

test_class = entity_recognizer()
test_class.extractEntities(test_string)
test_class.printEntitiesToFile("test_output.txt")
