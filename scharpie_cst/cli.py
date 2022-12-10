import sys
from typing import Sequence

from scharpie_cst.scharpie_cst import ScharpieCST
from scharpie_cst.checkers.imports import (
    MultipleImportsOnOneLineChecker,
    PdbSetTraceChecker
)
from scharpie_cst.checkers.variables import (
    SetHasDuplicateItemChecker,
    DictHasDuplicateKeyChecker
)

class LinterCLI:
    @staticmethod
    def cli(argv: Sequence[str] = sys.argv):
        source_paths = argv[1:]

        for path in source_paths:
            linter = ScharpieCST()

            linter.add_checker(MultipleImportsOnOneLineChecker())
            linter.add_checker(PdbSetTraceChecker())
            linter.add_checker(SetHasDuplicateItemChecker())
            linter.add_checker(DictHasDuplicateKeyChecker())

            linter.run(path)