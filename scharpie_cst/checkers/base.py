import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.scharpie_cst import Violation

class BaseCSTChecker(libcst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider, )

    def __init__(self, issue_code) -> None:
        self.issue_code = issue_code
        self.message = None
        self.violations = set()

    def report_violation(self, node: libcst.CSTNode, metadata = None, message_formatting = {}):
        if not metadata:
            metadata = self.get_metadata(PositionProvider, node).start
        self.violations.add(Violation(node, self.message.format(**message_formatting), metadata))