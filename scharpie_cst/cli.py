import sys
from typing import Sequence

from scharpie_cst.scharpie_cst import ScharpieCST

from scharpie_cst.checkers.base import BaseCSTChecker
from scharpie_cst.checkers.code import *
from scharpie_cst.checkers.imports import *
from scharpie_cst.checkers.variables import *

class LinterCLI:
    @staticmethod
    def cli(argv: Sequence[str] = sys.argv):
        source_paths = argv[1:]

        checkers = BaseCSTChecker.__subclasses__()

        for path in source_paths:
            linter = ScharpieCST()
            
            for checker in checkers:
                linter.add_checker(checker())

            linter.run(path)