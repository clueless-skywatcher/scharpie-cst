import libcst

from scharpie_cst.checkers.base import BaseCSTChecker

class NotInLoopChecker(BaseCSTChecker):
    '''
    Error: Break/continue statement is not in a loop
    '''
    def __init__(self) -> None:
        super(NotInLoopChecker, self).__init__(issue_code = 'EC001')
        self.message = "{not_in_loop} statement is not in a loop"

    def _has_stray_break(self, node):
        if isinstance(node, libcst.SimpleStatementLine):
            for child in node.body:
                if isinstance(child, libcst.Break):
                    return True
                elif isinstance(child, (libcst.If, libcst.With)):
                    return self._has_stray_break(child)
        return False
    
    def _has_stray_continue(self, node):
        if isinstance(node, libcst.SimpleStatementLine):
            for child in node.body:
                if isinstance(child, libcst.Continue):
                    return True
                elif isinstance(child, (libcst.If, libcst.With)):
                    return self._has_stray_continue(child)
        return False

    def visit_Module(self, module: "libcst.Module"):
        for node in module.body:
            if self._has_stray_break(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'break'})
            if self._has_stray_continue(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'continue'})

    def visit_If(self, if_statement: "libcst.If"):
        for node in if_statement.body.body:
            if self._has_stray_break(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'break'})
            if self._has_stray_continue(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'continue'})

    def visit_With(self, with_statement: "libcst.With"):
        for node in with_statement.body.body:
            if self._has_stray_break(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'break'})
            if self._has_stray_continue(node):
                self.report_violation(node, message_formatting={'not_in_loop': 'continue'})