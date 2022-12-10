
import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.checkers.base import BaseCSTChecker
from scharpie_cst.scharpie_cst import Violation

class MultipleImportsOnOneLineChecker(BaseCSTChecker):
    METADATA_DEPENDENCIES = (PositionProvider, )

    def __init__(self) -> None:
        super(MultipleImportsOnOneLineChecker, self).__init__(issue_code='WI001')
        self.violations = set()

    def visit_Import(self, node: "libcst.Import"):
        if len(node.names) > 1:
            pos = self.get_metadata(PositionProvider, node).start
            self.violations.add(Violation(node, "Multiple package imports on one line", pos))