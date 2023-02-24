import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.checkers.base import BaseCSTChecker

__all__ = [
    'LineEndingSemicolonChecker'
]

class LineEndingSemicolonChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super(LineEndingSemicolonChecker, self).__init__(issue_code = 'CC001')
        self.message = 'Semicolon at end of line'

    def visit_SimpleStatementLine(self, node: "libcst.SimpleStatementLine"):
        last_statement = node.body[-1]
        if isinstance(last_statement.semicolon, libcst.Semicolon):
            metadata = self.get_metadata(PositionProvider, last_statement.semicolon).start
            self.report_violation(node, metadata)