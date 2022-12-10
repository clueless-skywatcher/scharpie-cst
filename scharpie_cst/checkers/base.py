import libcst

class BaseCSTChecker(libcst.CSTVisitor):
    def __init__(self, issue_code) -> None:
        self.issue_code = issue_code
        self.violations = set()