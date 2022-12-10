import os
import sys
from typing import Any, NamedTuple, Sequence

import libcst
from libcst.metadata import MetadataWrapper, PositionProvider

class Violation(NamedTuple):
    node: libcst.CSTNode
    message: str
    metadata: Any

class MultipleImportsOnOneLineChecker(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider, )

    def __init__(self) -> None:
        super(MultipleImportsOnOneLineChecker, self).__init__()
        self.issue_code = 'WI001'
        self.violations = set()

    def visit_Import(self, node: "libcst.Import"):
        if len(node.names) > 1:
            pos = self.get_metadata(PositionProvider, node).start
            self.violations.add(Violation(node, "Multiple package imports on one line", pos))

class ScharpieCST:
    def __init__(self) -> None:
        self._checks = set()
        self._violations = []

    def add_checker(self, checker):
        self._checks.add(checker)

    def get_violations(self, file_name):
        for checker, violation in self._violations:
            metadata = violation.metadata
            print(
                f"{file_name} > Line {metadata.line} > Column {metadata.column} -> "
                f"{checker.issue_code}: {violation.message}"
            )

    def run(self, source_path):
        file_name = os.path.basename(source_path)

        with open(source_path) as source_file:
            source_code = source_file.read()
        
        tree = MetadataWrapper(libcst.parse_module(source_code))

        for checker in self._checks:
            tree.visit(checker)
            self._violations.extend([(checker, v) for v in checker.violations])
        
        self._violations = sorted(self._violations, key = lambda v: v[1].metadata.line)
        self.get_violations(file_name)
